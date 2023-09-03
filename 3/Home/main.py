def task2():
    # Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
    # В результирующем списке не должно быть дубликатов.

    lst = [1, 2, 3, 2, 2, 3, 5, 4, 6, 7, 7, 3, 5]
    result_lst = []
    for x in lst:
        if lst.count(x) > 1 and x not in result_lst:
            result_lst.append(x)
    return result_lst


def task3():
    # В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
    # Не учитывать знаки препинания и регистр символов.
    # За основу возьмите любую статью из википедии или из документации к языку.

    PUNCTUATION_CHARS = ('.', ',', '!', '?', '(', ')', '[', ']', '"', "'")

    path_to_file = "./Text.txt"
    text = ""
    with open(path_to_file, "r", encoding="utf-8") as file:
        text += file.read().lower()

    ranking_words = {}
    for word in text.split():
        if word not in PUNCTUATION_CHARS:
            ranking_words.setdefault(word, 0)
            ranking_words[word] = ranking_words.get(word) + 1

    top_10_words = {}
    for key, value in ranking_words.items():
        top_10_words.setdefault(value, [])
        temp_lst = top_10_words.get(value)
        temp_lst.append(key)
        top_10_words[value] = temp_lst
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    return top_10_words


if __name__ == "__main__":
    # print(task2())
    print(task3())
