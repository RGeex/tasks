"""
Получив на вход массив цифр, верните массив, в котором каждая цифра увеличивается на единицу,
на которую она находится в массиве: первая цифра увеличивается на 1, вторая — на 2 и так далее.
Убедитесь, что отсчет начинается с 1 (а не с 0).

Результат может содержать только однозначные числа, поэтому, если сложение цифры и её позиции даёт
многозначное число, следует вернуть только последнюю цифру этого числа.
Примечания:

    Если массив пуст, верните пустой массив.
    Массивы содержат только числа, поэтому не беспокойтесь об этом.

Примеры:

[1, 2, 3]  -->  [2, 4, 6]   #  [1+1, 2+2, 3+3]

[4, 6, 9, 1, 3]  -->  [5, 8, 2, 5, 8]  #  [4+1, 6+2, 9+3, 1+4, 3+5]
                                       #  9+3 = 12  -->  2

"""
import unittest
from typing import Any, Callable, List, Tuple


def incrementer(nums: List[int]) -> List[int]:
    """
    Обрабатывает входящий массив по заданному алгоритму.
    """
    return [sum(x) % 10 for x in enumerate(nums, 1)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(incrementer, (
        ([], []),
        ([1, 2, 3], [2, 4, 6]),
        ([4, 6, 7, 1, 3], [5, 8, 0, 5, 8]),
        ([3, 6, 9, 8, 9], [4, 8, 2, 2, 4]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8], [2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2]),
    ))
