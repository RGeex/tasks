"""

Число состоит просто из цифр.
Число 1256 состоит из цифр 1, 2, 5 и 6.
Для числа 1256 существует 24 различных перестановки цифр:
1256, 1265, 1625, 1652, 1562, 1526, 2156, 2165, 2615, 2651, 2561, 2516,
5126, 5162, 5216, 5261, 5621, 5612, 6125, 6152, 6251, 6215, 6521, 6512.

Ваша задача — написать программу, которая принимает число n и возвращает среднее значение
всех различных перестановок цифр этого числа. Ответ следует округлить до ближайшего целого
числа. В приведенном выше примере возвращаемое значение будет равно 3889.

n никогда не будет отрицательным

Несколько примеров:

permutation_average(2)
return 2

permutation_average(25)
>>> 25 + 52 = 77
>>> 77 / 2 = 38.5
return 39 *

permutation_average(20)
>>> 20 + 02 = 22
>>> 22 / 2 = 11
return 11

permutation_average(737)
>>> 737 + 377 + 773 = 1887
>>> 1887 / 3 = 629
return 629

Примечание: Ваша программа должна уметь обрабатывать числа длиной до 6 цифр.

* В Python версии 3 и выше используется банковское округление, поэтому ожидаемые значения для
этих тестов составят 3888 и 38 соответственно.

"""
import unittest
from typing import Any, Callable, Tuple
from itertools import permutations


def permutation_average(n: int) -> int:
    """
    Вычисляет среднее значение суммы чисел, комбинаций цифр числа.
    """
    x = [int(''.join(x)) for x in permutations(str(n))]
    return round(sum(x) / len(x))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(permutation_average, (
        (2, 2),
        (25, 38),
        (20, 11),
        (737, 629),
    ))
