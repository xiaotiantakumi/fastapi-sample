FROM python:3.10-slim AS builder
LABEL version="0.1"
LABEL description="api server"

# Poetryのインストール先を指定する環境変数.
ENV POETRY_HOME="/opt/poetry"
# Poetryの設定で、仮想環境を作成するかどうかを指定する環境変数.falseを指定(Dockerなので)
ENV POETRY_VIRTUALENVS_CREATE=false
# pipの設定で、キャッシュを使用するかどうかを指定する環境変数。
ENV PIP_NO_CACHE_DIR=off
# pipの設定で、pipのバージョンチェックを行うかどうかを指定する環境変数.
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
# pipの設定で、タイムアウト時間を指定する環境変数
ENV PIP_DEFAULT_TIMEOUT=100
# pythonのセットアップ先を指定する環境変数
ENV PYSETUP_PATH="/opt/pysetup"
# poetryがインストールされた場所を追加しています。これにより、Dockerイメージ内でpoetryを使用できるようになります。
ENV PATH="$POETRY_HOME/bin:$PATH"

# システムのパッケージリストを更新します。これにより、イメージのビルド時に最新のパッケージを使用できるようになります。
#  --no-install-recommends オプションは、依存関係としてインストールされるが必要ではないパッケージをインストールしないようにします。-yオプションは、インストール時に確認を求めないようにします。
# apt clean: システムから不要なパッケージを削除します。これにより、Dockerイメージのサイズを小さくできます
RUN apt update && \
    apt install --no-install-recommends -y curl && \
    apt clean

# poetryのインストール
RUN curl --ssl https://install.python-poetry.org | python3

# packages install
RUN mkdir -p /app/src
# pyproject.tomlはapp配下に配置しておく。
WORKDIR /app
# イメージ作成時にpyproject.tomlがないのでコピーしておく。
COPY pyproject.toml /app/
# 「--only main」オプションは、「pyproject.toml」に記述されている「[tool.poetry.dependencies]」セクションにのみ依存関係をインストールします。
RUN poetry install --only main

# src配下でpoetryを実行したいので移動しておく
WORKDIR /app/src

# Docker イメージが実行されるときにホスト側に公開するポート番号を指定します。
# これにより、Docker コンテナが起動した際に、外部からアクセスできるようになります。こ80番ポートが公開されます。
EXPOSE 80
# uvicornで--reloadすることによりアプリケーションの変更がホットリロードされるようになる
CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80","--reload"]