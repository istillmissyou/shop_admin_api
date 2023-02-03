from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import sys

from exceptions import exc_404
from schemas import Product, ProductCreate
from services import get_db
import crud

sys.path.append("..")

router = APIRouter(
    prefix='/api/products',
    tags=['products'],
)


@router.get(
        '/',
        response_model=list[Product],
)
async def get_products(db: Session = Depends(get_db)):
    return await crud.get_products(db)


@router.get(
        '/{product_id}',
        response_model=Product,
)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = await crud.get_product(db, product_id)
    exc_404(product)

    return product


@router.post(
        '/',
        response_model=Product,
)
async def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return await crud.create_product(db, product)


@router.put(
        '/{product_id}',
        response_model=Product,
)
async def update_product(
    product_id: int,
    product_data: ProductCreate,
    db: Session = Depends(get_db),
):
    product = await crud.get_product(db, product_id)
    exc_404(product)

    return await crud.update_product(db, product_data, product)


@router.delete(
        '/{product_id}',
        response_model=Product,
)
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = await crud.get_product(db, product_id)
    exc_404(product)

    return await crud.delete_product(db, product)
