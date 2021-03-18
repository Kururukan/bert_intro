# MeCab動作確認用コード
import MeCab


# MeCabを辞書を指定して準備
tagger = MeCab.Tagger("-d /home/username/usr/local/lib/mecab/dic/ipadic -Owakati")
# 形態素解析をしたいテキストを入力
text = "これはMeCab+Neologdの実験です。"
# 形態素解析の実行
wakati = tagger.parse(text)
# 形態素解析結果の表示
print(wakati)
