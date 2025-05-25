"""
В английском языке все слова в начале предложения должны начинаться с заглавной буквы.

Вам будет дан абзац, в котором не используются заглавные буквы.
Ваша задача — сделать заглавной первую букву первого слова каждого предложения.

Например,

вход:

"hello. my name is inigo montoya. you killed my father. prepare to die."

выход:

"Hello. My name is inigo montoya. You killed my father. Prepare to die."

Вы можете предположить:

    не будет никаких знаков препинания, кроме точек и пробелов

    за всеми точками, кроме последней, будет следовать пробел и по крайней мере одно слово
"""
import typing
import unittest


def fix(st: str) -> str:
    return '. '.join(x.capitalize() for x in st.split('. '))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(fix, (
        ("", ""),
        ("hi.", "Hi."),
        ("hello. my name is inigo montoya. you killed my father. prepare to die.", "Hello. My name is inigo montoya. You killed my father. Prepare to die."),
    ))
