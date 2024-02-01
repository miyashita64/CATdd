# CATdd
テスト駆動開発の支援を目的としたフレームワーク

## 各種バージョン(記載時点 2023.11.24)
- Pyenv  2.3.32
- Python 3.10.13
- Poetry 1.7.1

## 環境構築
1. pyenvのインストール
依存関係のインストール
```
sudo apt update
sudo apt upgrade
sudo apt install libssl-dev libffi-dev libncurses5-dev zlib1g zlib1g-dev libreadline-dev libbz2-dev libsqlite3-dev make gcc cmake build-essential
curl https://pyenv.run | bash
```

パスを通す(.bashrcなどに追記)
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
pyenv --version
```
pyenvのバージョンが表示されていればOK

2. Pythonをバージョン指定でインストールする
```
pyenv install 3.10.13
pyenv versions
```
3.10.13がリスト内に表示されていればOK

ローカルのPythonのバージョンを指定する
```
pyenv local 3.10.13
python3 --version
```
Pythonのバージョンが3.10.13と表示されればOK

3. Poetryのインストール
```
curl -sSL https://install.python-poetry.org | python3 -
# !!poetryのインストール完了時にパスを通すようにメッセージが表示されるので従うこと!!
export PATH="この部分はメッセージに従う:$PATH"
poetry --version
```
Poetryのバージョンが表示されていればOK

4. OpenAI APIキーの取得と設定
↓あたりでAPIキーを取得できる
https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key

環境変数に`OPENAI_API_KEY`を設定する
```
echo "export OPENAI_API_KEY=取得したOpenAI APIキー" >> ~/.bashrc
```

## CATddのセットアップ
1. 必要なパッケージをインストールする
```
poetry install
```

2. catddコマンドの有効化(.bashrcとかに書くと永続化できるよ)
```
source .env
```