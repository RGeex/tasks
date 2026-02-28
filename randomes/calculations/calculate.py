"""
Напишите функцию, которая принимает 3 значения. Первое и третье значения — числа.
Второе значение — символ.

    Если персонаж "+", "-", "*", или "/"Функция вернет результат соответствующей
    математической функции, примененной к двум числам.
    Если строка не содержит ни одного из указанных символов,
    функция должна вернуть null (выбросить исключение). ArgumentException(на языке C#).
    Помните, что деление на ноль невозможно. Если будет предпринята попытка деления на ноль,
    верните значение. null/ None(Python) / throw an ArgumentException(C#).

(2,"+", 4) --> 6
(6,"-", 1.5) --> 4.5
(-4,"*", 8) --> -32
(49,"/", -7) --> -7
(8,"m", 2) --> null
(4,"/",0) --> null


"""
import unittest
from typing import Any, Callable, Optional, Tuple


def calculate(num1: int | float, operation: str, num2: int | float) -> Optional[int | float]:
    """
    Производит вычисления на заданными числами.
    """
    try:
        return eval(f'{num1}{operation}{num2}')
    except Exception:
        pass


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(calculate, (
        ((3.2,"+", 8), 11.2),
        ((3.2,"-", 8), -4.8),
        ((3.2,"/", 8), 0.4),
        ((3.2,"*", 8), 25.6),
        ((-3,"+", 0), -3),
        ((-3,"-", 0), -3),
        ((-2, "/", -2), 1),
        ((-3,"*", 0), 0),
        ((-3,"/", 0), None),
        ((-3,"w", 0), None),
        ((-3,"w", 1), None),
    ))
