import sys
from typing import TYPE_CHECKING, List

import models
import schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

sys.path.append("..")


async def get_categories(db: 'Session'):
    '''Получение всех категорий'''
    return db.query(models.Category).all()


async def get_category(db: 'Session', category_id: int):
    '''Получение определенной категории по id'''
    return db.query(models.Category).filter(
        models.Category.id == category_id
    ).first()


async def get_products_by_category(
    db: 'Session',
    category_id: int,
) -> List[schemas.Product]:
    '''Получение товаров определенной категории по id'''
    products = db.query(models.Product).filter(
        models.Category.id == category_id
    )
    return list(map(schemas.Product.from_orm, products))


async def create_category(db: 'Session', category: schemas.CategoryCreate):
    '''Создание категории'''
    category = models.Category(**category.dict())
    db.add(category)
    db.commit()
    db.refresh(category)
    return schemas.Category.from_orm(category)


async def update_category(
    db: 'Session',
    category_data: schemas.CategoryCreate,
    category: models.Category,
) -> schemas.Category:
    '''Изменение категории'''
    category.name = category_data.name

    db.commit()
    db.refresh(category)

    return schemas.Category.from_orm(category)


async def delete_category(db: 'Session', category_id: int):
    '''Удаление категории'''
    category = db.query(models.Category).filter(
        models.Category.id == category_id
    ).first()
    db.delete(category)
    db.commit()
    return category
