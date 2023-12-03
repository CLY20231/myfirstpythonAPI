from typing import Optional

from pydantic import BaseModel, Field


# リクエスト
class RequestInfo(BaseModel):
    """
    検索情報
    """
    search_number: str = Field(
        title="入力数字",
        description='''
            操作件数
        ''',
        example="5"
    )


# レスポンス
class ResponseInfo(BaseModel):
    result_code: str = Field(
        None,
        title="操作結果",
        description="0:成功 1:失敗"
    )
    message: Optional[str] = Field(
        None,
        title="メッセージ",
        description="登録失敗時のメッセージ"
    )
    data: Optional[dict] = Field(
        None,
        title="検索詳細",
        description="youtubeで[python]がキーワードとして、検索した結果"
    )
