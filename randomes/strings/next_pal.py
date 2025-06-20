"""
В этом ката вам будет дано положительное целое число, val и вам нужно создать функцию
next_pal()( nextPalJavascript), который выведет наименьшее число-палиндром, превышающее val.

Давайте посмотрим:

For Python
next_pal(11) == 22

next_pal(188) == 191

next_pal(191) == 202

next_pal(2541) == 2552

Вы получите значения выше 10, все они действительны.

Наслаждайся этим!!
"""
import typing
import unittest


def next_pal(val: int) -> int:
    """
    Поиск следующего числа палиндрома.
    """
    while (x:= str(val + 1)) != x[::-1]:
        val += 1
    return val + 1


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(next_pal, (
        (11, 22),
        (188, 191),
        (191, 202),
        (2541, 2552),
    ))
