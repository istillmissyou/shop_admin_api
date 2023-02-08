from fastapi import HTTPException
from requests import head


def exc_404(obj):
    '''Исключение при отсутствие элемента в БД'''
    if obj is None:
        raise HTTPException(
            status_code=404, detail='The object does not exist'
        )


def is_url_image(image_url):
    '''Валидность изображения в ссылке'''
    if image_url is not None:
        image_formats = ('image/png', 'image/jpeg', 'image/jpg', 'image/webp')
        r = head(image_url)
        if r.headers['content-type'] not in image_formats:
            return True
        return False
