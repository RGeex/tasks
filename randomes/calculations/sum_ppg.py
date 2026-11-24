"""
Эта ката задумана как небольшое испытание для моих учеников.

Задание All Star Code Challenge #1

Напишите функцию, которая принимает два объекта/структуры/хеша/словаря/класса игрока
НБА и суммирует их очки за игру.

Примеры:
iverson = { 'team': '76ers', 'ppg': 11.2 }
jordan =  { 'team': 'bulls', 'ppg': 20.2 }
sum_ppg(iverson, jordan) # => 31.4
"""
import unittest
from typing import Any, Callable, Dict, Tuple


def sum_ppg(player_one: Dict, player_two: Dict) -> float:
    """
    Определяет общий счет 2-х игроков.
    """
    return sum(x["ppg"] for x in [player_one, player_two])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_ppg, (
        (({ 'team': '76ers', 'ppg': 11.2 }, { 'team': 'bulls', 'ppg': 20.2 }), 31.4),
    ))
