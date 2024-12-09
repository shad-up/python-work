def single_root_words(root_word,  *other_words):
    same_words = []
    for i in range(len(other_words)):
        low = other_words[i]
        if root_word.casefold() in low.lower() or low.lower() in root_word.casefold():
            same_words.append(other_words[i])
    print(same_words)
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
single_root_words('богатейшая','БЕдная', 'БоГаТ', 'ЧиСтейШая')