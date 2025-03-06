"""
В этой кате вам дадут две строки a и b И ваша задача состоит в том, чтобы вернуть персонажей,
которые не распространены в двух струнах.

Например:

solve("xyab","xzca") = "ybzc"
--The first string has 'yb' which is not in the second string.
--The second string has 'zc' which is not in the first string.

Также обратите внимание, что вы возвращаете символы из первой строки, объединенной с символами
из второй строки.
"""
import typing
import unittest


def no_intersections(a: str, b: str) -> str:
    """
    Выводит не перечения двух сток в изначальном порядке.
    """
    return ''.join([x for x in a + b if x not in set(a) & set(b)])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(no_intersections, (
        (("xyab","xzca"),"ybzc"),
        (("xyabb","xzca"),"ybbzc"),
        (("abcd","xyz"),"abcdxyz"),
        (("xxx","xzca"),"zca"),
    ))
