"""
Переместите каждую букву в предоставленной строке вперед 10 букв через алфавит.

Если он пройдет мимо «Z», начните снова в «А».

Ввод будет строкой с длиной> 0.
"""
import typing
import unittest


def move_ten(st: str) -> str:
    """
    Сдвиг положения букв в тексте на 10 позиций.
    """
    return st.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'klmnopqrstuvwxyzabcdefghij'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(move_ten, (
        ("testcase", "docdmkco"),
        ("codewars", "mynogkbc"),
        ("exampletesthere", "ohkwzvodocdrobo"),
        ("returnofthespacecamel", "bodebxypdroczkmomkwov") ,
        ("bringonthebootcamp", "lbsxqyxdrolyydmkwz") ,
        ("weneedanofficedog", "goxoonkxyppsmonyq") ,
    ))
