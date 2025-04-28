"""
Вам дана строка слов и цифр. Извлеките выражение, включающее:

    оператор: либо сложение ( "gains") или вычитание ( "loses")
    два числа, над которыми мы работаем

Верните результат расчета.

Примечания:

    "loses" и "gains"единственные два слова, описывающие операторов
    Никаких фруктовых долгов и надкусанных яблок = Числа целые и не отрицательные.

Примеры

"Panda has 48 apples and loses 4"  -->  44
"Jerry has 34 apples and gains 6"  -->  40

Должно получиться неплохое маленькое ката для вас :)

"""
import typing
import unittest


def calculate(st: str) -> int:
    """
    Производит вычисления в строке.
    """
    return eval(''.join({'gains': '+', 'loses': '-'}.get(x, ['', x][x.isdigit()]) for x in st.split()))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(calculate, (
        ("Panda has 48 apples and loses 4", 44),
        ("Jerry has 34 apples and gains 6", 40),
        ("Tom has 20 apples and gains 15", 35),
        ("Fred has 110 bananas and loses 50", 60),
        ("Pippi has 20 tunas and gains 0", 20),
    ))
