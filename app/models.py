from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Category(Base):
    '''
    Модель категории

    **Параметры**

    * `name`: наименование
    * `products`: One-to-Many
    '''
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    products = relationship('Product', back_populates='category')


class Product(Base):
    '''
    Модель товара

    **Параметры**

    * `name`: наименование
    * `price`: цена(стоимость)
    * `count`: количество
    * `category_id`: id категории
    * `category`: One-to-Many
    * `image_url`: ссылка на изображение
    '''
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    price = Column(Integer, index=True)
    count = Column(Integer, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')
    image_url = Column(String, index=True)
