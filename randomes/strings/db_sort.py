"""
Достаточно просто - вам будет дан массив. Значения в массиве будут либо числами, либо строками,
либо смесью того и другого. Вы не получите ни пустой массив, ни разреженный.

Ваша задача — вернуть один массив, в котором сначала идут числа, отсортированные по возрастанию,
а затем строки, отсортированные по алфавиту. Значения должны сохранять свой исходный тип.

Обратите внимание, что числа, записанные в виде строк, являются строками и должны быть
отсортированы вместе с другими строками.
"""
import typing
import unittest


def db_sort(arr: list) -> list:
    """
    Сортировка смешанного массива, сначала числа потом строки.
    """
    return sorted(arr, key=lambda x: (isinstance(x, str), x))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(db_sort, (
        ([6, 2, 3, 4, 5], [2, 3, 4, 5, 6]),
        ([14, 32, 3, 5, 5], [3, 5, 5, 14, 32]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        (["Banana", "Orange", "Apple", "Mango", 0, 2, 2], [0,2,2,"Apple","Banana","Mango","Orange"]),
        (["C", "W", "W", "W", 1, 2, 0], [0,1,2,"C","W","W","W"]),
        (['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6], [5,6,6,7,10,15,110,"!","2500","come","on"]),
        (["Apple",46,"287",574,"Peach","3","69",78,"Grape","423"], [46, 78, 574, '287', '3', '423', '69', 'Apple', 'Grape', 'Peach'] ),

    ))
