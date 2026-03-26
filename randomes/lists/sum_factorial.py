"""

Факториалы часто используются в теории вероятностей и применяются в качестве вводной задачи для
освоения конструкций с циклами. В этом задании вы будете складывать несколько факториалов.

Вот несколько примеров факториалов:

4 Factorial = 4! = 4 * 3 * 2 * 1 = 24

6 Factorial = 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

В этом задании вам будет дан список значений, для которых вы должны сначала найти факториал,
а затем вернуть их сумму.

Например, если вам передали список [4, 6]Эквивалентное математическое выражение выглядело бы так:
4! + 6!что будет равно 744.

Удачи!

Примечание: Предполагается, что все значения в списке являются положительными целыми числами > 0,
и каждое значение в списке уникально.

Кроме того, вам необходимо написать собственную реализацию вычисления факториала, поскольку
использовать встроенную функцию невозможно. math.factorial()метод.

"""
import unittest
from typing import Any, Callable, List, Tuple


DATA = {1: 1}


def fact(n: int) -> int:
    """
    Вычисление факториала + кеш.
    """
    if DATA.get(n):
        return DATA[n]
    DATA[n] = fact(n - 1) * n
    return DATA[n]


def sum_factorial(lst: List[int]) -> int:
    """
    Вычисление суммы факториалов.
    """
    return sum(map(fact, lst))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_factorial, (
        ([4, 6], 744),
        ([5, 4, 1], 145),
    ))
