from pydantic import BaseModel, Field, HttpUrl, validator
from requests import head


class ProductBase(BaseModel):
    '''
    Модель товара

    **Параметры**

    * `name`: наименование
    * `price`: цена(стоимость)
    * `count`: количество
    * `category_id`: id категории
    * `image_url`: ссылка на изображение
    '''
    name: str = Field(example='Xiaomi 25 Turbo')
    price: int = Field(example=999)
    count: int = Field(example=55)
    category_id: int = Field(example=2)
    image_url: HttpUrl | None = Field(
        default=None, example='https://img.com/example.png'
    )

    @validator('price', 'count')
    def check_positive_number(cls, v):
        '''
        Валидация на положительное число цены и количества товара
        '''
        if v < 0:
            raise ValueError('Цена и количество не могут быть отрицательными')
        return v

    @validator('image_url')
    def without_image(cls, v):
        '''Если нет изображения ставит заглушку'''
        if v is None:
            return 'https://p2payer.com/images/profile_nophoto.jpg'
        return v


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass


class CategoryBase(BaseModel):
    name: str


class Category(CategoryBase):
    id: int
    products: list[Product] = []  # список продуктов категории

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    pass
