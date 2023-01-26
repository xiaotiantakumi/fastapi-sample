# はじめに

サーバーを起動

```
docker-compose up -d
```

以下にアクセスする
http://localhost/hello-world

{"message":"Hello world5"}
こちらが表示されます。

## ソースの変更

新しいエンドポイントの作成は src 配下で行ってください。
src はディレクトリ共有されているので、ホスト側での変更とコンテナー内での変更が即時反映されます。
例えばホスト側での変更が即時に反映されるかを確認するために、src.py のレスポンスを修正してみて確認してください。

```
 HelloWorld(message="Hello world5")
```

## poetry

pyproject.toml もディレクトリ共有されています。
初回はホスト側の pyproject.toml がコンテナーにコピーされます。(Dockerfile に COPY コマンドを書いているので確認してください。)
サーバーが起動されると、ホストとコンテナの変更がそれぞれに適応されます。
ホスト側の環境を汚さないためには、コンテナの中に入って poetry を使い必要なモジュールを追加してください。

# その他

Docker イメージとコンテナーの操作のチートシートとして使っているだけ。
このリポジトリーに直接関係はない。

## Docker image の作成

イメージの作成

```
docker build -t fastapi-sample -f Dockerfile .
```

イメージの作成でキャッシュを使わないようにするパターン

```
docker build --no-cache -t fastapi-sample -f Dockerfile .
```

起動

```
docker container run -it -d -p 127.0.0.1:8080:80 --name fastapi-sample-container fastapi-sample
```

## イメージに入って確認

イメージからコンテナー起動してそのまま入る

```
docker run -it <image id> /bin/bash
```

起動中のコンテナーに入る

```
docker exec -it <container id> /bin/bash
```

## 削除系

イメージ削除
dangling=true フラグを使用して、タグやリポジトリがないイメージを検索し、それらのイメージ ID を取得し、それらを削除する

```
docker rmi $(docker images -f "dangling=true" -q)
```

コンテナー削除

```
docker container stop fastapi-sample-container
docker container rm fastapi-sample-container
docker rmi fastapi-sample

docker rm -f $(docker ps -a -q)
```

# docker compose

docker-compose down
docker-compose build --no-cache
docker-compose up -d

# 使用していない volumes を削除

```
docker volume prune -f
```
