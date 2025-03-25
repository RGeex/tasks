"""
Ваша задача — вернуть выходную строку, которая переводит входную строку sзаменив
каждый символ в st с числом, представляющим количество раз, когда этот символ
встречается в sи разделяя каждое число знаком sepперсонаж(и).

Пример (s, sep --> Вывод)

"hello world", "-" --> "1-1-3-3-2-1-1-2-1-3-1"
"19999999"   , ":" --> "1:7:7:7:7:7:7:7"
"^^^**$"     , "x" --> "3x3x3x2x2x1"
"""
import typing
import unittest


def freq_seq(st: str, sep: str) -> str:
    """
    Заменяет символы кол-вом, которые они встречаются в строке, через заданный разделитель.
    """
    return f'{sep}'.join(str(st.count(x)) for x in st)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(freq_seq, (
        (('hello world', '-'), '1-1-3-3-2-1-1-2-1-3-1'),
        (('19999999', ':'), '1:7:7:7:7:7:7:7'),
        (('^^^**$', 'x'), '3x3x3x2x2x1'),
    ))
