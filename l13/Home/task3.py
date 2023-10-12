# В организации есть два типа людей: сотрудники и обычные люди.
# Каждый человек(и сотрудник, и обычный) имеет следующие атрибуты:
#
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая)
# Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.
#
# Ваша задача:
#
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
# (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных
# и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
#
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на l1 год.
#
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID
# (по остатку от деления на l7).
#
# Создать несколько объектов класса Person и Employee с разными данными и проверить,
# что исключения работают корректно при передаче неверных данных.

import re


class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Validator:

    def __init__(self, kind):
        self.kind = kind

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.kind == "name":
            if not (isinstance(value, str) and re.fullmatch(r"[A-Za-zА-Яа-я-]+", value)):
                raise InvalidNameError(f"Invalid name: {value}. Name should be a non-empty string.")
        elif self.kind == "age":
            if not (isinstance(value, int) and value > 0):
                raise InvalidAgeError(f"Invalid age: {value}. Age should be a positive integer.")
        elif self.kind == "pid":
            if not (isinstance(value, int) and (99999 < value < 1000000 or value == -1)):
                raise InvalidIdError(f"Invalid id: {value}."
                                     f" Id should be a 6-digit positive integer between 100000 and 999999.")
        setattr(instance, self.param_name, value)


class Person:
    firstname = Validator("name")
    second_name = Validator("name")
    lastname = Validator("name")
    age = Validator("age")
    pid = Validator("pid")

    def __init__(self, firstname, second_name, lastname, age):
        self.firstname = firstname
        self.second_name = second_name
        self.lastname = lastname
        self.age = age
        self.pid = -1

    def birthday(self):
        self.age += 1
        return self.age

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, firstname, second_name, lastname, age, pid):
        super().__init__(firstname, second_name, lastname, age)
        self.pid = pid

    def get_level(self):
        return sum(self.pid) % 7


person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())
