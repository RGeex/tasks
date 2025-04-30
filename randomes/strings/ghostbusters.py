"""
О нет! Говорят, что город заполонили призраки. Ваша задача — избавиться от них и спасти положение!

В этом ката строки символизируют здания, а пробелы внутри этих строк символизируют призраков.

Так чего же вы ждете? Верните здание (строку) без каких-либо призраков (пробелов)!

Пример:

"Sky scra per" -> "Skyscraper"

Если в здании нет привидений, вернуть строку:

"You just wanted my autograph didn't you?"


"""
import typing
import unittest


def ghostbusters(building: str) -> str:
    """
    Убирает всех призраков из здания, если их нет сообщает об этом.
    """
    return building.replace(' ', '') if building.count(' ') else "You just wanted my autograph didn't you?"


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(ghostbusters, (
        ("Factor y", "Factory"),
        ("O  f fi ce", "Office"),
        ("BusStation", "You just wanted my autograph didn't you?"),
        ("Suite ", "Suite"),
        (" H ou se", "House"),
        ("YourHouse", "You just wanted my autograph didn't you?"),
        ("H o t e l ", "Hotel"),

    ))
