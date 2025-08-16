"""
Легко: сделайте коробку
При наличии числа в качестве параметра (от 2 до 30) вернуть массив, содержащий строки, образующие поле.

Так:

н = 5

[
  '-----',
  '-   -',
  '-   -',
  '-   -',
  '-----'
]

н = 3

[
  '---',
  '- -',
  '---'
]


"""
import typing
import unittest


def box(n: int) -> list[str]:
    """
    Создает список строк обозначающих коробку.
    """
    return [f'-{"- "[0 < i < n - 1] * (n - 2)}-' for i in range(n)]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase( type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(box, (
        (5,['-----',
            '-   -',
            '-   -',
            '-   -',
            '-----']),
    ))
