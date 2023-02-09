import uvicorn
from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from config import settings
from crud.product_crud import get_product, get_products, delete_product
from crud.category_crud import get_categories
from exceptions import is_url_image
from routers import categories, products
from services import add_tables, get_db
from models import Category, Product

add_tables()

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
    terms_of_service=settings.terms_of_service,
    contact=settings.contact,
    license_info=settings.license_info,
)

app.include_router(categories.router)
app.include_router(products.router)

# Линк статики
app.mount('/static', StaticFiles(directory='static'), name='static')

# Шаблоны через Jinja2
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def index(
    request: Request, db: Session = Depends(get_db)
):
    '''Главная страница с выводом по циклу товаров и завернутые в bootstrap'''

    return templates.TemplateResponse('index.html', {
        'request': request,
        'products': await get_products(db),
    })


@app.get('/product/{product_id}', response_class=HTMLResponse)
async def product_detail(
    product_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    '''Товар в деталях'''

    return templates.TemplateResponse('product_detail.html', {
        'request': request,
        'product': await get_product(db, product_id),
    })


@app.get('/create_product', response_class=HTMLResponse)
async def create_product_get(
    request: Request, db: Session = Depends(get_db)
):
    '''Форма создания продукта'''

    return templates.TemplateResponse('create_product.html', {
        'request': request,
        'categories': await get_categories(db),
    })


@app.post('/create_product', response_class=HTMLResponse)
async def create_product_post(
    request: Request, db: Session = Depends(get_db),
    name: str = Form(...), price: int = Form(...), count: int = Form(...),
    category_id: int = Form(...), image_url: str = Form(None),
):
    '''Форма создания продукта'''

    categories = await get_categories(db)

    # Проверка на обязательность категории
    if category_id == 0:
        return templates.TemplateResponse('product_no_category.html', {
            'request': request, 'name': name, 'categories': categories,
        })

    # Эксепт на валидность изображения в ссылке
    if is_url_image(image_url):
        return templates.TemplateResponse('product_no_image.html', {
            'request': request, 'name': name, 'categories': categories,
        })

    # Заглушка
    if image_url is None:
        image_url = 'https://p2payer.com/images/profile_nophoto.jpg'

    product = Product(name=name, price=price, count=count,
                      category_id=category_id, image_url=image_url)
    db.add(product)
    db.commit()
    db.refresh(product)

    return templates.TemplateResponse('create_product_done.html', {
        'request': request, 'name': name, 'categories': categories,
    })


@app.get('/product/delete/{product_id}', response_class=HTMLResponse)
async def delete_product_get(
    product_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    '''Удаление товара'''

    product = await get_product(db, product_id)
    await delete_product(db, product)

    return templates.TemplateResponse('delete_done.html', {
        'request': request,
    })


@app.get('/create_category', response_class=HTMLResponse)
async def create_category_get(
    request: Request, db: Session = Depends(get_db)
):
    '''Форма создания категории'''

    return templates.TemplateResponse('create_category.html', {
        'request': request,
        'categories': await get_categories(db),
    })


@app.post('/create_category', response_class=HTMLResponse)
async def create_category_post(
    request: Request, db: Session = Depends(get_db), name: str = Form(...),
):
    '''Форма создания категории'''

    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)

    return templates.TemplateResponse('create_category_done.html', {
        'request': request, 'name': name,
    })


if __name__ == '__main__':
    '''Для дебаггинга'''

    uvicorn.run(app, host="0.0.0.0", port=8000)
