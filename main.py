from fastapi import FastAPI

from api import call_youtube_api, schemas

api = FastAPI()


@api.get('/search/{search_number}', response_model=schemas.ResponseInfo)
async def search_number(search_number: str):
    """
    youtube 検索API

    Parameters
    ----------
    info : schemas.RequestInfo
        ユーザから送られてくるリクエスト。中身は検索件数。

    Returns
    -------
    responce : schemas.ResponseInfo
        APIの結果。
    """
    try:
        data = call_youtube_api.main(search_number)
        return schemas.ResponseInfo(result_code=0, data=data)
    except Exception:
        import traceback
        traceback.print_exc()
        return schemas.ResponseInfo(result_code=1, message='there is something wrong')


@api.post('/search', response_model=schemas.ResponseInfo)
async def search(info: schemas.RequestInfo):
    """
    youtube 検索API

    Parameters
    ----------
    info : schemas.RequestInfo
        ユーザから送られてくるリクエスト。中身は検索件数。

    Returns
    -------
    responce : schemas.ResponseInfo
        APIの結果。
    """
    try:
        data = call_youtube_api.main(info.search_number)
        return schemas.ResponseInfo(result_code=0, data=data)
    except Exception:
        import traceback
        traceback.print_exc()
        return schemas.ResponseInfo(result_code=1, message='there is something wrong')
