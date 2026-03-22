"""
Вы работаете в лучшей корпорации по производству бытовой электроники,
и ваш начальник хочет выяснить, какие три продукта приносят наибольшую прибыль.
Даны 3 списка одинаковой длины, подобные этим:

    товары: ["Computer", "Cell Phones", "Vacuum Cleaner"]
    суммы: [3, 24, 8]
    цены: [199, 299, 399]

Верните три названия продуктов с наибольшей выручкой ( amount * price), в порядке убывания
(от наибольшего к наименьшему доходу).

Примечание : если несколько товаров имеют одинаковый доход, упорядочьте их в соответствии
с их исходными позициями во входном списке.


"""
import unittest
from typing import Any, Callable, List, Tuple


def top3(products: List[str], amounts: List[int], prices: List[int]) -> List[str]:
    """
    Определяет 3 наиболее прибыльных продукта.
    """
    return sorted(products, key=lambda x: -amounts[products.index(x)] * prices[products.index(x)])[:3]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(top3, (
        ((['Computer', 'Cell Phones', 'Vacuum Cleaner'],
          [3, 24, 8],
          [199, 299, 399]),
            ['Cell Phones', 'Vacuum Cleaner', 'Computer']),

        ((['Cell Phones', 'Vacuum Cleaner', 'Computer', 'Autos', 'Gold', 'Fishing Rods', 'Lego', 'Speakers'],
          [5, 25, 2, 7, 10, 3, 2, 24],
          [51, 225, 22, 47, 510, 83, 82, 124]),
            ['Vacuum Cleaner', 'Gold', 'Speakers']),

        ((['Cell Phones', 'Vacuum Cleaner', 'Computer', 'Autos', 'Gold', 'Fishing Rods', 'Lego', 'Speakers'],
          [0, 12, 24, 17, 19, 23, 120, 8],
            [9, 24, 29, 31, 51, 8, 120, 14]),
            ['Lego', 'Gold', 'Computer']),

        ((['Speakers', 'Games', 'Radios', 'Drones', 'Scooter'],
          [1, 1, 1, 1, 1],
            [10, 10, 10, 10, 10]),
            ['Speakers', 'Games', 'Radios']),
    ))
