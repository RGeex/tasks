"""
Дан список чисел. Сложите несколько раз соседние пары чисел,
пока не останется только одно число.
Объяснение

Если список есть [1, 2, 3, 4, 5], первым шагом будет:

    1 + 2 = 3

    2 + 3 = 5

    3 + 4 = 7

    4 + 5 = 9

Возьмите результаты первого шага и повторите процесс сложения смежных пар:

    3 + 5 = 8

    5 + 7 = 12

    7 + 9 = 16

Продолжайте этот процесс, пока не останется только одно число:

    8 + 12 = 20

    12 + 16 = 28

Окончательно,

    20 + 28 = 48

Окончательный результат для списка [1, 2, 3, 4, 5] является 48.
Примеры

    Для списка [-1, -1, -1], результат есть -4.

    Для списка [1, 2, 3, 4], результат есть 20.

Примечание

    Входной список всегда будет содержать хотя бы одно число.

    Все элементы в списке будут допустимыми числами.


"""
import typing
import unittest


def total(arr: list[int]) -> int:
    """
    Суммирует значения списка попарно, пока не останется одно значение.
    """
    return total([sum(x) for x in zip(arr, arr[1:])]) if len(arr) > 1 else arr[0]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(total, (
        ([1, 2, 3, 4, 5], 48),
        ([1, 2, 3, 4], 20),
        ([1, 2, 3], 8),
        ([4, 4, 52, 23, 32, 1, -1], 1753),
        ([4, 4, 5, -1], 30),
        ([-1, -1, -1], -4),
        ([-1, -1, -10, 42, 92, 1, 23, 6, -3], 9248),
        ([-1, 1, -1, 1], 0),
        ([42], 42),
        ([-1, -1, -10, 42, 92, 1, 23, 6, -3], 9248),
    ))
