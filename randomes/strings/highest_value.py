"""
Вам будут предоставлены две строки ASCII, a и bВаша задача — написать функцию, которая определит,
какая из этих строк «стоит» больше, и вернуть ее.

Ценность строки определяется суммой ее индексов кодовых точек ASCII. Так, например, строка
HELLOимеет значение 372: H — кодовая точка 72, E — 69, L — 76, а O — 79. Сумма этих значений равна 372.

В случае ничьей следует вернуть первую строку, т.е. a.

"""
import typing
import unittest


def highest_value(a: str, b: str) -> str:
    """
    Определяет строку с большей стоимостью.
    """
    return max(a, b, key=lambda x: sum(map(ord, x)))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(highest_value, (
        (("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"), "KkLlMmNnOoPp4567"),
    ))
