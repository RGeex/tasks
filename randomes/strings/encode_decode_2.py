"""
Этот шифр заключается в том, что каждый символ строки умножается на 6 в результате умножения его кодового значения.

Например, кодирование Hello World!результат ưɞʈʈʚÀȊʚʬʈɘÆ.

Вам необходимо написать две функции:
encodeдля кодирования заданной строки,
decodeРасшифровать заданную строку.

Should work on empty string too


"""
import unittest
from typing import Any, Callable, Tuple


def encode(text: str):
    """
    Кодирует строку.
    """
    return ''.join(chr(ord(x) * 6) for x in text)


def decode(cipher: str):
    """
    Декодирует строку.
    """
    return ''.join(chr(ord(x) // 6) for x in cipher)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(encode, (
        ('Hello World!', 'ưɞʈʈʚÀȊʚʬʈɘÆ'),
        ('', ''),
    ))
    test(decode, (
        ('ưɞʈʈʚÀȊʚʬʈɘÆ', 'Hello World!'),
        ('', ''),
    ))
