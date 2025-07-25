"""
У вас есть строка чисел; начиная с третьего числа, каждое число является результатом операции,
выполненной с использованием двух предыдущих чисел.

Завершите функцию, которая возвращает строку операций по порядку, разделенных запятой и пробелом,
например: "subtraction, subtraction, addition"

Доступные операции (в порядке предпочтения):

1) addition
2) subtraction
3) multiplication
4) division

Примечания:

    Все входные данные верны.
    Количество чисел во входной строке >= 3
    Для такого случая как "2 2 4"- если возможны несколько вариантов - выберите первую возможную
    операцию из списка (в данном случае "addition")
    Следует использовать целочисленное деление.

Пример

"9 4 5 20 25"  -->  "subtraction, multiplication, addition"

Потому что:

9 - 4 = 5   --> subtraction
4 * 5 = 20  --> multiplication
5 + 20 = 25 --> addition
"""
import typing
import unittest


def say_me_operations(string_numbers: str) -> str:
    """
    Определяет результирующую операцию между заданными числами.
    """
    lst, res = list(map(int, string_numbers.split())), []
    for i in range(len(lst) - 2):
        a, b, c = lst[i:i+3]
        res.append({b and a // b == c: 'division', a * b == c: 'multiplication', a - b == c: 'subtraction', a + b == c: 'addition'}.get(1, ''))
    return  ', '.join(res)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(say_me_operations, (
        ("1 2 3 5 8", "addition, addition, addition"),
        ("9 4 5 20 25", "subtraction, multiplication, addition"),
        ("10 2 5 -3 -15 12", "division, subtraction, multiplication, subtraction"),
        ("2 2 4", "addition"),
    ))
