"""
Сколько дней мы будем находиться в зарубежной стране в качестве наших представителей?

Мои коллеги совершают деловые поездки в зарубежные страны. Нам нужно определить количество дней,
в течение которых наша компания представлена ​​в этой стране. Каждый день, когда один или несколько
коллег находятся в стране, считается днем, когда компания представлена. Один день не может
учитываться более чем один день.

Напишите функцию, которая принимает список пар и возвращает количество дней, в течение которых
компания представлена ​​в зарубежной стране. Первая цифра пары — это номер дня прибытия,
а вторая — номер дня отъезда, например, 1 января — это число 1, а 31 декабря — 365.

Пример:

days_represented([[10,17],[200,207]])

Возвращает 16, потому что есть две поездки по 8 дней, сумма которых составляет 16.

Удачного программирования! Можете оценить это задание, если хотите ;-)

"""
import unittest
from typing import Any, Callable, List, Tuple


def days_represented(trips: List[List[int]]) -> int:
    """
    Подсчитывает кол-во дней, когда компания является предствителем.
    """
    return len(set.union(*[set(range(a, b + 1)) for a, b in trips]))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(days_represented, (
        ([[10, 15], [25, 35]], 17),
        ([[2, 8], [220, 229], [10, 16]], 24),
    ))
