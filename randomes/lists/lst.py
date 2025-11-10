"""
В Haskell есть несколько полезных функций для работы со списками:

$ ghci
GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
λ head [1,2,3,4,5]
1
λ tail [1,2,3,4,5]
[2,3,4,5]
λ init [1,2,3,4,5]
[1,2,3,4]
λ last [1,2,3,4,5]
5
Ваша задача — реализовать эти функции на выбранном вами языке. Убедитесь, что они не редактируют массив; это может вызвать проблемы! Вот шпаргалка:

| HEAD | <----------- TAIL ------------> |
[  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
| <----------- INIT ------------> | LAST |

head [x] = x
tail [x] = []
init [x] = []
last [x] = x
Вот как я ожидаю, что функции будут вызываться на вашем языке:

head([1,2,3,4,5]) => 1
tail([1,2,3,4,5]) => [2,3,4,5]
"""
import typing
import unittest


def head(lst: list[int]) -> int:
    """
    Возвращает первый элемент списка.
    """
    return lst[0]


def last(lst: list[int]) -> int:
    """
    Возвращает последний элемент списка.
    """
    return lst[-1]


def tail(lst: list[int]) -> list[int]:
    """
    Возвращает список элементов начиная с второго.
    """
    return lst[1:]


def init(lst: list[int]) -> list[int]:
    """
    Возвращает список элементов кроме последнего.
    """
    return lst[:-1]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(head, (
        ([5,1], 5 ),
    ))
    test(tail, (
        ([1], [] ),
    ))
    test(init, (
        ([1,5,7,9], [1,5,7] ),
    ))
    test(last, (
        ([7,2], 2 ),
    ))
