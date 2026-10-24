"""
Вам даны две строки. Одним ходом вы можете выбрать любую из них и
удалить первый (т.е. самый левый) символ.

Например:

Применив операцию перемещения к строке "where", получаем строку "here".
Применив операцию перемещения к строке "a", получаем пустую строку "".
Реализуйте функцию, которая вычисляет минимальное количество перемещений,
необходимых для того, чтобы заданные строки стали равными.

Примечания
Обе строки состоят из строчных латинских букв.
Если строка уже пуста, вы не сможете выполнить больше операций удаления.
"""
import unittest
from typing import Any, Callable, Tuple


def shift_left(a: str, b: str) -> int:
    """
    Определяет, кол-во букв которые следует удалить, что бы слова стали одинаковыми.
    """
    return min(i+j for i in range(len(a)+1) for j in range(len(b)+1) if a[i:] == b[j:])


def shift_left_2(a: str, b: str, n: int = 0) -> int:
    """
    Определяет, кол-во букв которые следует удалить, что бы слова стали одинаковыми.
    """
    if a == b:
        return n
    elif len(a) > len(b):
        return shift_left_2(a[1:], b, n + 1)
    else:
        return shift_left_2(a, b[1:], n + 1)


def shift_left_3(a: str, b: str, n: int = 0) -> int:
    """
    Определяет, кол-во букв которые следует удалить, что бы слова стали одинаковыми.
    """
    r = len(a) + len(b)
    for i in range(-1, -min(len(a), len(b)) - 1, -1):
        if a[i] != b[i]:
            break
        r -= 2
    return r


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(shift_left, (
        (("test", "west"), 2),
        (("test", "yes"), 7),
        (("b", "ab"), 1),
    ))
    test(shift_left_2, (
        (("test", "west"), 2),
        (("test", "yes"), 7),
        (("b", "ab"), 1),
    ))
    test(shift_left_3, (
        (("test", "west"), 2),
        (("test", "yes"), 7),
        (("b", "ab"), 1),
    ))
