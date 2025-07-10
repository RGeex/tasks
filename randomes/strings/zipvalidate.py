"""
Вам следует написать простую функцию, которая принимает строку в качестве входных данных и
проверяет, является ли она допустимым российским почтовым индексом, возвращая true или false.

Корректный почтовый индекс должен состоять из 6 цифр без пробелов, букв и других символов.
Пустая строка также должна возвращать значение false.

Также имейте в виду, что действительный почтовый индекс не может начинаться с 0, 5, 7, 8 or 9
Примеры

Действительные почтовые индексы:

    198328
    310003
    424000

Неверные почтовые индексы:

    056879
    12А483
    1@63
    111


"""
import re
import typing
import unittest


def zipvalidate(postcode: str) -> bool:
    """
    Проверяет, что введен действующий почтовый индекс.
    """
    return bool(re.compile(r'^(?![05789])\d{6}$').fullmatch(postcode))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(zipvalidate, (
        ('198328', True),
        ('310003', True),
        ('424000', True),
        ('12A483', False),
        ('1@63', False),
        ('111', False),
        ('056879', False),
        ('1111111', False),
    ))
