"""
Мне нужно вывести несколько положительных целых чисел так, чтобы все они
занимали одинаковую ширину, добавляя минимальное количество начальных нулей.
К наибольшему целому числу начальные нули не добавляются.

Например, дано 1, 23, 2, 17, 102, Я хочу распечатать эти цифры следующим
образом:

001
023
002
017
102

Напишите функцию, которая принимает переменное количество целых чисел и
возвращает строку для печати.

"""
import typing
import unittest


def print_nums(*args: int) -> str:
    # return args
    # return [x for x in args]
    # return [(x, len(str(max(*args)))) for x in args]
    return '\n'.join(f'{x:0>{len(str(max(args)))}}' for x in args)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(print_nums, (
        (tuple(), ''),
        ((2,), '2'),
        ((1, 12, 34), '01\n12\n34'),
        ((1009, 2), '1009\n0002'),
        ((1, 1, 13), '01\n01\n13'),
        (tuple(range(2, 10, 3)), '2\n5\n8'),
        (tuple(i ** 3 for i in range(1, 4)), '01\n08\n27'),
    ))
