"""
Данута упорядоченная последовательность чисел от 1 до N. Из неё могло быть удалено одно число,
а оставшиеся числа перемешались. Найдите число, которое было удалено.

Пример:

Начальная последовательность массивов:[1,2,3,4,5,6,7,8,9]
Смешанный массив с одним удаленным числом — это[3,2,4,6,7,8,1,9]
Ваша функция должна возвращать целое число 5.
Если из исходного массива не было удалено ни одного числа, ваша функция должна вернуть целое число 0.

Примечание : N может быть равно 1 или меньше (в последнем случае первый массив будет []).
"""
import unittest
from typing import Any, Callable, List, Tuple


def find_deleted_number(arr: List[int], mixed_arr: List[int]) -> int:
    """
    Поиск удаленного числа в списке.
    """
    return max(set(arr + [0]) - set(mixed_arr))


def find_deleted_number_2(arr: List[int], mixed_arr: List[int]) -> int:
    """
    Поиск удаленного числа в списке.
    """
    return sum(arr) - sum(mixed_arr)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_deleted_number, (
        (([1, 2, 3, 4, 5], [3, 4, 1, 5]), 2),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 9, 7, 4, 6, 2, 3, 8]), 5),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 7, 6, 9, 4, 8, 1, 2, 3]), 0),
    ))
    test(find_deleted_number_2, (
        (([1, 2, 3, 4, 5], [3, 4, 1, 5]), 2),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 9, 7, 4, 6, 2, 3, 8]), 5),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 7, 6, 9, 4, 8, 1, 2, 3]), 0),
    ))
