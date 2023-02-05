from crud.product_crud import get_products
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services import add_tables, get_db
from sqlalchemy.orm import Session
from routers import categories, products
import uvicorn

add_tables()

app = FastAPI(
    title='Store API',
    description='API for the admin panel for the online store',
    version='0.0.7',
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

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def index(
    request: Request, db: Session = Depends(get_db)
):
    products = await get_products(db)
    return templates.TemplateResponse(
        'index.html', {
            'request': request, 'products': products, 'categories': categories
        }
    )


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
