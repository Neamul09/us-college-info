import json

with open('enriched_colleges.json', 'r', encoding='utf-8') as f:
    colleges = json.load(f)

print(f"Total colleges: {len(colleges)}")
for i, c in enumerate(colleges, 1):
    print(f"{i:3d}. {c['name']} | {c.get('type')} | USNews: {c.get('us_news_display')} | Need-Blind: {c.get('need_blind_status')}")
