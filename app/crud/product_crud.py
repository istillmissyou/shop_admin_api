import sys
from typing import TYPE_CHECKING, List

import models
import schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

sys.path.append("..")


async def get_products(db: 'Session') -> List[schemas.Product]:
    '''Получение всех товаров'''
    products = db.query(models.Product).all()
    return list(map(schemas.Product.from_orm, products))


async def get_product(db: 'Session', product_id: int):
    '''Получение определенного товара по id'''
    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()


async def create_product(
    db: 'Session',
    product: schemas.ProductCreate,
) -> schemas.Product:
    '''Создание товара'''
    product = models.Product(**product.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return schemas.Product.from_orm(product)


async def update_product(
    db: 'Session',
    product_data: schemas.ProductCreate,
    product: models.Product,
) -> schemas.Product:
    '''Изменение товара'''
    product.name = product_data.name
    product.price = product_data.price
    product.count = product_data.count
    product.image_url = product_data.image_url

    db.commit()
    db.refresh(product)

    return schemas.Product.from_orm(product)


async def delete_product(db: 'Session', product: models.Product):
    '''Удаление товара'''
    db.delete(product)
    db.commit()
    return product
