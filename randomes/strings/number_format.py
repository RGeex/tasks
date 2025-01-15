"""
Отформатируйте любое целое число в строку с помощью «,» (запятых) в правильных местах.

Пример:

For n = 100000 the function should return '100,000';
For n = 5678545 the function should return '5,678,545';
for n = -420902 the function should return '-420,902'.
"""
import typing
import unittest


def number_format(n: int) -> str:
    """
    Форматирует число в формат разделенный запятыми.
    """
    return f'{n:,}'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(number_format, (
        (100000, "100,000"),
        (5678545, "5,678,545"),
        (-420902, "-420,902"),
        (-3, "-3"),
        (-1003, "-1,003"),
    ))
