import json
from homework_top_words
import top_long_words

with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)

words_list = ' '.join([item['description'] for item in json_data['rss']['channel']['items']]).split()
print(*top_long_words(words_list, 6, 10), sep='\n')
