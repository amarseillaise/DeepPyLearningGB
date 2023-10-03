# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class AnimalFactory:

    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "Cat":
            return Cat(**kwargs)
        elif animal_type == "Dog":
            return Dog(**kwargs)
        elif animal_type == "Bird":
            return Bird(**kwargs)
        else:
            raise ValueError("Unsupported animal type: " + animal_type)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Meow! I'm {self.name} and I'm {self.age} years old.")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Woof! I'm {self.name} and I'm {self.age} years old.")


class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Chirick chirick! I'm {self.name} and I'm {self.age} years old.")


animal_type = "Cat"
parameters = {"name": "Tom", "age": 5}

animal = AnimalFactory.create_animal(animal_type, **parameters)
animal.speak()
