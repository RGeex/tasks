"""
Учитывая строку из цифр [0-9], вернуть строку, где каждая цифра повторяется несколько раз, равна ее значению.
Примеры

"312" should return "333122"

"102269" should return "12222666666999999999"
"""
import typing
import unittest


def explode(st: str) -> str:
    """
    Преобразует строку из цифр [0-9], где каждая цифра повторяется значения цифры.
    """
    return ''.join(n * int(n) for n in st)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(explode, (
        ('0', ''),
        ('000', ''),
        ('312', '333122'),
        ('123', '122333'),
        ('102269','12222666666999999999'),
    ))
