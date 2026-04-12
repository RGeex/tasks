"""
Задача

Напишите функцию, которая принимает два аргумента: (1) текущую руку игрока и (2) текущую открытую
карту на столе. Функция должна возвращать Trueесли игрок может совершить результативное действие,
или Falseесли игроку необходимо взять карту из колоды.

Игрок может сделать ход, если у него есть карта:

    это тот же цвет, что и открытая карта.
    ИЛИ это то же самое число, что и на открытой карте.

Формат карт

    Цвета всегда пишутся строчными буквами: «красный», «жёлтый», «синий», «зелёный».
    Числа — это цифры от 0 до 9.
    Каждая карточка оформлена в виде "цифры цвета", например, "синий 5".

Примечания

    Возвращаться Falseесли у игрока нет карт на руках (пустой список).
    В этой колоде нет специальных карт или джокеров.

Примеры

["yellow 3", "yellow 7", "blue 8", "red 9", "red 2"], "red 1" ➞ True  # "red 9" or "red 2"
["yellow 3", "yellow 7"], "blue 7"                   ➞ True  # "yellow 7"
["yellow 3", "yellow 5", "red 8"], "red 2"           ➞ True  # "red 8"
["yellow 3", "yellow 5", "red 8"], "blue 5"          ➞ True  # "yellow 5"
["yellow 3", "blue 5", "red 8", "red 9"], "green 4"  ➞ False
["yellow 3", "red 8"], "green 2"                     ➞ False

"""
import unittest
from typing import Any, Callable, List, Tuple


def can_play(hand: List[str], face_up: str) -> bool:
    """
    Определяет, может ли игрок сделать ход.
    """
    return next((True for cur in hand if any(len(set(x)) == 1 for x in zip(cur.split(), face_up.split()))), False)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(can_play, (
        ((['yellow 3', 'yellow 5', 'red 8'], 'red 2'), True),
        ((['yellow 3', 'yellow 5', 'red 8'], 'blue 5'), True),
        ((['yellow 3', 'blue 5', 'red 8', 'red 9'], 'green 4'), False),
        ((['yellow 3', 'red 8'], 'green 2'), False),
        ((['yellow 5', 'yellow 8', 'red 0', 'blue 0', 'green 4'], 'green 2'), True),
        (([], 'green 2'), False),
        ((['red 2'], 'red 0'), True),
        ((['red 2', 'red 8', 'red 5'], 'blue 1'), False),
    ))
