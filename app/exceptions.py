from fastapi import HTTPException


def exc_404(obj):
    '''Исключение при отсутствие элемента в БД'''
    if obj is None:
        raise HTTPException(
            status_code=404, detail=f'The {obj} does not exist'
        )
