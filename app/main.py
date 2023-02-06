import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from config import settings
from crud.product_crud import get_products
from routers import categories, products
from services import add_tables, get_db

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

    products = await get_products(db)
    return templates.TemplateResponse(
        'index.html', {
            'request': request, 'products': products, 'categories': categories
        }
    )


if __name__ == '__main__':
    '''Для дебаггинга'''

    uvicorn.run(app, host="0.0.0.0", port=8000)
