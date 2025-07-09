"""
Ваш компьютер забыл, как распознавать ASCII! (или Unicode, как угодно) Он может общаться
только в двоичном формате, и ему нужно сообщить вам нечто важное. Напишите функцию,
которая получит длинную строку двоичного кода и преобразует её в строку. Помните,
что в Python двоичный вывод начинается с '0b'.

В качестве примера: binary_to_string('0b10000110b11000010b1110100') == 'Cat'

Ввод может состоять из заглавных и строчных букв и цифр (конечно, в двоичной форме),
а также специальных символов. Входными данными вашей функции всегда будет одна
строка двоичных данных.

"""
import typing
import unittest


def binary_to_string(binary: str) ->str:
    """
    Строку бинарного кода, преобразует в ASCII.
    """
    return ''.join([chr(int(x, 2)) for x in binary.split('0b') if x])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(binary_to_string, (
        ('0b10000110b11000010b1110100', 'Cat'),
        ('0b10010000b11001010b11011000b11011000b11011110b1000000b10101110b11011110b11100100b11011000b11001000b100001', 'Hello World!'),
        ('0b10100110b11001010b11000110b11100100b11001010b11101000b1000000b11011010b11001010b11100110b11100110b11000010b11001110b11001010b1000000b110001', 'Secret message 1'),
    ))
