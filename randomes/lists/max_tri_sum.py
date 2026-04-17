"""
Задача

Дан массив/список целых чисел. Найдите максимальную сумму этих чисел. 3DISTINCT элементы массива.
Примечания :

    Размер массива должен быть не менее 3 .
    Элементы массива могут быть равны нулю или иметь отрицательное значение.
    повторяющиеся числа В массиве/списке могут встречаться,
    поэтому (дубликаты не учитываются при суммировании) .

Примеры ввода и вывода

    maxTriSum ({3,2,6,8,2,3}) ==> return (17)

    Лучшая тройка = {6,8,3} , её сумма равна 17.

    maxTriSum ({2,1,8,0,6,4,8,6,2,4}) ==> return (18)

    Лучшая тройка = {8, 6, 4} , её сумма равна 18.

    maxTriSum ({-7,12,-7,29,-5,0,-7,0,0,29}) ==> return (41)

    Лучшая тройка = {12, 29, 0} , её сумма равна 41.


"""
import unittest
from typing import Any, Callable, List, Tuple


def max_tri_sum(numbers: List[int]) -> int:
    """
    Поиск максимальной суммы не учитывая дубликаты.
    """
    return sum(sorted(set(numbers))[-3:])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(max_tri_sum, (
        ([3, 2, 6, 8, 2, 3], 17),
        ([2, 9, 13, 10, 5, 2, 9, 5], 32),
        ([2, 1, 8, 0, 6, 4, 8, 6, 2, 4], 18),
        ([-3, -27, -4, -2, -27, -2], -9),
        ([-14, -12, -7, -42, -809, -14, -12], -33),
        ([-13, -50, 57, 13, 67, -13, 57, 108, 67], 232),
        ([-7, 12, -7, 29, -5, 0, -7, 0, 0, 29], 41),
        ([-2, 0, 2], 0),
        ([-2, -4, 0, -9, 2], 0),
        ([-5, -1, -9, 0, 2], 1),
    ))
