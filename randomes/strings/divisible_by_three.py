"""
Уловка, которую я изучил в начальной школе, чтобы определить, было ли число делится на три, заключается в том,
чтобы добавить все целые числа в число вместе и разделить полученную сумму на три. Если нет остатка от деления
суммы на три, то первоначальное число делится на три.

Учитывая серию цифр в качестве строки, определите, делится ли число по строке на три.

Пример:

"123"      -> true
"8409"     -> true
"100853"   -> false
"33333333" -> true
"7"        -> false

Старайтесь избегать использования оператора % (Modulo). 
"""
import typing
import unittest


def divisible_by_three(st: str) -> bool:
    """
    Определяет, делится ли без остатка сумма цифр с в строке.
    """
    return not sum(map(int, st)) % 3


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(divisible_by_three, (
        ('123', True),
        ('19254', True),
        ('88', False),
        ('1', False),
    ))
