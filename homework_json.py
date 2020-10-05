import json
from homework_top_ten import top_ten_longer_than_six

with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)

words_list = ' '.join([item['description'] for item in json_data['rss']['channel']['items']]).split()
print(*top_ten_longer_than_six(words_list), sep='\n')
