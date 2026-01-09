"""
В списке где-то спрятан «непристойный» номер. Найдите его индекс, если, конечно, у вас хватит сил!
Вход:

    Вы получите массив массивов (список списков).
    Каждый подмассив может содержать либо другой массив, либо одно число.
    На входе всегда будет как минимум один подмассив.
    В подмассивах будет скрыто только одно число.

Выход:

Возвращает индекс подмассива первого уровня, содержащего скрытое число.
Примеры:

[ [[[]]] , [[]], [], [], [[2]] ] -> индекс равен 4

[ [1] ] -> индекс равен 0

[ [], [8], [] , [] ] -> индекс равен 1
"""
import unittest
from typing import Any, Callable, List, Tuple


def naughty_number(arr: List[Any]) -> int:
    """
    Определяет под каким индексом есть список содержащий цифры.
    """
    def find_int(arr: List[Any]) -> List[int]:
        """
        На основе переданного списка определяет где внутри списка есть цифры.
        """
        return [1 if isinstance(x, int) else find_int(x)[0] for x in arr] or [0]
    return find_int(arr).index(1)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(naughty_number, (
        ([[[[]]], [[]], [], [], [[2]]], 4),
        ([[1]], 0),
        ([[], [8], [], []], 1),
        ([[[[[[[[[42]]]]]]]]], 0),
        ([[], [], [], [], [], [], [], [], [], [], [], [77]], 11),
        ([[[]], [[[[[]]]]], [], [[[[[[[[[]]]]]]]]], [[[]]], [[[[31]]]], [[]], []], 5),
        ([[1], [[[[]]]], [[]], [[[[[[[[[]]]]]]]]], []], 0),
    ))
