import crud
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services import add_tables, get_db
from sqlalchemy.orm import Session
from routers import categories, products

add_tables()

app = FastAPI(
    title='Store API',
    description='API for the admin panel for the online store',
)

app.include_router(categories.router)
app.include_router(products.router)

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
