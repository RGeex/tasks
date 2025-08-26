"""
Сравните две строки, сравнив сумму их значений (код символа ASCII).

    Для сравнения считать все буквы заглавными.
    null/NULL/Nil/Noneследует рассматривать как пустые строки
    Если строка содержит символы, отличные от букв, то вся строка считается пустой.

Ваш метод должен возвращать true, если строки равны и falseесли они не равны.
Примеры:

"AD", "BC"  -> equal
"AD", "DD"  -> not equal
"gf", "FG"  -> equal
"zz1", ""   -> equal (both are considered empty)
"ZzZz", "ffPFF" -> equal
"kl", "lz"  -> not equal
null, ""    -> equal


"""
import typing
import unittest


def compare(s1: str | None, s2: str | None) -> bool:
    """
    Проверяет эквивалентность строк по сумме символов.
    """
    return not sum(sum(map(ord, x.upper())) * (i or -1) if x and x.isalpha() else 0 for i, x in enumerate((s1, s2)))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(compare, (
        (("AD", "BC"), True),
        (("AD", "DD"), False),
        (("gf", "FG"), True),
        (("Ad", "DD"), False),
        (("zz1", ""), True),
        (("ZzZz", "ffPFF"), True),
        (("kl", "lz"), False),
        ((None, ""), True),
        (("!!", "7476"), True),
        (("##", "1176"), True),
    ))
