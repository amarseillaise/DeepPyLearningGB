# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
#
# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
#
#
# Математика,Физика,История,Литература
# Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:
#
# __init__(self, name, subjects_file): конструктор класса, принимающий ФИО студента и имя файла с данными о предметах и оценках.
#
# add_subject(self, subject, grade, test_score): метод для добавления информации о предмете, оценке и результате теста.
#
# get_average_grade(self): метод, возвращающий средний балл студента по всем предметам.
#
# get_subjects(self): метод, возвращающий список всех предметов, по которым есть информация у студента.
#
# Реализовать функцию get_average_grades(students),
# которая принимает список студентов и выводит информацию о средних баллах для каждого студента.
#
# Реализовать функцию get_subject_average(students, subject),
# которая принимает список студентов и название предмета,
# и выводит информацию о среднем балле по этому предмету для каждого студента.
#
# Реализовать функцию get_top_student(students, subject), которая принимает список студентов и название предмета,
# и выводит информацию о студенте с наивысшим средним баллом по этому предмету.

import csv
import os
import re


class Descriptor:
    def __init__(self, min_value=0, max_value=0, score_kind=None):
        self.min_value = min_value
        self.max_value = max_value
        self.score_kind = score_kind

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


    def validate(self, value):
        if re.fullmatch(r"[A-ZА-Я][A-ZА-Яa-zа-я\s]+", value):
            return True



class Student:
    name = Descriptor()

    def __init__(self, name: str, subjects_file: str):
        self.name: str = name
        self._disciplines: dict = self.__get_disciplines(subjects_file)

    def __str__(self):
        return f"Студент: {self.name}"

    @staticmethod
    def __get_disciplines(subjects_file):
        if subjects_file in os.listdir():
            with open(subjects_file, "r", encoding="UTF-8") as f:
                dump = csv.reader(f, delimiter=',')
                for line in dump:
                    result = line
            return {k: {"grade": [], "test_score": []} for k in result}

    @staticmethod
    def __add_score_and_grade(kind):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                kind_of_score = self._disciplines[args[0]]
                kind_of_score[kind].append(args[1])
                return func(self, *args, **kwargs)

            return wrapper

        return decorator

    @staticmethod
    def __get_avg_score_and_grade(kind):
        def decorator(func):
            def wrapper(self, discipline=None):
                lst = []
                for disc in self._disciplines.items():
                    if disc[1].get(kind):
                        if discipline:
                            if disc[0] == discipline:
                                lst.append(sum(disc[1].get(kind)) / len(disc[1].get(kind)))
                        else:
                            lst.append(sum(disc[1].get(kind)) / len(disc[1].get(kind)))
                return sum(lst) / len(lst)

            return wrapper

        return decorator

    @__add_score_and_grade("grade")
    def add_grade(self, discipline, score):
        if not isinstance(score, int) or not (1 < score < 6):
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        pass

    @__add_score_and_grade("test_score")
    def add_test_score(self, discipline, score):
        if not isinstance(score, int) or not (0 < score < 100):
            raise ValueError("Оценка должна быть целым числом от 1 до 100")
        pass

    @__get_avg_score_and_grade("grade")
    def get_average_grade(self, discipline=None):
        pass

    @__get_avg_score_and_grade("test_score")
    def get_average_test_score(self, discipline=None):
        pass

    def get_subjects(self):
        lst = []
        for disc in self._disciplines.items():
            if disc[1].get("grade") or disc[1].get("test_score"):
                lst.append(disc[0])
        return lst


def get_average_grades(students: list[Student]):
    return [(student.name, student.get_average_grade(), student.get_average_test_score()) for student in students]

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
