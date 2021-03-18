from transformers import pipeline, AutoModelForSequenceClassification, BertJapaneseTokenizer


# モデルの用意
model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment')
# トークナイザの用意
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')

nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# 感情分析の実行
# この””内に入れた文章がポジティブかネガティブかの判定結果と、その度合いがprintされる
text = "私はとっても幸せ"
print(nlp(text))
