"""
Вам необходимо написать функцию, которая возвращает первый неповторяющийся символ в заданной строке.

Если все символы уникальны, вернуть первый символ строки.
Если уникального символа нет, вернуть nullв JS или Java, Noneна языке питона, '\0'в С.

Можно предположить, что входная строка всегда имеет ненулевую длину.
Примеры

"test"   returns "e"
"teeter" returns "r"
"trend"  returns "t" (all the characters are unique)
"aabbcc" returns null (all the characters are repeated)
"""
import typing
import unittest


def first_non_repeated(st: str) -> str | None:
    """
    Возвращает первый не повторяющийся символ строки или None.
    """
    return next((x for x in st if st.count(x) == 1), None)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(first_non_repeated, (
        ("test", 'e'),
        ("teeter", 'r'),
        ("1122321235121222", '5'),
    ))
