"""
Вы устраиваете барбекю, и после него у вас остается мусор, который нужно сдать на переработку.

Есть 3 контейнера для раздельного сбора мусора: красный — пластик, зеленый — стекло, синий — картон.

Вам нужно отсортировать мусор по материалу и вернуть количество предметов в каждой коробке в виде массива (или кортежа в Python):

[plastic, glass, card]

Тип материала можно определить по знаку номинала изделия:

    Пластик : значение > 0
    Стекло : значение < 0
    Карта : значение = 0

Пример

rubbish = [5, -9, 0, 6, -84, -95, 15]
// Plastic = 3, Glass = 3, Card = 1
// Output: [3, 3, 1]


"""
import unittest
from typing import Any, Callable, List, Tuple


def recycle_me(rubbish: List[int]) -> Tuple[int]:
    """
    Сортирует мусор.
    """
    return tuple([sum(map(int, x)) for x in zip(*[[['010', '100'][x > 0], '001'][not x] for x in rubbish])]) or (0, 0, 0)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(recycle_me, (
        ([5, -9, 0, 6, -84, -95, 15], (3, 3, 1)),
        ([45, -26, -4, -66, -84, -38, 14], (2, 5, 0)),
    ))
