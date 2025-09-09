"""
Некоторые, но не все
Описание

Ваша задача — создать функцию, которая по заданной последовательности и
предикату возвращает Trueесли только некоторые (но не все) элементы в
последовательности являются Trueпосле применения предиката
Примеры

('abcdefg&%$', x -> isLetter(x)) == true
('&%$=', x -> isLetter x) == false
('abcdefg', x -> isLetter x) == false

([4, 1], x -> x > 3) == true
([1, 1], x -> x > 3) == false
([4, 4], x -> x > 3) == false


"""
import typing
import unittest
from typing import Callable


def some_but_not_all(seq: str, pred: Callable) -> bool:
    """
    Определяет что не все элементы доходят по условию.
    """
    return len(set(map(pred, seq))) > 1


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(some_but_not_all, (
        (('abcdefg&%$', str.isalpha), True),
        (('&%$=', str.isalpha), False),
        (('abcdefg', str.isalpha), False),
        (([4, 1], lambda x: x>3), True),
        (([1, 1], lambda x: x>3), False),
        (([4, 4], lambda x: x>3), False),
    ))
