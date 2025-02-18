"""
Отфильтруйте номер

О, нет! Число было смешано с текстом. Ваша цель - получить номер из текста, можете ли вы вернуть номер обратно в его первоначальное состояние?
Задача

Ваша задача - вернуть число из строки.
Подробности

Вам будет предоставлена ​​ряд чисел и букв, смешанных, вам нужно вернуть все числа в этой строке в порядке, который они встречаются.
"""
import typing
import unittest


def filter_string(st: str) -> str:
    """
    Из строки получает число.
    """
    return int(''.join(n for n in st if n.isdigit()))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(filter_string, (
        ("123", 123),
        ("a1b2c3", 123),
        ("aa1bb2cc3dd", 123),
        ("aa 112 3dd", 1123),
        ("11bb2c23c3", 112233),
    ))
