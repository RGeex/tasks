"""
Изменить каждую букву в заданной строке на следующую букву в алфавите.
Функция принимает один параметр s (нить).

Примечания:

    Пробелы и специальные символы должны остаться прежними.
    Заглавные буквы следует переносить таким же образом, но
    при этом они должны оставаться заглавными.

Примеры

"Hello"               -->  "Ifmmp"
"What is your name?"  -->  "Xibu jt zpvs obnf?"
"zoo"                 -->  "app"
"zzZAaa"              -->  "aaABbb"
"""
import typing
import unittest
from string import ascii_lowercase as low, ascii_uppercase as upp


def next_letter(st: str) -> str:
    """
    Производит сдвиг символов на 1 вперед.
    """
    return st.translate(str.maketrans(low + upp, low[1:] + low[:1] + upp[1:] + upp[:1]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(next_letter, (
        ("Hello", "Ifmmp"),
        ("What is your name?", "Xibu jt zpvs obnf?"),
        ("zOo", "aPp"),
    ))
