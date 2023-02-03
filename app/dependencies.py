from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header()):
    if x_token != 'famsdfkasmfoo2ei1d9x2exj29':
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(x_key: str = Header()):
    if x_key != 'skdjfaoirj93jx9ax93':
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key
