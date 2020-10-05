from collections import Counter

def top_ten_longer_than_six(word_list):
    words_longer_than_six_list = (word for word in word_list if len(word) > 6)
    top_ten_words_list = Counter(words_longer_than_six_list).most_common(10)
    return [item[0] for item in top_ten_words_list]
