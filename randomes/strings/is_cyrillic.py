"""
Буквы кириллицы, используемые в таких языках, как русский и украинский,
имеют другие значения в кодировке Unicode, чем буквы латинского алфавита.
Две из этих букв кириллицы включают: а и укоторые, если вы скопируете эти 2,
не совпадают с латинскими a и y

Не верите мне?
латинский a:
Латинская буква а Конечный результат латинского а
кириллица а:
Кириллица а Конечный результат кириллицы а
Задача

Ваша задача — написать функцию, которая возвращает, является ли заданная
строка (или символ) кириллической буквой в кириллическом блоке Unicode .

Строка (или символ) всегда будет состоять из одной буквы.
Намекать

Вот ссылка на список блоков Unicode для кириллицы в Википедии для справки.

Архив Wayback Machine
Примеры

Input: "D"
Output: false (or False in Python or your language's equivalent)

Input: "Я"
Output: true (or True in Python or your language's equivalent)


"""
import typing
import unittest


def is_cyrillic(letter: str) -> bool:
    """
    Определяет, относится ли указанный символ к кириллице или нет.
    """
    return 1023 < ord(letter) < 1280


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_cyrillic, (
        ("Д", True),
        ("D", False),
        ("а", True),
        ("a", False),
    ))
