"""
Если в качестве входных данных задана строка, переместите все ее гласные
в конец строки в том же порядке, в котором они были до этого.

Гласные (в этой ката): a, e, i, o, u

Примечание: все предоставленные входные строки указаны в нижнем регистре.
Примеры

"day"    ==>  "dya"
"apple"  ==>  "pplae"
"""
import typing
import unittest
from operator import add


def move_vowels(st: str) -> str:
    """
    Помещает все гласные в конец слова, в том же порядке.
    """
    return st and ''.join(add(*zip(*[['', x][::x in 'aeiou' or -1] for x in st])))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(move_vowels, (
        ('', ''),
        ('day', 'dya'),
        ('apple', 'pplae'),
        ('peace', 'pceae'),
        ('maker', 'mkrae'),
        ('programming', 'prgrmmngoai'),
        ('javascript', 'jvscrptaai'),
        ('python', 'pythno'),
        ('ruby', 'rbyu'),
        ('haskell', 'hskllae'),
        ('clojure', 'cljroue'),
        ('csharp', 'cshrpa'),
    ))
