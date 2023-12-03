import sys
from ast import keyword

from apiclient.discovery import build

'''

'''


def main(arg):
    """
    当日キャンセル可能な情報をDBから削除する。

    Parameters
    ----------
    arg : number
        引数

    Returns
    -------
    response :
        結果
    """
    keyword = 'Python'
    apiKey = "AIzaSyAn-pqU0sHU5kRXsIRjBCdBQjAzzS8hDbE"

    try:
        search_responses = CallAPI(apiKey, keyword, int(arg))
        response_result = GetChanneltitle(search_responses)
        return response_result
    except Exception as e:
        print("error : ", e)


def CallAPI(apiKey, keyword, arg):
    """
    youtubeの検索APIをたたく
    API先: https://www.googleapis.com/youtube/v3/search

    Parameters
    ----------
    apiKey : str
        youtube api をたたくため、利用するapiKey
    keyword : str
        titleを操作するためのkeyword
    arg : number
        数字

    Returns
    -------
    response :
        https://www.googleapis.com/youtube/v3/search の操作結果
    """

    youtube = build('youtube', 'v3', developerKey=apiKey)
    request = youtube.search().list(
        q=keyword,
        part='snippet',
        type='video',
        regionCode="jp",
        maxResults=arg,
    )
    response = request.execute()

    return response


def GetChanneltitle(search_responses):
    """
    出力結果を整理する

    Parameters
    ----------
    search_responses : dict
        youtube api のレスポンス結果

    Returns
    -------
    response :
        チャンネル名、動画タイトルを含めるhashmap
    """
    response = {}

    for search_response in search_responses['items']:
        # snippet
        snippetInfo = search_response['snippet']
        # チャンネル名
        channeltitle = snippetInfo['channelTitle']
        # 動画タイトル
        title = snippetInfo['title']
        # response 結果作成
        if channeltitle in response:
            response[channeltitle].append(title)
        else:
            response[channeltitle] = [title]

    return response


if __name__ == "__main__":
    keyword = sys.argv[1]
    main(keyword)
