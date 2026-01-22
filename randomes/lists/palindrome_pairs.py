"""
Дан список уникальных слов. Найдите все пары различных индексов (i, j) в данном списке,
так чтобы конкатенация этих двух слов, т.е. words[i] + words[j], являлась палиндромом.

Примеры:

["bat", "tab", "cat"] # [[0, 1], [1, 0]]
["dog", "cow", "tap", "god", "pat"] # [[0, 3], [2, 4], [3, 0], [4, 2]]
["abcd", "dcba", "lls", "s", "sssll"] # [[0, 1], [1, 0], [2, 4], [3, 2]]

Входные данные, не являющиеся строками, следует преобразовывать в строки.

Возвращает массив массивов, содержащих пары различных индексов, образующих палиндромы.
Пары должны быть возвращены в том порядке, в котором они появляются в исходном списке.

"""
import unittest
from typing import Any, Callable, List, Tuple


def palindrome_pairs(words: List[Any]) -> List[List[int]]:
    """
    Поиск индексов пар палиндромов.
    """
    res, words = [], list(map(str, words))
    for i, st1 in enumerate(words):
        for j, st2 in enumerate(words):
            if i != j and (x := st1 + st2) == x[::-1]:
                res.append([i, j])
    return res


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(palindrome_pairs, (
        (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
        (["dog", "cow", "tap", "god", "pat"], [[0, 3], [2, 4], [3, 0], [4, 2]]),
        (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [2, 4], [3, 2]]),
    ))
