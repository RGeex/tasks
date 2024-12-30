"""
В некоторых странах бывшего Советского Союза существовало поверье о счастливых билетах.
Считалось, что любой транспортный билет приносит удачу, если сумма цифр в левой половине
его номера равна сумме цифр в правой половине. Вот примеры таких чисел:

003111    #             3 = 1 + 1 + 1
813372    #     8 + 1 + 3 = 3 + 7 + 2
17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle
number when adding the halves.
56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6

Такие билеты либо съедали после использования, либо собирали, чтобы похвастаться.

Ваша задача написать функцию luck_check(str), который возвращает true/True если аргумент
представляет собой строковое десятичное представление номера счастливого билета, или
false/False для всех остальных номеров. Он должен выдавать ошибки для пустых строк или строк,
которые не представляют собой десятичное число.
"""
import typing
from operator import eq


def luck_check(st: str) -> bool:
    """
    Определяет, является ли билет счастливым.
    """
    if isinstance(st, str) and st.isdigit():
        i, n = divmod(len(st), 2)
        return eq(*[sum(map(int, x)) for x in (st[:i], st[i + n:])])
    raise ValueError("Invalid type value should throw error.")


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        def test_case(self):
            try:
                self.assertEqual(func(key), val)
            except ValueError as error:
                self.assertEqual(str(error), val)
        return test_case

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(luck_check, (
        ('5555', True),
        ('003111', True),
        ('543970707', False),
        ('439924', False),
        ('943294329932', False),
        ('000000', True),
        ('454319', True),
        ('1233499943', False),
        ('935336', False),
        (lambda: luck_check('6F43E8'), "Invalid type value should throw error."),
        (lambda: luck_check('1234 '), "Invalid type value should throw error."),
        (lambda: luck_check('124-21'), "Invalid type value should throw error."),
        (lambda: luck_check('124X212'), "Invalid type value should throw error."),
    ))
