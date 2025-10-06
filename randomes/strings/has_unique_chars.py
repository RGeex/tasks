"""
Напишите программу, которая определяет, содержит ли строка только уникальные символы. Возвращает true, если это так, и false в противном случае.

Строка может содержать любой из 128 символов ASCII. Символы чувствительны к регистру, например, «a» и «A» считаются разными символами.

"""
import typing
import unittest


def has_unique_chars(string: str) -> bool:
    """
    Определяет, содержил ли строка только уникальные символы.
    """
    return len(string) == len(set(string))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(has_unique_chars, (
        ("abcdef", True),
        ("++-", False),
        ("  nAa", False),
    ))
