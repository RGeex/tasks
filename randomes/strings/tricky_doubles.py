"""
Напишите функцию, которая возвращает удвоенное значение входных данных,
за исключением случаев, когда значение является "хитрым числом с плавающей запятой".

Число считается «хитрой дублью», если оно состоит из двух одинаковых половин
без дополнительных цифр. Например, 44, 1212, и 7777Удвоение чисел — сложная задача,
потому что каждая половина числа одинакова. 4 и 4, 12 и 12, 77 и 77).

Если входное значение представляет собой сложный тип double, верните его как есть.
В противном случае верните значение, умноженное на 2.

Примеры сложных чисел с плавающей запятой:

    44состоит из двух 4с
    77состоит из двух 7с
    3333состоит из двух 33с
    8787состоит из двух 87с
    100100состоит из двух 100с

В примере 8787 число 87 удваивается (появляется дважды).

trickyDoubles(15)   // should return 30
trickyDoubles(100)  // should return 200
trickyDoubles(4343) // should return 4343


"""
import unittest
from typing import Any, Callable, Tuple


def tricky_doubles(num: int) -> int:
    """
    Удваивает число, если оно не является хитрым.
    """
    return num * [1, 2][len(str(num)) % 2 or not str(num).startswith(str(num)[len(str(num)) // 2:])]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(tricky_doubles, (
        (2, 4),
        (34, 68),
        (14521452, 14521452),
    ))
