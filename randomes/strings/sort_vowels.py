"""
Отсортируйте гласные!

В этом ката мы хотим отсортировать гласные в особом формате.
Задача

Напишите функцию, которая принимает входную строку sи вернуть строку следующим образом:


                  C|                          R|
                  |O                          n|
                  D|                          d|
   "CODEWARS" =>  |E       "Rnd Te5T"  =>      |
                  W|                          T|
                  |A                          |e
                  R|                          5|
                  S|                          T|

Примечания:

    Перечислите все гласные с правой стороны |
    Перечислите все символы, кроме гласных, на левой стороне |
    Для целей этого ката гласные следующие: a e i o u
    Вернуть каждый символ в его первоначальном регистре
    Каждая строка разделена знаком \n
    Неверный ввод ( undefined / null / integer )должен вернуть пустую строку

"""
import typing
import unittest


def sort_vowels(st: typing.Any) -> str:
    """
    Сортирует гласные в особом формате.
    """
    return '\n'.join([f'{x}|', f'|{x}'][x.lower() in 'aeiou'] for x in st) if isinstance(st, str) else ''


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_vowels, (
        ('Codewars', 'C|\n|o\nd|\n|e\nw|\n|a\nr|\ns|'),
        ('Rnd Te5T', 'R|\nn|\nd|\n |\nT|\n|e\n5|\nT|'),
        (1337, ''),
        (None, ''),
    ))
