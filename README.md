![shop_admin_api Workflow](https://github.com/istillmissyou/shop_admin_api/actions/workflows/main.yml/badge.svg)
# API shop admin

## Описание

Апи для интернет магазина аля админ панель

* **/** — главная страница, где выводятся все товары (остальные разделы в разработке)
* **/create_category** — добавить категорию
* **/create_product** — добавить товар
* **/docs** — документация swagger
* **/redoc** — документация redoc

## Описание API запросов

* **GET /api/v1/categories/** — получение всех категорий и их товаров
* **GET /api/v1/categories/category_id/** —  получение категории и её товаров
* **POST /api/v1/categories/** — создание категории
* **PUT /api/v1/categories/category_id/** —  изменение категории
* **DELETE /api/v1/categories/category_id/** —  удаление категории
* **GET /api/v1/products/** — получение всех товаров
* **GET /api/v1/products/product_id/** —  получение товара
* **POST /api/v1/products/** — создание товара
* **PUT /api/v1/products/product_id/** —  изменение товара
* **DELETE /api/v1/products/product_id/** —  удаление товара

## Технологии

* Python 3.10.6
* FastAPI 0.89.1
* SQLAlchemy 2.0.0
* PostgreSQL 15.0

## Подготовительные действия

Склонировать репозиторий

```
git clone https://github.com/istillmissyou/shop_admin_api.git
```

установить Docker

```
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### Шаблон для .env файла

```
POSTGRES_USER=myuser (имя пользователя)
POSTGRES_PASSWORD=1234password (пароль)
POSTGRES_DB=shop_admin_db (название базы)
POSTGRES_SERVER=db (название хоста)
POSTGRES_PORT=5432 (порт)
```

### Как запустить:

Склонировать проект и в терминале перейти в папку "infra"
Далее в командной строке:

``` 
sudo docker compose up --build
```

## Автор
Данил Штунь
