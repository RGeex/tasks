"""
Завершите функцию, которая подсчитывает количество уникальных согласных в строке
(состоящей из печатных символов ASCII).

Согласные — это буквы, используемые в английском языке, за исключением "a", "e", "i", "o", "u".

Помните, ваша функция должна возвращать количество уникальных согласных — без учета дубликатов.
Например, если строка, переданная в функцию, читается как "add", функция должна возвращать
1 скорее, чем 2, с "d"является дубликатом.

Аналогично, функция должна также игнорировать повторяющиеся согласные разных падежей. Например,
"Dad"переданное в функцию должно вернуть 1 как "d" и "D"являются дубликатами.
Примеры

"add" ==> 1
"Dad" ==> 1
"aeiou" ==> 0
"sillystring" ==> 7
"abcdefghijklmnopqrstuvwxyz" ==> 21
"Count my unique consonants!!" ==> 7


"""
import typing
import unittest


def count_consonants(st: str) -> int:
    """
    Подсчитывает кол-во уникальных согласных в строке.
    """
    return sum(x.isalpha() for x in set(st.lower()) - set('aeiou'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count_consonants, (
        ('sillystring', 7),
        ('aeiou', 0),
        ('abcdefghijklmnopqrstuvwxyz', 21),
        ('Count my unique consonants!!', 7),
    ))
