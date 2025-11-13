"""
Завершите метод, который принимает массив целых чисел и возвращает одно из
следующих значений:

"yes, ascending"- если числа в массиве отсортированы по возрастанию
"yes, descending"- если числа в массиве отсортированы в порядке убывания
"no"- в противном случае
Порядок не обязательно должен быть строгим: отсортированный массив может
содержать последовательные дубликаты, например, [1, 1, 2, 3]отсортирован по
возрастанию.

Гарантируется, что всегда будет единственный правильный ответ. Точнее:

не будет массивов с менее чем 2 элементами
не будет массивов, где все элементы равны
"""
import typing
import unittest


def is_sorted_and_how_1(arr: list[int]) -> str:
    """
    определяет последовательность сортировки списка.
    """
    return all(a < b for a, b in zip(arr, arr[1:])) and 'yes, ascending' or all(a > b for a, b in zip(arr, arr[1:])) and 'yes, descending' or 'no'


def is_sorted_and_how_2(arr: list[int]) -> str:
    """
    определяет последовательность сортировки списка.
    """
    return ['yes, ascending', 'yes, descending', 'no'][next((i for i, x in enumerate((arr, arr[::-1])) if sorted(arr) == x), 2)]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_sorted_and_how_1, (
        ([1, 2], 'yes, ascending'),
        ([15, 7, 3, -8], 'yes, descending'),
        ([4, 2, 30], 'no'),
    ))
    test(is_sorted_and_how_2, (
        ([1, 2], 'yes, ascending'),
        ([15, 7, 3, -8], 'yes, descending'),
        ([4, 2, 30], 'no'),
    ))
