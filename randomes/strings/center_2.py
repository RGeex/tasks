"""
Ваша компания MRE Tech наняла духовного консультанта, который дал совет по новая политика баланса:
не принимайте чью-либо сторону, не оказывайте предпочтение, оставайтесь посередине. Это политика
применяется даже к программному обеспечению, где все строки теперь должны быть центрированы.
Вы бедняга, раз решили это реализовать.
Задача

Реализовать функцию centerкоторый принимает строку strng, целое число width, и необязательный
символ fill (по умолчанию: ' ') и возвращает новую строку длина width где strngрасположен по
центру и справа и слева дополнен fill.

center(strng, width, fill=' ')

Если левый и правый отступы не могут быть одинаковой длины, сделайте отступ на левая сторона на
один символ длиннее.

Если strngдлиннее, чем width возвращаться strngбез изменений.
Примеры

center('a', 3)  # returns " a "
center('abc', 10, '_')  # returns "____abc___"
center('abcdefg', 2)  # returns "abcdefg"
"""
import typing
import unittest


def center(strng: str, width: int, fill: str = ' ') -> str:
    """
    Центрует строку с использованием заполнителя на заданную длину.
    """
    return f'{strng[::-1]:{fill}^{width}}'[::-1]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(center, (
        (("a", 3), " a "),
        (("abc", 10, '_'), "____abc___"),
        (("abcdefg", 2), "abcdefg"),
    ))
