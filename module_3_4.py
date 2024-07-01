def single_root_words(root_words, *other_words):
    same_words = []
    root_words = root_words.lower()
    for i in other_words:
        low = i.lower()                             # сравнение слов в нижнем регистре
        if root_words in low or low in root_words:  # Или корневое слово часть или наоборот
            same_words.append(i)                    # Вывод с учётом регистра
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']
