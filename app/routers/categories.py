import sys
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import category_crud
from exceptions import exc_404
from schemas import Category, CategoryCreate
from services import get_db

sys.path.append("..")

router = APIRouter(
    prefix='/api/v1/categories',
    tags=['categories'],
)


@router.get('/', response_model=list[Category])
async def get_categories(db: Session = Depends(get_db)):
    '''Получение всех категорий'''

    return await category_crud.get_categories(db)


@router.get('/{category_id}', response_model=list[Category])
async def get_products_by_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    '''Получение товаров определенной категории по id'''

    return await category_crud.get_products_by_category(db, category_id)


@router.post('/', response_model=Category)
async def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
):
    '''Создание категории'''

    return await category_crud.create_category(db, category)


@router.put('/{category_id}', response_model=Category)
async def update_category(
    category_id: int,
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
):
    '''Изменение категории'''

    category = await category_crud.get_category(db, category_id)
    exc_404(category)

    return await category_crud.update_category(db, category_data, category)


@router.delete('/{category_id}', response_model=Category)
async def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    '''Удаление категории'''

    category = await category_crud.get_category(db, category_id)
    exc_404(category)

    return await category_crud.delete_category(db, category_id)
