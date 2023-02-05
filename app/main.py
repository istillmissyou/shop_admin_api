import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from crud.product_crud import get_products
from routers import categories, products
from services import add_tables, get_db

add_tables()

app = FastAPI(
    title='Store API',
    description='API for the admin panel for the online store',
    version='0.1.4',
    terms_of_service='https://github.com/istillmissyou/'
                     'shop_admin_api/blob/main/LICENSE',
    contact={
        "name": "Данил Штунь",
        "url": "https://github.com/istillmissyou",
        "email": "danilshtun@yandex.ru",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
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

    products = await get_products(db)
    return templates.TemplateResponse(
        'index.html', {
            'request': request, 'products': products, 'categories': categories
        }
    )


if __name__ == '__main__':
    '''Для дебаггинга'''

    uvicorn.run(app, host="0.0.0.0", port=8000)
