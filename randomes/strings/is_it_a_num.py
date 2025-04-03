"""
Исправьте мои номера телефонов

О, слава богу, ты здесь! Последний стажер все испортил!

Все номера телефонов наших клиентов зашифрованы, и нам нужны эти номера телефонов,
чтобы раздражать их бесконечными звонками с предложениями о продажах!
Формат

Номера телефонов хранятся в виде строк и состоят из 11 цифр, например '02078834982'и
всегда должен начинаться с 0.

Однако произошло нечто странное, и теперь все номера телефонов содержат множество
случайных символов, пробелов, а некоторые из них вообще не являются номерами телефонов!

Например, '02078834982'каким-то образом стало 'efRFS:)0207ERGQREG88349F82!'и есть
еще много строк, которые нам нужно проверить.
Задача

Имея строку, вы должны решить, содержит ли она действительный номер телефона.
Если содержит, вернуть исправленный номер телефона в виде строки, т.е.
'02078834982'без пробелов и специальных символов, в противном случае вернуть "Not a phone number".
"""
import typing
import unittest


def is_it_a_num(st: str) -> str:
    """
    Убирает из строки все кроме цифр и проверят, что цифры являются номером телефона.
    """
    return x if (x := ''.join(n for n in st if n.isdigit())).startswith('0') and len(x) == 11 else "Not a phone number"


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_it_a_num, (
        ("S:)0207ERGQREG88349F82!efRF)", "02078834982"),
        ("sjfniebienvr12312312312ehfWh", "Not a phone number"),
        ("0192387415456", "Not a phone number"),
        ("v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165", "02084564165"),
        ("stop calling me no I have never been in an accident", "Not a phone number"),
    ))
