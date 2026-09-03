"""
Тимми пытается определить, team 1выиграла ли его команда игру, но его reduceфункция доставляет ему некоторые проблемы!

    t1s = reduce(lambda a, b: a ^ b, t1, 0)
    t2s = reduce(lambda a, b: a & b, t2, 0)
    return t1s > t2s

У каждой команды есть массив/список, содержащий до трех целых чисел, представляющих полученные ими баллы. У команды может быть меньше трех баллов.

Команда 1 побеждает, если сумма её очков превышает сумму очков команды 2.

Вернитесь, trueесли команда 1 победит или falseв противном случае!
"""
import unittest
from typing import Any, Callable, List, Tuple


def calculate_total(t1: List[int], t2: List[int]) -> bool:
    """
    Определяет победила ли команда 1.
    """
    return sum(t1) > sum(t2)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(calculate_total, (
        (([1, 2, 2], [1, 0, 0]), True),
        (([6, 45, 1], [1, 55, 0]), False),
        (([57, 2, 1], []), True),
        (([], [3, 4, 3]), False),
        (([], []), False),
    ))
