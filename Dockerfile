# CATddのDockerfile
#
# Dockerイメージのビルド
# $ docker build -t catdd .
# Dockerコンテナを起動
# $ docker run --name catdd -id catdd
#
# トラブルシューティング
# 
# 以下のエラーが出た際は「$ docker pull alpine:latest」で解決できるかも
#  => ERROR [internal] load metadata for docker.io/library/alpine:latest
# ------
#  > [internal] load metadata for docker.io/library/alpine:latest:
# ------
# failed to solve with frontend dockerfile.v0: failed to create LLB definition: rpc error: code = Unknown desc = error getting credentials - err: exit status 1, out: ``

# 軽量OSを使用
FROM alpine:latest

# コマンドのインストール
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    yaml \
    yq \
    g++ \
    make \
    cmake \
    git \
    bash \
 && rm -rf /var/cache/apk/*

# Pythonライブラリのインストール
RUN pip3 install \
    openai \
    pyyaml \
    janome

# 作業ディレクトリ構築
WORKDIR /root/CATdd
COPY . /root/CATdd

# ETロボコン2022のリポジトリをクローン
RUN cd /root/CATdd/target_project \
    && git clone https://github.com/KatLab-MiyazakiUniv/etrobocon2022.git \
    && cd etrobocon2022 \
    && git reset --hard 5c01965d978bef7fc319b8612ba8828304ca5c36 \
    && rm module/Motion/*

# COPY bank/motion_module/* target_project/etrobocon2022/module/Motion/
# COPY bank/test/* target_project/etrobocon2022/test/
COPY bank/Atm.* target_project/etrobocon2022/module/

CMD ["/bin/sh"]