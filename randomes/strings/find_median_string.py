"""
Вам дана строка. Ваша задача — преобразовать её в верхний регистр,
затем найти сумму каждого символа, преобразованного в его код ASCII,
затем разделить сумму на длину строки, округлить в меньшую сторону и
преобразовать полученное значение в эквивалентный символ в коде ASCII.

Примечание: делайте это максимально 57персонажи
Примеры

"abc"  -->  "B"
"asd"  -->  "H"
"iamareallyreallylongstringthatiscompletelyworthlessandisheretostophardcoders"  -->  "L"
"""
import typing
import unittest


def find_median_string(st: str) -> str:
    """
    Поиск средней буквы ASCII среди строки букв.
    """
    return chr(sum(map(ord, st.upper())) // len(st))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_median_string, (
        ('abc', 'B'),
        ('asd', 'H'),
        ('iamareallyreallylongstringthatiscompletelyworthlessandisheretostophardcoders', 'L'),
    ))
