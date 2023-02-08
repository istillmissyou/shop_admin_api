from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Store API'
    app_description: str = 'API for the admin panel for the online store'
    app_version: str = '0.1.9'
    terms_of_service: str = ('https://github.com/istillmissyou/'
                             'shop_admin_api/blob/main/LICENSE')
    contact: dict = {
        "name": "Данил Штунь",
        "url": "https://github.com/istillmissyou",
        "email": "danilshtun@yandex.ru",
    }
    license_info: dict = {
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_server: str
    postgres_port: int

    class Config:
        env_file = '.env'


settings = Settings()
