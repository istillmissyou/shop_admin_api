from pydantic import BaseModel, HttpUrl, validator


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
    name: str
    price: int
    count: int
    category_id: int
    image_url: HttpUrl | None = None

    @validator('price', 'count')
    def check_positive_number(cls, v):
        '''
        Валидация на положительное число цены и количества товара
        '''
        if v < 0:
            raise ValueError('Цена и количество не могут быть отрицательными')
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
