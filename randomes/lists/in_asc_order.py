"""
Цифры указаны в правильном порядке?
В этом задании ваша функция принимает на вход массив целых чисел. Ваша задача — определить,
расположены ли числа в порядке возрастания. Массив считается расположенным в порядке возрастания,
если нет двух соседних целых чисел, у которых значение левого целого числа превышает
значение правого целого числа.

Для целей данного задания вы можете предположить, что все входные данные являются допустимыми,
то есть массивами, содержащими только целые числа.

Обратите внимание, что массив из 0 или 1 целых чисел автоматически считается отсортированным в
порядке возрастания, поскольку все (ноль) смежные пары целых чисел удовлетворяют условию,
что значение левого целого числа не превышает значение правого целого числа.

Например:

in_asc_order([1,2,4,7,19]) # returns True
in_asc_order([1,2,3,4,5]) # returns True
in_asc_order([1,6,10,18,2,4,20]) # returns False
in_asc_order([9,8,7,6,5,4,3,2,1]) # returns False because the numbers are in DESCENDING order
Примечание: Если ваше решение проходит все фиксированные тесты, но не проходит случайные тесты,
убедитесь, что вы не изменяете входной массив.
"""
import unittest
from typing import Any, Callable, List, Tuple


def in_asc_order(arr: List[int]) -> bool:
    """
    Определяет, расположены ли числа в порядке возрастания.
    """
    return next((False for i, n in enumerate(arr) if i and arr[i - 1] > n), True)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(in_asc_order, (
        ([1, 2], True),
        ([2, 1], False),
        ([1, 2, 3], True),
        ([1, 3, 2], False),
        ([1, 4, 13, 97, 508, 1047, 20058], True),
        ([56, 98, 123, 67, 742, 1024, 32, 90969], False),
    ))
