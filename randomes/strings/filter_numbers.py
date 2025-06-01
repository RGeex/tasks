"""
Неудачный фильтр — исправление ошибки №3

О нет, фильтр Тимми, похоже, не работает? Ваша задача — исправить функцию Фильтра чисел,
чтобы удалить все числа из строки.

def filter_numbers(string):
    return "".join(x for x in string if int(x))
"""
import typing
import unittest


def filter_numbers(string: str) -> str:
    """
    Удаяляет все цифра в строке.
    """
    return "".join(x for x in string if not x.isdigit())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(filter_numbers, (
        ("test123", 'test'),
        ("a1b2c3", 'abc'),
        ("aa1bb2cc3dd", 'aabbccdd'),
        ("CodeWars", 'CodeWars'),
        ("99234", ''),
    ))
