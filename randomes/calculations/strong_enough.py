"""
Вы были наняты правительством Японии для написания функции, которая проверяет,
достаточно ли прочно здание, чтобы выдержать имитированное землетрясение.

Здание рухнет, если магнитуда землетрясения превысит прочность здания.

Землетрясение представляется в виде двумерного массива. Каждый элемент внешнего массива
представляет собой ударную волну, а каждый элемент внутреннего массива — дрожание.
Магнитуда землетрясения определяется произведением значений его ударных волн.
Ударная волна равна сумме значений его дрожаний.

Пример землетрясения -->[[5,3,7],[3,3,1],[4,1,2]] ((5+3+7) * (3+3+1) * (4+1+2)) = 735

Первоначально здание имеет прочность 1000, но это значение подвержено экспоненциальному снижению
на 1% в год. Более подробную информацию об экспоненциальном снижении прочности можно
найти по этой ссылке: https://en.wikipedia.org/wiki/Exponential_decay

Учитывая землетрясение и возраст здания, напишите функцию, которая возвращает "Safe!",
если здание достаточно прочное, или "Needs Reinforcement!", если оно обрушится.
"""
import unittest
from typing import Any, Callable, Tuple
from functools import reduce
from operator import mul


def strong_enough(earthquake: list[list[int]], age: int) -> str:
    """
    Опрделят выстоит или обрушится здание после земятресения.
    """
    return ["Needs Reinforcement!", "Safe!"][reduce(mul, map(sum, earthquake)) < 1000 * (1 - 0.01) ** age]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(strong_enough, (
        (([[2, 3, 1], [3, 1, 1], [1, 1, 2]], 2), "Safe!"),
        (([[5, 8, 7], [3, 3, 1], [4, 1, 2]], 2), "Safe!"),
        (([[5, 8, 7], [3, 3, 1], [4, 1, 2]], 3), "Needs Reinforcement!"),
        (([[5, 1, 7], [1, 1, 1], [4, 1, 2]], 100), "Safe!"),
        (([[5, 1, 7], [1, 1, 7], [4, 1, 2]], 50), "Needs Reinforcement!"),
        (([[5, 8, 7], [1, 1, 1], [6, 6, 1]], 25), "Needs Reinforcement!"),
        (([[5, 8, 7], [1, 1, 1], [6, 6, 1]], 20), "Safe!"),
        (([[1, 8, 7], [1, 3, 1], [6, 2, 1]], 30), "Safe!"),
        (([[1, 1, 6], [1, 1, 10], [6, 10, 1]], 2), "Needs Reinforcement!"),
        (([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 325), "Safe!"),
    ))
