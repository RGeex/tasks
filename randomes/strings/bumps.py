"""
Ваша машина старая, она легко ломается. Амортизаторы вышли из строя, и вы думаете,
что она выдержит еще около 15 ударов, прежде чем окончательно умрет.

К сожалению для вас, ваша дорога очень ухабистая! Учитывая строку, показывающую либо
ровную дорогу ( _) или шишки ( n). Если вы смогли безопасно добраться домой,
столкнувшись с 15 bumps or less, возвращаться Woohoo!, в противном случае возврат Car Dead
"""
import typing
import unittest


def bumps(road: str) -> str:
    """
    Проверяет, доедет ли машина до дома, учитывая дорогу.
    """
    return 'Woohoo!' if road.count('n') < 16 else 'Car Dead'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(bumps, (
        ("n", "Woohoo!"),
        ("__nn_nnnn__n_n___n____nn__nnn", "Woohoo!"),
        ("nnn_n__n_n___nnnnn___n__nnn__", "Woohoo!"),
        ("_nnnnnnn_n__n______nn__nn_nnn", "Car Dead"),
        ("______n___n_", "Woohoo!"),
        ("nnnnnnnnnnnnnnnnnnnnn", "Car Dead"),
    ))
