"""
Помогите Джонни!
Он не может заставить свой код работать!
Простой код

Джонни пытается создать функцию, которая кодирует две строки в ASCII-коды и
суммирует их, но не может найти ошибку в коде! Помогите ему!

def add(s1, s2):
    s1 = s1.encode()
    s2 = s2.encode()
    s1 = sum(s1)
    s2 = sum(s1)
    return s1+s2
"""
import typing
import unittest


def add(s1: str, s2: str) -> str:
    """
    Вычисляет сумму символов в ASCII двух переданных строк.
    """
    return sum(map(ord, s1 + s2))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(add, (
        (('a', 'b'), 195),
        (('aa', 'bb'), 390),
    ))
