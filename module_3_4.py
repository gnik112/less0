
def single_root_words(root_word, *other_words):
    same_words = []
    word1 = root_word.lower()
    for word in other_words:
        word2 = word.lower()
        if word1.find(word2) >= 0 or word2.find(word1) >= 0:
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)