# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
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
from l12.Home.task1 import UserNameError

PATH_DB = 'user_db.json'


class User:
    name = NameValidator()

    def __init__(self, name: str, uid: int, access_lvl: int):
        self.name = name
        self.uid = uid
        self.access_lvl = access_lvl

    def __eq__(self, other):
        other_uid = None
        if isinstance(other, int):
            other_uid = other
        elif isinstance(other, User):
            other_uid = other.uid
        return self.uid == other_uid

    def __str__(self):
        return f"{self.name}_{self.uid}"

    def __repr__(self):
        return f"{self.name}_{self.uid}"


class UsersDb:
    def __init__(self):
        self.users = []
        if os.path.exists(PATH_DB):
            with open(PATH_DB, 'r', encoding='UTF-8') as file:
                self.temp_json_dump = json.load(file, parse_int=int)
        else:
            self.temp_json_dump = {str(k): {} for k in range(1, 8)}

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < len(self.users):
            result = self.users[self.current]
            self.current += 1
            return result
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
        selected_lst: dict = self.temp_json_dump[str(user.access_lvl)]
        selected_lst[str(user.uid)] = user.name
        self.__dump_to_json()

    def __create_users_from_json(self, path):
        if os.path.exists(path):
            with open(path, 'r', encoding='UTF-8') as file:
                self.temp_json_dump = json.load(file, parse_int=int)
                for acc_lvl, usr_lst in self.temp_json_dump.items():
                    for uid, name in usr_lst.items():
                        self.add_user(User(name, int(uid), int(acc_lvl)))

    def create_users(self):
        self.__create_users_from_json(PATH_DB)
        while True:
            name = input('Введите имя: ')
            if not name:
                self.__dump_to_json()
                break
            lvl = self.input_lvl()
            uid = self.input_id()
            if uid not in self.users:
                try:
                    new_user = User(name, uid, lvl)
                except UserNameError as e:
                    print(e)
                    continue
                self.add_user(new_user)
                self.__dump_to_json()
            else:
                print("Такой ID уже занят")

    def __dump_to_json(self):
        with open(PATH_DB, 'w', encoding='UTF-8') as file:
            json.dump(self.temp_json_dump, file, indent=4, ensure_ascii=False)

    def input_id(self):
        list_id = (u.uid for u in self.users)
        while True:
            uid = input('Введите ID: ')
            if uid not in list_id and uid.isdigit():
                return uid
            print('Такой ID занят, введите заново')

    @staticmethod
    def input_lvl():
        while True:
            lvl = input('Введите уровень доступа: ')
            if lvl.isdigit() and 0 < int(lvl) < 8:
                return lvl
            else:
                print("Уровень доступа должен быть от 1 до 7")


# usr1 = User("Namea", 1, 5)
# usr2 = User("Nameb", 2, 1)
# usr3 = User("Namec", 3, 2)
# usr4 = User("Named", 4, 3)
#
# db_usr = UsersDb()
# db_usr.add_user(usr1)
# db_usr.add_user(usr2)
# db_usr.add_user(usr4)
#
# db_usr.create_users()
