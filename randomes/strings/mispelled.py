"""
Создайте функцию mispelled(word1, word2):

mispelled('versed', 'xersed') # returns True
mispelled('versed', 'applb') # returns False
mispelled('versed', 'v5rsed') # returns True
mispelled('1versed', 'versed') # returns True
mispelled('versed', 'versed') #returns True 

Он проверяет, отличается ли слово2 от слова1 максимум на один символ.

Это может быть дополнительный символ в конце или начале любого из слов.

В тестах, которые ожидаются true, неправильно написанное слово всегда будет отличаться в
основном одним символом. Если два слова одинаковы, вернуть True.

"""
import typing
import unittest
from itertools import zip_longest


def mispelled(*args: str) -> bool:
    """
    Проверяет, отличаютлся ли слова менее чем на 2 символа.
    """
    return min(map(sum, [[a != b for a, b in zip_longest(*x)] for x in (args, map(lambda x: x[::-1], args))])) < 2


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(mispelled, (
        (('versed', 'xersed'), True),
        (('versed', 'applb'), False),
        (('versed', 'v5rsed'), True),
        (('1versed', 'versed'), True),
        (('versed', 'versed'), True),
    ))
