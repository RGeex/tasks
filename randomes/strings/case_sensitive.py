"""
Ваша задача очень проста. Дана входная строка s, case_sensitive(s), проверьте, все ли буквы строчные или нет.
Верните True/False и список всех записей, которые не являются строчными, в порядке их появления в s.

Например, case_sensitive('codewars') возвращает [True, []], а case_sensitive('codeWaRs') возвращает [False, ['W', 'R']].

Удачи :) 
"""
import typing
import unittest


def case_sensitive(st: str) -> list[bool, list[str]]:
    """
    Получает данные на основе строки, по заданным критериям.
    """
    return [not (x := [x for x in st if x.isupper()]), x]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(case_sensitive, (
        ('asd', [True, []]),
        ('cellS', [False, ['S']]),
        ('z', [True, []]),
        ('', [True, []]),
    ))
