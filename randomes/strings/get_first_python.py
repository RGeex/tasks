"""
Вам будет предоставлен массив объектов (ассоциативные массивы в PHP),
представляющий данные о разработчиках, зарегистрировавшихся на следующую
организованную вами встречу по программированию. Список отсортирован по
времени регистрации.

Ваша задача — вернуть одну из следующих строк:

    < firstName here >, < country here >первого разработчика Python,
    который зарегистрировался; или
    There will be no Python developersесли ни один разработчик Python
    не зарегистрировался.

Например, дан следующий входной массив:

list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]

ваша функция должна возвращать Victoria, Puerto Rico.

Примечания:

    Входной массив всегда будет допустимым и отформатированным, как в примере выше.
"""
import typing
import unittest


def get_first_python(users: list[dict]) -> str:
    """
    Получает первого в списке разработчика python.
    """
    return next((f'{x["first_name"]}, {x["country"]}' for x in users if x["language"] == "Python"), 'There will be no Python developers')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase( type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_first_python, (
        ([
            { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
            { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
            { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
        ], "Victoria, Puerto Rico"),
        ([
            { "first_name": "Kseniya", "last_name": "T.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript" },
            { "first_name": "Amar", "last_name": "V.", "country": "Bosnia and Herzegovina", "continent": "Europe", "age": 32, "language": "Ruby" }
        ], "There will be no Python developers"),
    ))
