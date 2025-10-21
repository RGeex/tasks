"""
Есть два типа зелий:

    Зелье выращивания: «А»
    Сжимающее зелье: «B».

    Если «А» следует сразу за цифрой, прибавьте к ней 1.
    Если «B» следует сразу за цифрой, вычтите 1 из цифры.

Создайте функцию, которая возвращает строку в соответствии с этими правилами,
удаляя зелья после их употребления.

Примеры

"3A78B51" ➞ "47751"
# 3 grows to 4, 8 shrinks to 7

"9A999B" ➞ "10998"
# First 9 grows to 10 and second 9 shrinks to 8

"6A123" ➞ "7123"
# 6 grows to 7

"567" ➞ "567"
# No change

Примечания

    Цифры, справа от которых нет зелья, следует оставить в покое.
    За цифрой всегда будет следовать ноль или ровно 1 зелье.
    В данной строке не будет 0.
"""
import typing
import unittest


def after_potion(s: str) -> str:
    """
    Подсчет результата, после всех выпитых зелий.
    """
    return ''.join([str(int(a) + {'A': 1, 'B': -1}.get(b, 0)) for a, b in zip(s, s[1:] + '0') if a.isdigit()])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(after_potion, (
        ("567", "567"),
        ("9999B", "9998"),
        ("9A123", "10123"),
        ("3A78B51", "47751"),
        ("1A2A3A4A", "2345"),
        ("9B8B7B6A", "8767"),
        ("9A9A9A9A", "10101010"),
    ))

