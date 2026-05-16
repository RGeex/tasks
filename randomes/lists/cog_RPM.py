"""
Ключевые слова задания

Вам дан список шестеренок зубчатой ​​передачи.

Каждый элемент представляет собой количество зубьев данной шестерни.

например [100, 75] означает

    Первая шестерня имеет 100 зубьев.
    Вторая шестерня имеет 75 зубьев.

Если первая шестерня вращается по часовой стрелке со скоростью 1 об/мин, то какова частота вращения последней шестерни?

(для вращения против часовой стрелки используйте отрицательные числа)
Примечания

    Нет двух шестеренок с одним и тем же валом.

"""
import unittest
from typing import Any, Callable, List, Tuple


def cog_RPM(cogs: List[int]) -> float:
    """
    Определяет частоту вращения последней шестерни.
    """
    return cogs[0] / cogs[-1] * (len(cogs) % 2 or -1)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(cog_RPM, (
        ([100, 75], -4/3),
        ([100, 100, 75], 4/3),
        ([100, 100], -1),
        ([100, 100, 100], 1),
        ([100, 100, 100, 100], -1),
    ))
