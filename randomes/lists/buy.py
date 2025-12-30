"""
История

Вы получили подарочную карту для местного магазина. На ней есть определенный баланс,
который можно использовать для покупок, но только для двух товаров, и любой неиспользованный
баланс теряется. Вы хотите купить что-то для друга и для себя. Поэтому вы хотите купить два
товара, суммарная стоимость которых составит всю сумму подарочной карты.
Задача

Вы получите сумму, равную стоимости подарочной карты. cи конечный список значений элементов.
Вам следует вернуть пару индексов, соответствующих значениям, сумма которых равна c:

buy(2,[1,1])       = [0,1]
buy(3,[1,1])       = None
buy(5,[5,2,3,4,5]) = [1,2]

Индексы начинаются с 0( 1(в COBOL). Первый индекс всегда должен быть меньше второго индекса.
Если существует несколько решений, верните минимальное (лексикографически):

buy(5,[1,2,3,4,5]) = [0,3] # the values at [1,2] also adds up to five, but [0,3] < [1,2]
"""
import unittest
from typing import Any, Callable, List, Tuple, Optional


def buy(x: int, arr: List[int]) -> Optional[List[int]]:
    """
    Поиск 2 чисел в списке, дающих в сумме искомое число.
    """
    return next(([i - 1, arr.index(x - n, i)] for i, n in enumerate(arr, 1) if (x - n) in arr[i:]), None)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(buy, (
        ((2, [1, 1]), [0, 1]),
        ((3, [1, 1]), None),
        ((5, [5, 2, 3, 4, 5]), [1, 2]),
        ((5, [1, 2, 3, 4, 5]), [0, 3]),
        ((5, [0, 0, 0, 2, 3]), [3, 4]),
    ))
