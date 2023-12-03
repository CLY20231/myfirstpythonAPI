## ロカール環境

```
- pip install google-api-python-client
- python ./api/call_youtube_api.py
```

## コンテナでテストする場合
- docker-compose up -d 
- docker exec -it youtube-api bash
- pipenv run call_youtube_api 2

### ブラウザでテストをしたい場合
####  コンテナを起動する
- docker-compose up -d 
#### コンテナを立ち上げて、以下のURLを開いて、テストしてください。
- http://localhost:8000/docs
