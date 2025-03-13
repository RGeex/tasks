"""
Ваша задача — удалить все последовательные дубликаты слов из строки, оставив только записи первых
слов. Например:

"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

--> "alpha beta gamma delta alpha beta gamma delta"

Слова будут разделены одним пробелом. В строке не будет начальных или конечных пробелов. Пустая
строка (0 слов) является допустимым вводом.
"""
import typing
import unittest
from itertools import groupby


def remove_consecutive_duplicates(st: str) -> str:
    """
    Удаляет из строки последовательно идущие дубликаты слов.
    """
    return ' '.join([x for x, _ in groupby(st.split())])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_consecutive_duplicates, (
        ("", ""),
        ('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta', 'alpha beta gamma delta alpha beta gamma delta'),
        ("iIi IiI", "iIi IiI"),
        ("aa a aa a aa", "aa a aa a aa"),
        ("this his is is sih siht", "this his is sih siht"),
        ("don't don t do not dont", "don't don t do not dont"),
    ))
