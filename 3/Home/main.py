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

    PUNCTUATION_CHARS = ('.', ',', '!', '?', '(', ')', '[', ']', '"', "'", '-', '—')
    result = ""

    # Записываем текс из файла в переменную
    path_to_file = "./Text.txt"
    text = ""
    with open(path_to_file, "r", encoding="utf-8") as file:
        text += file.read().lower()

    # Формируем словарь в формате: {слово: количество повторений}
    ranking_words = {}
    for word in text.split():
        if word not in PUNCTUATION_CHARS:
            ranking_words.setdefault(word, 0)
            ranking_words[word] = ranking_words.get(word) + 1

    # Переформируем словарь в обратный формат: {количество вхождений: слово}
    top_10_words = {}
    for key, value in ranking_words.items():
        top_10_words.setdefault(value, [])
        temp_lst = top_10_words.get(value)
        temp_lst.append(key)
        top_10_words[value] = temp_lst
    includes_keys_list = sorted(list(top_10_words.keys()), reverse=True)  # Получаем список отсортированных ключей

    # формируем текст для вывода
    for i in range(10):
        place = top_10_words.get(includes_keys_list[i])
        result += f"На месте {i + 1} находятся слова {place}, которые встречаются {includes_keys_list[i]} раз\n"

    return result


def task4(weight):
    # Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
    # Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
    # Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

    items = []
    act_mass = 0
    backpack = {
        "Спички": 10,
        "Тушёнка": 15,
        "Селёдка": 7,
        "Мини-палатка": 25,
        "Стулья": 11,
        "Кирпичи": 4,
        "Игральные карты": 51,
        "Изотопы": 2,
    }
    for key, value in backpack.items():
        if act_mass > weight or act_mass + value > weight:
            continue
        items.append(key)
        act_mass += value

    return f"При массе {act_mass} в рюкзак поместились следующие вещи: \n{items}"


if __name__ == "__main__":
    print(task2())
    print(task3())
    print(task4(40))
