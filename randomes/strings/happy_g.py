"""
Задача

Скажем так "g" is happyв данной строке, если непосредственно справа или слева от нее находится еще одна буква «g».

Выясните, все ли буквы «g» в заданной строке являются счастливыми.
Пример

Для str = "gg0gg3gg0gg", вывод должен быть true.

Для str = "gog", вывод должен быть false.
Ввод/вывод

    [input] нить str

Случайная строка из строчных букв, цифр и пробелов.

    [output]логическое значение

trueесли все "g"ы счастливы, false в противном случае.

"""
import typing
import unittest
from itertools import groupby


def happy_g(st: str) -> bool:
    """
    Проверяет есть ли у всех букв "g" рядом пара.
    """
    return all(len(list(b)) > 1 for a, b in groupby(st) if a == 'g')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(happy_g, (
        ("gg0gg3gg0gg", True),
        ("gog", False),
        ("ggg ggg g ggg", False),
        ("A half of a half is a quarter.", True),
        ("good grief", False),
        ("bigger is ggooder", True),
        ("gggggggggg", True),
    ))
