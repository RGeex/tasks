"""
Задача

Напишите функцию, которая проверяет, образуют ли два неотрицательных целых числа "взаимосвязанную двоичную пару".
Блокировка?

    Числа могут быть взаимосвязаны, если их двоичное представление не имеет 1находится в том же месте
    Сравнения проводятся по битовой позиции, справа налево (см. примеры ниже).
    Когда представления имеют разную длину, несовпадающие крайние левые биты игнорируются.

Примеры

    a = 9, b = 4

    Наложение изображений показывает, как они могут переплетаться.

     9    1001
     4     100

    Здесь нет 1's' занимают любую позицию, поэтому функция возвращает true.

    a = 3, b = 6

    Эти представления не взаимосвязаны.

     3      11
     6     110

    Обнаружив, что у них обоих есть 1в той же позиции функция возвращает false.

Вход

Два неотрицательных целых числа.
Выход

Логический true или false являются ли эти целые числа взаимоблокируемыми.
"""
import unittest
from typing import Any, Callable, Tuple


def interlockable(a: int, b: int) -> bool:
    """
    Определяет, являются ли эти целые числа взаимоблокируемыми.
    """
    return not a & b


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(interlockable, (
        ((9, 4),  True ),
        ((3, 6), False ),
        ((2, 5),  True ),                            
        ((7, 1), False ),
        ((0, 8),  True ),
    ))
