"""
О, нет!

Листы с песнями были брошены в снег, и строки каждого куплета перепутались.
Задача

Вам нужно написать функцию сортировки, которая сможет организовать строки в правильном порядке, иначе Рождество будет отменено!

финальный куплет. Напоминание: Ниже показано, как должен выглядеть

On the 12th day of Christmas my true love gave to me
12 drummers drumming,
11 pipers piping, 
10 lords a leaping, 
9 ladies dancing, 
8 maids a milking,
7 swans a swimming, 
6 geese a laying, 
5 golden rings, 
4 calling birds,
3 French hens, 
2 turtle doves and 
a partridge in a pear tree.
"""
import typing
import unittest
from random import shuffle


def song_sorter(lines: list[str]) -> list[str]:
    """
    Сотрирут строки песенки в правльном порядке.
    """
    return sorted(lines, key=lambda x: 'On 12 11 10 9 8 7 6 5 4 3 2 a'.split().index(x.split()[0]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    real_lines = [ 
        "On the 12th day of Christmas my true love gave to me",
        "12 drummers drumming,",
        "11 pipers piping,",
        "10 lords a leaping,",
        "9 ladies dancing,",
        "8 maids a milking,",
        "7 swans a swimming,", 
        "6 geese a laying,", 
        "5 golden rings,", 
        "4 calling birds,",
        "3 French hens,", 
        "2 turtle doves and", 
        "a partridge in a pear tree.",
    ]
    shuffle_lines = real_lines.copy()
    shuffle(shuffle_lines)
    test(song_sorter, (
        (shuffle_lines, real_lines),
    ))
