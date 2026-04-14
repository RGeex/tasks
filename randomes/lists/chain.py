"""
Напишите универсальный цепной преобразователь функций.

Напишите универсальный цепной вызов функций, который принимает начальное значение и
массив функций для его выполнения (массив символов для Ruby).

Входными данными для каждой функции являются выходные данные предыдущей функции
(за исключением первой функции, которая принимает в качестве входных данных начальное значение).
После завершения выполнения функция возвращает конечное значение.

def add10(x): return x + 10
def mul30(x): return x * 30

chain(50, [add10, mul30])
# returns 1800

"""
import unittest
from typing import Any, Callable, List, Tuple


def add10(x): return x + 10
def mul30(x): return x * 30


def chain(init_val: int, functions: List[Callable[[int], int]]) -> int:
    """
    Цепной преобразователь функций.
    """
    return chain(functions.pop(0)(init_val), functions) if functions else init_val


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(chain, (
        ((42, []), 42),
        ((50, [mul30]), 1500),
        ((50, [mul30, add10]), 1510),
        ((50, [add10, mul30]), 1800),
    ))
