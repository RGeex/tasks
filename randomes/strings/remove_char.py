"""
Вам предоставили список с указанием дневной выручки на каждый день недели.
К сожалению, список повреждён и содержит лишние символы. Вместо того, чтобы
устранить причину проблемы, ваш начальник попросил вас создать программу,
которая удалит все лишние символы и вернёт исправленный список.

Ожидаемые символы — цифры, «$» и «.». Ожидается, что все элементы в
возвращаемом списке будут строками.

Например:

a1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']
remove_char(a1)
>>> ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']


"""
import typing
import unittest
import re


def remove_char(array: list[str]) -> list[str]:
    """
    Убирает лишние символы и форматируем строки из списка по заданному шаблону.
    """
    return [re.sub(r'^(.*?)(\d{2})$', r'$\1.\2', re.sub(r'[^\d]', '', x)) for x in array]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_char, (
        (['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94'], ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']),
        (['%$$$%$9p2. 42', '"e"$1..5o.4/d9', '$29.29', ',$,.59,.,25', 'E$5.0O0'], ['$92.42', '$15.49', '$29.29', '$59.25', '$5.00']),
        (['#...$0...00'"'", '$44.59', '{}$$$$.$$...92))().f8f3', '$41.a11', '$about3.50'], ['$0.00', '$44.59', '$92.83', '$41.11', '$3.50']),
    ))
