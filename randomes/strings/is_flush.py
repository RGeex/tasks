"""
Определите, является ли покерная комбинация флешевой, то есть являются ли пять карт одной масти .

Вашей функции будет передан список/массив из 5 строк, каждая из которых представляет собой покерную
карту в формате "5H"(5 червей), означающая достоинство карты, за которым следует начальная буква ее
масти ( Hуши, SПэдди, Dалмазы или C(любс). Джокеры не включены.

Ваша функция должна возвращать trueесли рука — флеш, false в противном случае.

Возможные значения карт: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
Примеры

["AS", "3S", "9S", "KS", "4S"]  ==> true

["AD", "4S", "7H", "KS", "10S"] ==> false
"""
import typing
import unittest


def is_flush(cards: list[str]) -> bool:
    """
    Определяет, является л переданная комбинация катр флешевой.
    """
    return len({x[-1] for x in cards}) == 1


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_flush, (
        (["AS", "3S", "9S", "KS", "4S"], True),
        (["AD", "4S", "7H", "KC", "5S"], False),
        (["AD", "4S", "10H", "KC", "5S"], False),
        (["QD", "4D", "10D", "KD", "5D"], True),
    ))
