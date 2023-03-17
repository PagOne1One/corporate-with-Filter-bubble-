import json

# JSONファイルの読み込み
with open('chrome_history.json', 'r') as f:
    data = json.load(f)

# 訪問回数とURLの抽出
result = []
for item in data:
    result.append({
        'visit_count': item['visit_count'],
        'url': item['url']
    })

# 結果の出力
print(result)
