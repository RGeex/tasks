"""
Подсчитайте количество вхождений каждого символа и верните результат в виде списка кортежей в
порядке их появления. В случае пустого вывода верните пустой список.

Для получения точной информации о реализации структуры данных в зависимости от используемого
языка программирования обратитесь к настройкам решения.

Пример:

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]

"""
import unittest
from typing import Any, Callable, List, Tuple
from collections import Counter


def ordered_count(inp: str) -> List[Tuple[str, int]]:
    """
    Подсчитывает вхождение каждого символа строки.
    """
    return list(Counter(inp).items())


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(ordered_count, (
        ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
        ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
    ))
