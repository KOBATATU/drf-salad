# Pythonのイメージ
FROM python:3.9

# 作業ディレクトリを設定する
WORKDIR /work

# 必要なパッケージをインストールする
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080