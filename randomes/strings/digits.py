"""
Определите общее количество цифр в целом числе ( n>=0) задано в качестве входных данных для функции.
Например, 9 — это одна цифра, 66 имеет 2 цифры, а 128685 имеет 6 цифр. Будьте осторожны,
чтобы избежать переполнений/недополнений.

Все введенные данные будут действительны.

"""
import typing
import unittest


def digits(num: int) -> int:
    """
    Подсчитывает кол-во цифр в десятичном числе.
    """
    return len(str(num))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(digits, (
        (5, 1),
        (12345, 5),
        (9876543210, 10),
    ))
