"""
JavaScript предоставляет встроенный метод parseInt.

Его можно использовать следующим образом:

    "10"возвращается 10
    "10 apples"также возвращается 10

Мы хотели бы, чтобы он вернулся. "NaN"(в виде строки) для второго случая,
поскольку входная строка не является допустимым числом.

Вам предлагается написать функцию со следующими правилами:

    Преобразование должно выполняться, если заданная строка содержит только одно целочисленное
    значение (и, возможно, пробелы — включая табуляции, переводы строк... — на обоих концах)
    Для всех остальных строк (включая те, которые представляют значения с плавающей точкой) он
    должен возвращать NaN
    Следует предположить, что все числа не имеют знака и записаны в десятичной системе счисления.


"""
import typing
import unittest


def my_parse_int(st: str) -> int | str:
    """
    Преобразует строку в число, если в ней содержатся только цифр и пробелы.
    """
    return int(x) if (x := st.strip()).isdigit() else 'NaN'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(my_parse_int, (
        ("1", 1),
        ("  1 ", 1),
        ("08", 8),
        ("5 friends", "NaN"),
        ("16.5", "NaN"),
    ))
