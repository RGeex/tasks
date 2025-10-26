"""
Проверьте, содержит ли строка одинаковое количество «x» и «o».
Метод должен возвращать логическое значение и не учитывать регистр.
Строка может содержать любой символ.
"""
import typing
import unittest
from operator import eq


def xo(s: str) -> bool:
    """Поиск в строке 'x' и 'o', сравнение их колличеств."""
    return eq(*[s.lower().count(i) for i in 'xo'])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(xo, (
        ("", True),
        ("ooxx", True),
        ("oxOx", True),
        ("zzoo", False),
        ("ooxXm", True),
        ("xooxx", False),
        ("zpzpzpp", True),
    ))
