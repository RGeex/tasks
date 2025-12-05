"""
Дан список целых чисел (может быть положительным или отрицательным) , найдите целое число с
наибольшим количеством единичных битов в его двоичном дополнительном представлении .
Пример

most_one_bits([[3, 7, 8, 9, 15]) => #Output: 15 (it has 4 '1' bits)

most_one_bits([3, 7, 8, 9, 23, 28]) => #Output: 23 (it has 4 '1' bits)

В случае равенства чисел вернуть последнее целое число в списке с наибольшим количеством единичных
битов .

most_one_bits([6, 3, 6, 9, 10]) => #Output: 10 (all have 2 '1' bits
but 10 is the last)

Примечание:

Целые числа должны быть представлены в 8 битах.

Для положительных чисел расчет единичных битов в двоичном представлении остается тем же, но
отрицательные целые числа будут иметь другие результаты.

most_one_bits([-1,-2,-3]) => #Output -1( it has total of 8 '1' bits)

Дубликаты

В случае дублирования целых чисел будет учитываться только первое вхождение.

Пример

most_one_bits([85, 120,-23,-15,-23]) =>#Output -15

( first occurrence of -15 is after first occurrence -23)

Входной список никогда не будет пустым ([])

"""
import unittest
from typing import Any, Callable, List, Tuple


def most_one_bits(nums: List[int]) -> int:
    """
    Определяет последнее число в списке с наибольшим кол-вом битов.
    """
    return max(sorted(set(nums), key=nums.index)[::-1], key=lambda x: format((x < 0 and 256) + x, '08b').count('1'))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(most_one_bits, (
        ([3, 7, 8, 9, 15], 15),
        ([3, 7, 8, 9, 23, 28], 23),
        ([3, 5, 6, 9, 10], 10),
        ([1], 1),
        ([-1, -2, -3], -1),
        ([85, 120, -23, -15, -23], -15),
    ))
