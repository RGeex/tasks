"""
Дана строка s, ваша задача — вернуть другую строку, такую, чтобы четные и нечетные символы s
сгруппированы, и группы разделены пробелами. Четная группа идет первой, за ней следует пробел,
а затем нечетная часть.
Примеры

input:    "CodeWars" => "CdWr oeas"
           ||||||||      |||| ||||
indices:   01234567      0246 1357

Четные индексы 0, 2, 4, 6, поэтому имеем "CdWr"как первая группа.
Нечетные индексы — 1, 3, 5, 7, поэтому вторая группа — "oeas".
И последняя строка для возврата: "Cdwr oeas".
Примечания

Проверяемые строки имеют длину не менее 8 символов.
"""
import typing
import unittest


def sort_my_string(st: str) -> str:
    """
    Из заданной строки создает новую по заданному шаблону.
    """
    return ' '.join(map(''.join, zip(*[['', x][::i % 2 or -1] for i, x in enumerate(st)])))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_my_string, (
        ("CodeWars", "CdWr oeas"),
        ("YCOLUE'VREER", "YOU'RE CLEVER"),
    ))
