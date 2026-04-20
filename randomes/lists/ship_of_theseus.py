"""
«Корабль Тесея» — это классический философский мысленный эксперимент о формировании
идентичности во времени.

В нем задается вопрос: если каждую часть корабля постепенно заменять по одной детали,
останется ли это в итоге тот же самый корабль?

В этом ката эта идея превращается в простую задачу проверки.

Корабль представлен матрицей состояний.

В каждом ряду показано судно в разный момент времени.

Считается, что судно осталось неизменным только в том случае, если между каждыми двумя
последовательными рядами изменилась ровно одна его часть.
Правила

    Все строки должны иметь одинаковую длину.
    Строки необходимо сравнивать по позициям .
    Между одним рядом и следующим ровно один элемент (часть корабля) . должен отличаться
    Если какой-либо переход изменяет ноль элементов или более одного элемента,
    процесс считается недействительным.

верните true Если весь процесс корректен, , в противном случае — false .

Если матрица имеет 0 или 1 строку, верните true .
Пример

Начальные значения:

[
  ["a", "b", "c"],
  ["x", "b", "c"],
  ["x", "y", "c"],
  ["x", "y", "z"]
]

Шаг за шагом

["a", "b", "c"] -> ["x", "b", "c"] -> 1 change
["x", "b", "c"] -> ["x", "y", "c"] -> 1 change
["x", "y", "c"] -> ["x", "y", "z"] -> 1 change

Результат

true

Ещё один пример

Начальные значения:

[
  ["a", "b", "c"],
  ["x", "y", "c"]
]

Шаг за шагом

["a", "b", "c"] -> ["x", "y", "c"] -> 2 changes

Результат

false

Пример различной длины строк

Начальные значения:

[
  ["a", "b", "c"],
  ["x", "b"]
]

Шаг за шагом

The rows have different lengths, so the process is invalid.

Результат

false
"""
import unittest
from typing import Any, Callable, List, Tuple
from itertools import zip_longest as zl


def ship_of_theseus(ship: List[List[str]]) -> bool:
    """
    Является ли корабль кораблем Тесея.
    """
    return next((False for i, x in enumerate(ship[1:]) if sum(a != b for a, b in zl(x, ship[i], fillvalue='.')) != 1), True)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(ship_of_theseus, (
        ([["a", "b", "c"], ["x", "b", "c"], ["x", "y", "c"], ["x", "y", "z"]], True),
        ([["a", "b", "c"], ["x", "y", "c"]], False),
        ([["a", "b", "c"], ["x", "b"]], False),
        ([["a", "b", "c"]], True),
        ([], True),
    ))
