"""
Пройдите через мой green glass door.

Вы можете взять moon, но не тот sun.

Вы можете взять свой slippers, но не твой sandals.

Вы можете пройти через yelling, но не shouting.

Ты не можешь пробежать сквозь fast, но вы можете бежать с speed.

Вы можете взять sheet, но не твой blanket.

Вы можете носить свой glasses, но не твой contacts.

Вы разобрались? Хорошо! Тогда напишите программу, которая тоже разберется.

"""
import typing
import unittest


def step_through_with(st: str) -> bool:
    """
    поиск повторяющихся букв в слове стоящих подряд.
    """
    return not next((0 for a, b in zip(st, st[1:]) if a == b), 1)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(step_through_with, (
        ("moon", True),
        ("test", False),
        ("glasses", True),
        ("airplane", False),
        ("free", True),
        ("branch", False),
        ("aardvark", True),
    ))
