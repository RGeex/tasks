"""
Задача

Удалите все восклицательные знаки с конца слов. Слова разделяются одним пробелом.
Внутри слова нет восклицательных знаков.
Примеры

remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi Hi"
remove("!!!Hi !!hi!!! !hi") === "!!!Hi !!hi !hi"
"""
import re
import typing
import unittest


def remove(st: str) -> str:
    """
    Удаляет восклицательные знаки с конца слов в предложении.
    """
    return re.sub(r'\b!+', '', st)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove, (
        ('Hi!', 'Hi'),
        ('Hi!!!', 'Hi'),
        ('!Hi', '!Hi'),
        ('!Hi!', '!Hi'),
        ('Hi! Hi!', 'Hi Hi'),
        ('!!!Hi !!hi!!! !hi', '!!!Hi !!hi !hi'),
    ))
