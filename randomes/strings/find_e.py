"""
Можно ли написать книгу без буквы «е»?
Задача

Дана строка str, возвращаться:
Сколько символов «e» содержится в строке (без учета регистра).
Если заданная строка не содержит символов «e», вернуть: «Нет никакой «е».»
Если указанная строка пуста, вернуть пустую строку.
Если заданная строка равна `null`/`None`/`nil`, вернуть `null`/`None`/`nil`

"""
import typing
import unittest


def find_e(st: str) -> str:
    """
    Поиск колличества букв "e" в строке или сообщение об ощибке.
    """
    return st and str(st.lower().count('e') or "There is no \"e\".")


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_e, (
        ('actual', "There is no \"e\"."),
        ('English', '1'),
        ('English exercise', '4'),
        ('', ''),
        (None, None),
    ))
