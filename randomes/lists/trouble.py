"""
Дан массив целых чисел (x) и целевое число (t). Вам необходимо определить, дают ли любые два последовательных числа в массиве сумму t. Если да, удалите второе число.

Пример:

х = [1, 2, 3, 4, 5]
т = 3

1+2 = t, поэтому удаляем 2. Других пар = t нет, поэтому остальная часть массива остается:

[1, 3, 4, 5]

Пройдитесь по массиву слева направо.

Верните полученный массив.
"""
import typing
import unittest


def trouble(x: list[int], t: int) -> list[int]:
    """
    Удаляет второй элемент если 2 последовательных числа списка в сумме дают t.
    """
    return trouble(x, t) if next((x.pop(i) or 1 for i, (a, b) in enumerate(zip(x, x[1:]), 1) if a + b == t), 0) else x


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(trouble, (
        [([1, 3, 5, 6, 7, 4, 3],7), [1, 3, 5, 6, 7, 4]],
        [([4, 1, 1, 1, 4],2), [4, 1, 4]], 
        [([2, 6, 2],8), [2, 2]], 
        [([2, 2, 2, 2, 2, 2], 4), [2]],
    ))
