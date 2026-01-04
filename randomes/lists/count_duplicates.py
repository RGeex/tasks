"""
Даны несколько списков ( name, age, height), каждый размером n:

Каждая запись содержит одно имя, один возраст и один рост. Атрибуты,
соответствующие каждой записи, определяются индексом соответствующего списка.
Например, первая запись состоит из первых элементов каждого списка, вторая запись —
из вторых элементов каждого списка и т. д.

Дублирующаяся запись — это запись, в которой имя, возраст и рост совпадают.

Напишите функцию, которая принимает атрибуты каждой записи и возвращает целое число,
обозначающее количество дубликатов. При наличии набора дубликатов исходная запись не
должна считаться дубликатом.

"""
import unittest
from typing import Any, Callable, List, Tuple


def count_duplicates(name: List[str | int], age: List[str | int], height: List[str | int]) -> int:
    """
    Определяет кол-во дубликатов.
    """
    return len(name) - len(set(zip(name, age, height)))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count_duplicates, (
        ((['John', 'Beth', 'Beth', 'Bill'], [37, 23, 30, 46], [183, 170, 165, 175]), 0),
        ((['John', 'Beth', 'Beth', 'Beth', 'Bill'], [37, 23, 23, 23, 46], [183, 170, 170, 170, 175]), 2),
        ((['Jack', 'Ben', 'Jack', 'Ben', 'Jack', 'Jack'], [25, 25, 34, 25, 25, 34], [180, 180, 200, 180, 180, 200]), 3),
    ))
