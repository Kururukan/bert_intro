from transformers import BertTokenizer, BertJapaneseTokenizer, AutoModelForSequenceClassification, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment')
model = BertModel.from_pretrained('bert-base-uncased')