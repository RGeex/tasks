"""
Двоичный пробел внутри положительного числа numэто любая последовательность последовательных нулей,
окруженная единицами с обоих концов в двоичном представлении num.
Например:
9имеет двоичное представление 1001и содержит двоичный промежуток длиной 2.
529имеет двоичное представление 1000010001и содержит два бинарных пробела:
один длиной 4 и один длиной 3.
20имеет двоичное представление 10100и содержит один двоичный пробел длиной 1.
15имеет двоичное представление 1111и имеет 0бинарные пробелы.
Писать function gap(num) что, учитывая положительный num, возвращает длину самого длинного
двоичного промежутка.
Функция должна возвращать 0 если numне содержит двоичного пробела.
"""
import typing
import unittest


def gap(num: int) -> int:
    """
    Поиск длины максимального пробела для заданного числа.
    """
    return max(map(len, f'{num:b}'.strip('0').split('1')))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(gap, (
        (9, 2),
        (529, 4),
        (20, 1),
        (15, 0),
    ))
