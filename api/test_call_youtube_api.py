import call_youtube_api
import pytest

# search_response 情報
search_responses_one = {
    'items': [
        {
            'snippet': {
                'channelTitle': 'channelTitle1',
                'title': 'title1'
            }
        }
    ]
}

search_responses_same_channelTitle = {
    'items': [
        {
            'snippet': {
                'channelTitle': 'channelTitle1',
                'title': 'title1'
            },
        },
        {
            'snippet': {
                'channelTitle': 'channelTitle1',
                'title': 'title2'
            }
        }
    ]
}

search_responses_diff_channelTitle_multiple = {
    'items': [
        {
            'snippet': {
                'channelTitle': 'channelTitle1',
                'title': 'title1'
            },
        },
        {
            'snippet': {
                'channelTitle': 'channelTitle2',
                'title': 'title2'
            },
        },
        {
            'snippet': {
                'channelTitle': 'channelTitle3',
                'title': 'title3'
            }
        }
    ]

}

# result 結果
result_one = {
    'channelTitle1': ['title1']
}

result_search_responses_same_channelTitle = {
    'channelTitle1': ['title1', 'title2']
}

result_search_responses_diff_channelTitle_multiple = {
    'channelTitle1': ['title1'],
    'channelTitle2': ['title2'],
    'channelTitle3': ['title3']
}


@pytest.mark.parametrize('input, excepted', [
    (search_responses_one, result_one),
    (search_responses_same_channelTitle, result_search_responses_same_channelTitle),
    (search_responses_diff_channelTitle_multiple, result_search_responses_diff_channelTitle_multiple)])
def test_GetChanneltitle(input, excepted):
    '''
    search_responses 情報をDict型に変換する処理のテスト
    '''
    actual = call_youtube_api.GetChanneltitle(input)
    assert actual == excepted
