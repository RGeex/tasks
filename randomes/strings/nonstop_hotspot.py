"""
Задача

Выпущен новый «хакерский» телефон, способный подключаться к любой сети Wi-Fi на любом расстоянии,
при условии отсутствия препятствий между точкой доступа и телефоном. По заданной строке вернуть
количество точек доступа Wi-Fi, к которым я могу подключиться.

    Телефон представлен как P.
    Точка доступа представлена ​​как *.
    Препятствие представлено как #Вы не сможете получить доступ к точке доступа, если она
    находится за одним из этих препятствий.

Примеры

nonstop_hotspot("*   P  *   *") ➞ 3
# No obstructions

nonstop_hotspot("*  * #  * P # * #") ➞ 1
# Only one wifi available before obstructions

nonstop_hotspot("***#P#***") ➞ 0
# No access due to obstructions
"""
import typing
import unittest
import re


def nonstop_hotspot(area: str) -> int:
    """
    Определяет к сколько точкам wi-fi может подключиться пользователь.
    """
    return re.search(r'#?([^#]*P[^#]*)#?', area).group(1).count('*')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(nonstop_hotspot, (
        ('*   P  *   *', 3),
        ('*  * #  * P # * #', 1),
        ('***#P#***', 0),
        ('#P#', 0),
        ('P', 0),
        ('P       #', 0),
        ('P     *  # *', 1),
        ('*   # * P', 1),
        ('# *****  **  P     ** #    ', 9),
    ))
