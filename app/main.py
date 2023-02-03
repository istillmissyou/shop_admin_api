import crud
from exceptions import exc_404
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schemas import Category, CategoryCreate, Product, ProductCreate
from services import add_tables, get_db
from sqlalchemy.orm import Session

add_tables()

app = FastAPI(
    title='Store API',
    description='API for the admin panel for the online store',
)

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def index(
    request: Request, db: Session = Depends(get_db)
):
    products = await crud.get_products(db)
    categories = await crud.get_categories(db)
    return templates.TemplateResponse(
        'index.html', {
            'request': request, 'products': products, 'categories': categories
        }
    )


@app.get('/api/products', response_model=list[Product])
async def get_products(db: Session = Depends(get_db)):
    return await crud.get_products(db)


@app.get('/api/products/{product_id}', response_model=Product)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = await crud.get_product(db, product_id)
    exc_404(product)

    return product


@app.post('/api/products', response_model=Product)
async def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return await crud.create_product(db, product)


@app.put('/api/products/{product_id}', response_model=Product)
async def update_product(
    product_id: int,
    product_data: ProductCreate,
    db: Session = Depends(get_db),
):
    product = await crud.get_product(db, product_id)
    exc_404(product)

    return await crud.update_product(db, product_data, product)


@app.delete('/api/products/{product_id}', response_model=Product)
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = await crud.get_product(db, product_id)
    exc_404(product)

    return await crud.delete_product(db, product)


@app.get('/api/categories', response_model=list[Category])
async def get_categories(db: Session = Depends(get_db)):
    return await crud.get_categories(db)


@app.get('/api/categories/{category_id}', response_model=list[Category])
async def get_products_by_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    return await crud.get_products_by_category(db, category_id)


@app.post('/api/categories', response_model=Category)
async def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
):
    return await crud.create_category(db, category)


@app.put('/api/categories/{category_id}', response_model=Category)
async def update_category(
    category_id: int,
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
):
    category = await crud.get_category(db, category_id)
    exc_404(category)

    return await crud.update_category(db, category_data, category)


@app.delete('/api/categories/{category_id}', response_model=Category)
async def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    category = await crud.get_category(db, category_id)
    exc_404(category)

    return await crud.delete_category(db, category_id)
