from collections import Counter

def top_long_words(word_list, length=6, top=10):
    words_longer_than_six_list = (word for word in word_list if len(word) > length)
    top_ten_words_list = Counter(words_longer_than_six_list).most_common(top)
    return [item[0] for item in top_ten_words_list]
