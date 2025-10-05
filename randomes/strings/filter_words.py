"""
Напишите функцию, принимающую строку типа
WOW this is REALLY          amazing
и возвращение
Wow this is really amazing.
Строка должна быть написана заглавными буквами и с правильными интервалами.

Примеры:

"HELLO CAN YOU HEAR ME" --> "Hello can you hear me"
"now THIS is REALLY interesting" --> "Now this is really interesting"
"THAT was EXTRAORDINARY!" --> "That was extraordinary!"
"""
import typing
import unittest


def filter_words(st: str) -> str:
    """
    Убирает лишние пробелы и дулает закгавной только первую букву предложения.
    """
    return ' '.join(st.split()).capitalize()


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(filter_words, (
        ('HELLO world!', 'Hello world!'),
        ('This    will    not    pass ', 'This will not pass'),
        ('NOW THIS is a VERY EXCITING test!', 'Now this is a very exciting test!'),
    ))
