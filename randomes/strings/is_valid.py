"""
Дана строка, определите, является ли она допустимым идентификатором.
Вот синтаксис допустимых идентификаторов:

    Каждый идентификатор должен содержать хотя бы один символ.
    Первый символ должен быть выбран из: буквы, подчеркивания или знака доллара.
    Первый символ не может быть цифрой.
    Остальные символы (кроме первого) могут быть из: буквы, цифры, подчеркивания
    или знака доллара. Другими словами, это может быть любой допустимый символ идентификатора.

Примеры допустимых идентификаторов:

    i
    wo_rd
    b2h


Примеры недействительных идентификаторов:

    1i
    wo rd
    !b2h

"""
import re
import typing
import unittest


def is_valid(st: str) -> bool:
    """
    Проверяет, является ли переданная строка допустимым модификатором.
    """
    return bool(st and re.match(r'(^[a-zA-Z_$])([\w$]*)?$', st))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_valid, (
        ("okay_ok1", True),
        ("$ok", True),
        ("___", True),
        ("str_STR", True),
        ("myIdentf", True),
        ("1ok0okay", False),
        ("!Ok", False),
        ("", False),
        ("str-str", False),
        ("no no", False),
    ))
