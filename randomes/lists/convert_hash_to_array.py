"""
Преобразовать хеш в массив. Ничего больше, ничего меньше.

{name: 'Jeremy', age: 24, role: 'Software Engineer'}

следует преобразовать в

[["age", 24], ["name", "Jeremy"], ["role", "Software Engineer"]]
"""
import unittest
from typing import Any, Callable, Tuple


def convert_hash_to_array(dct: dict[str, Any]) -> list[list[Any]]:
    """
    Конветирует словарь в отсортированный список списков.
    """
    return sorted(map(list, dct.items()))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(convert_hash_to_array, (
        ({"name": "Jeremy"}, [["name", "Jeremy"]]),
        ({"name": "Jeremy", "age": 24}, [["age", 24], ["name", "Jeremy"]]),
        ({"name": "Jeremy", "age": 24, "role": "Software Engineer"}, [["age", 24], ["name", "Jeremy"], ["role", "Software Engineer"]]),
        ({"product": "CodeWars", "power_level_over": 9000}, [["power_level_over", 9000], ["product", "CodeWars"]]),
        ({}, []),
    ))
