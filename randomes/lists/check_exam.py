"""
Первый входной массив содержит ключ к правильным ответам на экзаменационный вопрос,
например ["a", "a", "b", "d"], . Второй массив содержит ответы, представленные студентом.

Оба массива не пусты и имеют одинаковую длину. Верните оценку для этого массива ответов,
указав +4для каждого правильного ответа, -1для каждого неправильного ответа и +0
для каждого пустого ответа пустую строку (в C используется пробел).

Если значение меньше 0, вернуть 0.

Например:

    Correct answer    |    Student's answer   |   Result         
 ---------------------|-----------------------|-----------
 ["a", "a", "b", "b"]   ["a", "c", "b", "d"]  →     6
 ["a", "a", "c", "b"]   ["a", "a", "b", "" ]  →     7
 ["a", "a", "b", "c"]   ["a", "a", "b", "c"]  →     16
 ["b", "c", "b", "a"]   ["" , "a", "a", "c"]  →     0
"""
import unittest
from typing import Any, Callable, List, Tuple


def check_exam(arr1: List[str], arr2: List[str]) -> int:
    """
    Определяет балл набранный студентом.
    """
    return x if (x := sum([-1, 4][a == b] if b else 0 for a, b in zip(arr1, arr2))) > 0 else 0


def check_exam_2(arr1: List[str], arr2: List[str]) -> int:
    """
    Определяет балл набранный студентом.
    """
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(check_exam, (
        ((["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6),
        ((["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7),
        ((["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16),
        ((["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0),
    ))
    test(check_exam_2, (
        ((["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6),
        ((["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7),
        ((["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16),
        ((["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0),
    ))
