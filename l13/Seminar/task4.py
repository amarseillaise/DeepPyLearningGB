# Вспоминаем задачу из семинара l8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от l1 до l7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.


# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от l1 до l7).
# 📌После каждого ввода добавляйте новую информацию в JSON файл.
# 📌Пользователи группируются по уровню доступа.
# 📌Идентификатор пользователя выступает ключём для имени.
# 📌Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
import os
from l12.Home.task1 import NameValidator

PATH_DB = 'user_db.json'


def load_json():
    if os.path.exists(PATH_DB):
        with open(PATH_DB, 'r', encoding='UTF-l8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def input_name():
    return input('Введите имя: ')


def input_id(dict_users: dict):
    list_id = set()
    for users in dict_users.values():
        for user in users:
            for u_id in user:
                list_id.add(u_id)

    while True:
        u_id = input('Введите ID: ')
        if u_id not in list_id and u_id.isdigit():
            return u_id
        print('Такой ID занят, введите заново')


def input_lvl():
    while True:
        lvl = input('Введите уровень доступа: ')
        if lvl.isdigit() and 0 < int(lvl) < 8:
            return lvl


def create_users():
    while True:
        user_db = load_json()
        name = input_name()
        if not name:
            break
        u_id = input_id(user_db)
        lvl = input_lvl()
        if lvl in user_db:
            user_db[lvl].append({u_id: name})
        else:
            user_db[lvl] = [{u_id: name}]
        with open(PATH_DB, 'w', encoding='UTF-l8') as file:
            json.dump(user_db, file, indent=4, ensure_ascii=False)


# create_users()







class User:
    name = NameValidator()

    def __init__(self, name:str, uid: int, access_lvl: int):

        self.name = name
        self.uid = uid
        self.access_lvl = access_lvl

    def __eq__(self, other):
        if isinstance(other, User):
            return self.uid == other.uid

    def __str__(self):
        return f"{self.name}_{self.uid}"

    def __repr__(self):
        return f"{self.name}_{self.uid}"


class UsersDb:
    def __init__(self):
        self.users = []
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.users):
            result = self.users[self.current]
            self.current += 1
            return result
        self.current = 0
        raise StopIteration

    def __str__(self):
        result = "["
        for user in self:
            result += f"{user.name}_{user.uid}, "
        result += ']'
        return result

    def __repr__(self):
        result = "["
        for user in self:
            result += f"{user.name}_{user.uid}, "
        result += ']'
        return result


    def add_user(self, user: User):
        self.users.append(user)


usr1 = User("Namea", 1, 5)
usr2 = User("Nameb", 2, 1)
usr3 = User("Namec", 3, 2)
usr4 = User("Named", 4, 3)

db_usr = UsersDb()
db_usr.add_user(usr1)
db_usr.add_user(usr2)

if usr2 not in db_usr:
    db_usr.add_user(usr2)

for u in db_usr:
    print(u)