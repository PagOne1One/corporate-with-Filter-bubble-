import json
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

# 生成されたJSONファイルを読み込む
with open('search_history.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# URLのみを抽出して、テキストデータを作成する
text_data = []
for item in data:
    text_data.append(item['url'])

# テキストデータを前処理して、単語に分割する
preprocessed_data = [simple_preprocess(text) for text in text_data]

# Word2Vecによる単語埋め込みを行う
model = Word2Vec(preprocessed_data, size=100, window=5, min_count=1, workers=4)

# 単語のベクトルを取得する
vector = model.wv['単語']
