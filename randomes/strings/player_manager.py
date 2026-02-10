"""
Вы — Мастер Подземелий в публичной игре по D&D в местном магазине комиксов,
и в последнее время у вас возникли проблемы с упорядочиванием информации о ваших игроках,
поэтому вы решили написать небольшой код, чтобы помочь вам в этом!

Цель этого кода — создать массив объектов, который будет хранить имя игрока и его контактный номер,
полученные из заданной строки.

Если переданный аргумент является пустой строкой, метод должен возвращать пустой массив. nil/ None/ null.
Примеры

player_manager("John Doe, 8167238327, Jane Doe, 8163723827") returns [{"player": "John Doe",
"contact": 8167238327}, {"player": "Jane Doe", "contact": 8163723827}]
player_manager(None) returns []
player_manager("")   returns []

playerManager("John Doe, 8167238327, Jane Doe, 8163723827") returns [{player: "John Doe", contact: 8167238327}, {player: "Jane Doe", contact: 8163723827}]
playerManager(null) returns []
playerManager("")   returns []

Вперед!
"""
import unittest
from typing import Any, Callable, Dict, List, Optional, Tuple


def player_manager(players: str) -> Optional[List[Dict[str, str | int]]]:
    """
    Из переданной строки создает массив данных.
    """
    if players and isinstance(players, str):
        lst = [int(x) if x.isdigit() else x for x in players.split(', ')]
        return [dict(zip(('player', 'contact'), lst[i:i + 2])) for i in range(0, len(lst), 2)]
    return []


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(player_manager, (
        ("John Doe, 8167238327, Jane Doe, 8163723827", [{"player": "John Doe", "contact": 8167238327}, {"player": "Jane Doe", "contact": 8163723827}]),
        ("", []),
    ))
