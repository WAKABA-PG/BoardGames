# BoardGames
Pythonによるボードゲーム

## 環境構築
### Pythonをインストールする（versionは任意）

### pygame(ライブラリ)をインストール
```
 pip install pygame
```

### pygbag(ライブラリ)をインストール
Python(pygame)からWBBページに変換するために必要
```
 pip install pygame
```
### kivy(ライブラリ)をインストール
※これは実施しなくてもOK
```
 pip install kivy
```

## pygame → WEBページへのビルド方法
### ファイル名を編集
pygameで作成したXXXX.pyファイル名を「main.py」に変更する

### ビルド用フォルダを作成する
フォルダを任意の名前、場所に作成し、上記main.pyを配置する

### main.pyの中身を編集
最初に以下を追記
```
import asyncio
```

main関数を宣言を以下のように修正
```
async def main():
```

「pygame.display.update()」のすぐに後に以下を追記する
```
pygame.display.update()
##これの下に以下を追記

await asyncio.sleep(0)
```

mainの呼びだしを以下のように修正
```
asyncio.run(main())
```
### ビルド実施
上記でmain.pyを配置したフォルダの1つ上の階層へcdで移動する。  
以下のコマンドを実行  
```
pygbag [フォルダ名]
```

### 実行確認
以下へアクセスして確認する  
※ローカルホストだとエラーになることある

http://localhost:8000/


### デプロイ
上記フォルダに作成された「\build\web」フォルダをそのままサーバへ配置する。


## サンプルゲーム
https://wakabaclass.com/wp-content/uploads/2023/11/web/index.html  
https://wakabaclass.com/wp-content/uploads/2023/11/web2/index.html 

