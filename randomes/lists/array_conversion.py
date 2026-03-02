"""
Задача

Дан массив из 2 элементов. к целые числа (для некоторого целого числа) k
Выполните следующие операции, пока массив не будет содержать только один элемент:

1-го, 3-го, 5-го и т. д. 
В итерациях (с 1-й отсчеты) каждая пара последовательных элементов заменяется их суммой;
2-го, 4-го, 6-го и т. д. 
В ходе итераций каждая пара последовательных элементов заменяется их произведением.

После завершения работы алгоритма в массиве останется один элемент. Верните этот элемент.
Пример

Для inputArray = [1, 2, 3, 4, 5, 6, 7, 8] на выходе должно получиться 186.

У нас есть [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186]
Таким образом, ответ — 186.
Ввод/вывод

    [input]целочисленный массив arr

    Ограничения: 2 1 ≤ arr.length ≤ 2 5 , -9 ≤ arr[i] ≤ 99.

    [output]целое число


"""
import unittest
from typing import Any, Callable, List, Tuple


def array_conversion(arr: List[int], n: int = 0) -> int:
    """
    Выполняет последовательность операций, пока в массиве более 1 элемента.
    """
    return array_conversion([[a + b, a * b][n % 2] for a, b in zip(arr[0::2], arr[1::2])], n + 1) if len(arr) > 1 else arr[-1]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(array_conversion, (
        ([1, 2, 3, 4, 5, 6, 7, 8], 186),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 64),
        ([3, 3, 5, 5], 60),
    ))
