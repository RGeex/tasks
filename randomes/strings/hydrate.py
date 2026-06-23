"""
Добро пожаловать в бар Codewars!

В баре Codewars рекомендуют выпивать по одному стакану воды на каждый стандартный напиток,
чтобы завтра утром не было похмелья.

Ваши коллеги-программисты угостили вас сегодня вечером несколькими напитками в виде строки.
Верните строку, указывающую, сколько стаканов воды вам следует выпить, чтобы не испытывать похмелья.
Примеры

"1 beer"  -->  "1 glass of water"
because you drank one standard drink

"1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"  -->  "10 glasses of water"
because you drank ten standard drinks

Примечание:

Для простоты будем считать, что любой «пронумерованный элемент» в строке — это напиток.
Даже "1 bear"-> "1 glass of water"; или "1 chainsaw and 2 pools"-> "3 glasses of water"...

"""
import unittest
from typing import Any, Callable, Tuple


def hydrate(drink_string: str) -> str:
    """
    Определяет кол-во стаканов воды, которые нужно выпить.
    """
    return f'{(x := sum(int(x[0]) for x in drink_string.replace(" and", ",").split(", ")))} glass{["es", ""][x == 1]} of water'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(hydrate, (
        ("1 beer", "1 glass of water"),
        ("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer", "10 glasses of water"),
    ))
