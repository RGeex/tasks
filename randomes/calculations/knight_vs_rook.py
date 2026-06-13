"""
Конь против Ладьи

Если вы не знакомы с шахматами, вы можете узнать о них больше здесь .

Вам будут предоставлены позиции коня и ладьи на доске. Реализуйте функцию, которая определяет,
какая фигура может взять другую:

    "Rook"если ладья возьмет коня
    "Knight"если конь возьмет ладью
    "None" в противном случае

Ознакомьтесь с тестовыми примерами и удачного кодирования! :)


"""
import unittest
from typing import Any, Callable, Tuple


def knight_vs_rook(knight: Tuple[int, str], rook: Tuple[int, str]) -> str:
    """
    Определяет победителя между ладьёй и конем в шахматах.
    """
    (a, b), (c, d) = knight, rook
    return {a == c or b == d: 'Rook', (x := abs(a - c)) + abs(ord(b) - ord(d)) == 3 and x in (1, 2): 'Knight'}.get(1, 'None')


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(knight_vs_rook, (
        (((6,'D'), (4,'C')),  'Knight'),
        (((2,'B'), (2,'G')),  'Rook'),
        (((7,'B'), (2,'F')),  'None'),
    ))
