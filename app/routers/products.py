import sys
from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from crud import product_crud
from exceptions import exc_404
from schemas import Product, ProductCreate
from services import get_db, write_notification

sys.path.append("..")

router = APIRouter(
    prefix='/api/v1/products',
    tags=['products'],
)


@router.get('/', response_model=list[Product])
async def get_products(db: Session = Depends(get_db)):
    '''Получение всех товаров'''

    return await product_crud.get_products(db)


@router.get('/{product_id}', response_model=Product)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    '''Получение определенного товара по id'''

    product = await product_crud.get_product(db, product_id)
    exc_404(product)

    return product


@router.post('/', response_model=Product)
async def create_product(
    background_tasks: BackgroundTasks,
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    '''Создание товара с фоновой задачей'''

    product = await product_crud.create_product(db, product)
    background_tasks.add_task(write_notification, product.name)
    return product


@router.put('/{product_id}', response_model=Product)
async def update_product(
    product_id: int,
    product_data: ProductCreate,
    db: Session = Depends(get_db),
):
    '''Изменение товара'''

    product = await product_crud.get_product(db, product_id)
    exc_404(product)

    return await product_crud.update_product(db, product_data, product)


@router.delete('/{product_id}', response_model=Product)
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    '''Удаление товара'''

    product = await product_crud.get_product(db, product_id)
    exc_404(product)

    return await product_crud.delete_product(db, product)
