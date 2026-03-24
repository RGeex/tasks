"""

Перед вами находятся nnn куч Однодолларовые купюры.

Ваш помощник будет выполнять следующие операции до тех пор, пока одна из куч не опустеет:

    Вычислите наибольший общий делитель сумм денег в стопках.
    Выньте из каждой стопки купюр указанную сумму и отдайте её себе.

Вы хотите узнать: когда одна из куч будет опустошена, сколько денег вы получите в общей сложности?

Напишите функцию calcчто позволит вам вернуть всю сумму, полученную вами по завершении всех операций.

Вам будет предоставлен массив размеров. nnn — количество 1 долларовые купюры. В каждой стопке лежат
Примеры

calc([1, 2, 3, 4, 5]) = 5
calc([3, 4]) = 6

    Все числа в массиве являются положительными целыми числами.

"""
import unittest
from typing import Any, Callable, List, Tuple


def calc(numberss: List[int]) -> int:
    """
    Определяет кол-во полученных денег по заданному алгоритму.
    """
    return len(numberss) * min(numberss)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(calc, (
        ([1, 2, 3, 4, 5], 5),
        ([3, 4], 6),
    ))
