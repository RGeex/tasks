"""
Вам будет предоставлен массив объектов (ассоциативные массивы в PHP, таблицы в COBOL),
представляющих данные о разработчиках, которые зарегистрировались для участия в следующей
встрече по программированию, которую вы организуете.

Ваша задача — вернуть массив, в котором каждый объект будет иметь новое свойство «приветствие»
со следующим строковым значением:

Привет <имя здесь>, что вам больше всего нравится в <язык здесь>?

Например, дан следующий входной массив:

list1 = [
  { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
  { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' } 
]

Ваша функция должна возвращать следующий массив:

[
  { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java',
    'greeting': 'Hi Sofia, what do you like the most about Java?'
  },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python',
    'greeting': 'Hi Lukas, what do you like the most about Python?'
  },
  { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby',
    'greeting': 'Hi Madison, what do you like the most about Ruby?'
  } 
]
Примечания:

    Порядок свойств в объектах не имеет значения (за исключением COBOL).
    Входной массив всегда будет допустимым и отформатированным, как в примере выше. 
"""
import typing
import unittest


def greet_developers(lst: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Добавляет в список разработчиков приветственную строку.
    """
    for x in lst:
        x['greeting'] = f"Hi {x['firstName']}, what do you like the most about {x['language']}?"
    return lst


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':

    test(greet_developers, (
        ([
            { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
            { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
            { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' } 
        ],
        [
            { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java',
            'greeting': 'Hi Sofia, what do you like the most about Java?'
            },
            { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python',
            'greeting': 'Hi Lukas, what do you like the most about Python?'
            },
            { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby',
            'greeting': 'Hi Madison, what do you like the most about Ruby?'
            } 
        ]),
    ))
