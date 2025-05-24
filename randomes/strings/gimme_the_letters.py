"""
Если задана строка, указывающая диапазон букв, вернуть строку, которая включает все буквы 
в этом диапазоне, включая последнюю букву.
Обратите внимание: если диапазон указан заглавными буквами , верните строку также
заглавными буквами!
Примеры

"a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
"h-o" ➞ "hijklmno"
"Q-Z" ➞ "QRSTUVWXYZ"
"J-J" ➞ "J"

Примечания

    . дефисом Две буквы в строке будут разделены
    Вам не нужно беспокоиться об обработке ошибок в этом ката (т.е. обе буквы будут иметь
    одинаковый регистр, и вторая буква не будет предшествовать первой по алфавиту).
"""
import typing
import unittest


def gimme_the_letters(st: str) -> str:
    """
    Возвращает заданный диапазон букв.
    """
    return ''.join(map(chr, range(*[ord(x) + i for i, x in enumerate(st.split('-'))])))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(gimme_the_letters, (
        ("a-z", "abcdefghijklmnopqrstuvwxyz"),
        ("h-o", "hijklmno"),
        ("Q-Z", "QRSTUVWXYZ"),
        ("J-J", "J"),
        ("a-b", "ab"),
        ("A-A", "A"),
        ("g-i", "ghi"),
        ("H-I", "HI"),
        ("y-z", "yz"),
        ("e-k", "efghijk"),
        ("a-q", "abcdefghijklmnopq"),
        ("F-O", "FGHIJKLMNO"),
    ))
