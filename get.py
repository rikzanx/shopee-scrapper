import json

with open('Shopee_219835045.json') as f:
  data = json.load(f)

length = len(data['items'])
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(length)

for item in data['items']:
    print(item['price_max'])