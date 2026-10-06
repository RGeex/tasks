"""
Напишите функцию, которая принимает два числа aи bи возвращает в виде строки aзначение, меньшее, большее или равное .b

(5, 4)   ---> "5 is greater than 4"
(-4, -7) ---> "-4 is greater than -7"
(2, 2)   ---> "2 is equal to 2"
Есть только одна проблема...

Вы не ifможете использовать операторы условных операторов, а также тернарный оператор ? :.

На самом деле, это слово ifи этот символ ?не допускаются в вашем коде.
"""
import unittest
from typing import Any, Callable, Tuple


def no_ifs_no_buts(a: int, b: int) -> str:
    """
    Определяет отношение одного числа к другому.
    """
    d = {a < b: 'smaller than', a == b: 'equal to', a > b: 'greater than'}
    return f'{a} is {d[True]} {b}'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(no_ifs_no_buts, (
        ((45, 51), "45 is smaller than 51"),
        ((1, 2), "1 is smaller than 2"),
        ((-3, 2), "-3 is smaller than 2"),
        ((1, 1), "1 is equal to 1"),
        ((100, 100), "100 is equal to 100"),
        ((100, 80), "100 is greater than 80"),
        ((20, 19), "20 is greater than 19"),
    ))
