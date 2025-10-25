"""
Портфель имеет четырёхзначный роликовый замок . Каждая цифра — это число из 0-9который можно катить как вперед, так и назад.

Создайте функцию, которая возвращает наименьшее количество поворотов, необходимых для перевода замка из текущей комбинации в целевую. Один поворот эквивалентен увеличению числа на единицу.

Для иллюстрации:

    текущий замок : 4089
    захват цели : 5672

Какое минимальное количество поворотов необходимо для преобразования 4089 к 5672?

4 ➞ 5
4 ➞ 5  // Forward Turns: 1 <- Min
4 ➞ 3 ➞ 2 ➞ 1 ➞ 0 ➞ 9 ➞ 8 ➞ 7 ➞ 6 ➞ 5  // Backward Turns: 9

0 ➞ 6
0 ➞ 1 ➞ 2 ➞ 3 ➞ 4 ➞ 5 ➞ 6  // Forward Turns: 6
0 ➞ 9 ➞ 8 ➞ 7 ➞ 6  // Backward Turns: 4  <- Min

8 ➞ 7
8 ➞ 9 ➞ 0 ➞ 1 ➞ 2 ➞ 3 ➞ 4 ➞ 5 ➞ 6 ➞ 7  // Forward Turns: 9
8 ➞ 7  // Backward Turns: 1  <- Min

9 ➞ 2
9 ➞ 0 ➞ 1 ➞ 2  // Forward Turns: 3  <- Min
9 ➞ 8 ➞ 7 ➞ 6 ➞ 5 ➞ 4 ➞ 3 ➞ 2  // Backward Turns: 7

Занимает 1 + 4 + 1 + 3 = 9минимальное количество оборотов, чтобы сменить замок с 4089 к 5672.
Примечания

    Оба замка имеют строковый формат.
    А 9катится вперед к 0, и 0катится назад к 9.



"""
import typing
import unittest


def min_turns(current: str, target: str) -> int:
    """
    Определяет минимальное кол-во оборотов замка для набора кода из заданной позиции.
    """
    return sum(min(10 - max(a, b) + min(a, b), abs(a - b)) for a, b in zip(*[map(int, x) for x in (current, target)]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(min_turns, (
        (("4089", "5672"), 9),
        (("1732", "4444"), 9),
        (("7109", "2332"), 13),
        (("2391", "4984"), 10),
        (("1234", "3456"), 8),
        (("1111", "1100"), 2),
        (("1111", "0000"), 4),
        (("0000", "9999"), 4),
    ))
