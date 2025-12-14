"""
Один из традиционных методов определения победителя в матче по го называется подсчетом очков
по камням. Этот метод имеет некоторые недостатки, но с алгоритмической точки зрения он
является самым простым. Поэтому мы начнем именно с него.

Входными данными для головоломки является двумерная коллекция, представляющая собой игровое
поле для игры в го, например:

board = [
    [W, W, W, B, B, B],
    [W, W, W, W, B, B],
    [W, W, W, B, B, B],
    [W, X, W, B, B, B],
    [X, W, B, B, B, B],
    [W, W, B, X, B, X]
]

Bизображают поля с черными камнями, Wизображают поля с белыми камнями, и XПредставьте пустые поля.
Ваша задача — определить победившую сторону, то есть сторону, у которой больше камней на доске.
Затем верните либо W или Bи количество камней на стороне в виде кортежа в зависимости от того,
у какой стороны больше камней на доске. В случае ничьей, вернуть значение. Tи количество камней
с одной стороны в виде кортежа. Пустые поля в этом методе определения победителя не учитываются.
Следовательно, их можно игнорировать.

В приведенном примере, Bна доске 17 камней, тогда как WУ них всего 15. Следовательно, чёрные
победили, и ("B", 17)следует вернуть.

Обратите внимание, что размер доски может варьироваться, но как минимум она должна быть размером
3х3!
"""
import unittest
from typing import Any, Callable, Tuple


def determine_winner(board: list[list[str]]) -> tuple[str, int]:
    """
    Определяет победителя на доске, по кол-ву камней.
    """
    data = dict.fromkeys('BW', 0)
    for line in board:
        for x in line:
            if x in data:
                data[x] += 1
    (a, b), (c, d) = sorted(data.items(), key=lambda x: x[1])
    return (a, b) if b > d else (f'{c}T'[b == d], d)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(determine_winner, (
        ([["W", "W", "W", "B", "B", "B"],
          ["W", "W", "W", "W", "B", "B"],
          ["W", "W", "W", "B", "B", "B"],
          ["W", "X", "W", "B", "B", "B"],
          ["X", "W", "B", "B", "B", "B"],
          ["W", "W", "B", "X", "B", "X"]], ("B", 17)),
    ))
