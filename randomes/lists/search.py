"""
Вы любите кофе и хотите узнать, какие зерна вы можете себе позволить покупать.

Первым аргументом вашей функции поиска будет число, представляющее ваш бюджет.

Вторым аргументом будет массив цен на кофейные зерна.

Ваша функция «поиска» должна возвращать магазины, продающие кофе в рамках вашего бюджета.

Функция поиска должна возвращать строку цен на кофейные зерна, которые вы можете себе позволить. Цены в этой строке должны быть отсортированы по возрастанию.
"""
import typing
import unittest


def search(budget: int, prices: list[int|float]) -> str:
    """
    Определяет цены которые доступны покупателю.
    """
    return ','.join(sorted([str(n) for n in prices if n <= budget], key=float))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(search, (
        ((3, [6, 1, 2, 9, 2]), "1,2,2"),
        ((14, [7, 3, 23, 9, 14, 20, 7]), "3,7,7,9,14"),
        ((0, [6, 1, 2, 9, 2]), ""),
        ((10, []), ""),
        ((10, [0, 0, 0]), "0,0,0"),
        ((0, [0, 0, 0]), "0,0,0"),
        ((24, [24, 0, 100, 2, 5]), "0,2,5,24"),
        ((24, [2.7, 0, 100.9, 1, 5.5]), "0,1,2.7,5.5"),
        ((-1, [1, 2, 3, 4]), ""),
        ((-1, [-1, 0, 1, 2, 3, 4]), "-1"),
        ((14, [17, 33, 23, 19, 19, 20, 17]), ""),
        ((14, [13, 15, 14, 14, 15, 13]), "13,13,14,14"),
    ))
