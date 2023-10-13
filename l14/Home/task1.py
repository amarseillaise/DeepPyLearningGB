# 📌 На семинаре l13 был создан проект по работе с пользователями (имя, id, уровень)
# 📌 Напишите l3-l7 тестов pytest (или unittest на ваш выбор) для данного проекта
# 📌 ОБЯЗАТЕЛЬНО! Используйте фикстуры

import pytest
from l13.Seminar.task4 import *


@pytest.fixture
def user_data():
    return {
        'name': 'John',
        'uid': 1,
        'access_lvl': 3
    }


@pytest.fixture
def user(user_data):
    return User(**user_data)


@pytest.fixture
def users_db():
    return UsersDb()


def test_user_initialization(user, user_data):
    assert user.name == user_data['name']
    assert user.uid == user_data['uid']
    assert user.access_lvl == user_data['access_lvl']


def test_user_equality(user):
    assert user == user.uid


def test_user_string_representation(user):
    expected_result = f"{user.name}_{user.uid}"

    assert str(user) == expected_result
    assert user.__str__() == expected_result


def test_user_db_initialization(users_db):
    assert len(users_db.users) == 0
    assert users_db.temp_json_dump == {str(k): {} for k in range(1, 8)}

