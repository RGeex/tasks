"""
Поздравляем! Этот особенный человек дал вам свой номер телефона.

Но ПОДОЖДИТЕ, это действительное число?

Ваша задача — написать функцию, которая проверяет, содержит ли заданная строка
действительный британский номер мобильного телефона или нет.

    Если строка является допустимым номером Великобритании, верните "In with a chance".

    Если он недействителен или вам дана пустая строка, верните "Plenty more fish in the sea".

Число может быть действительным в следующих случаях:

    В Великобритании мобильные номера начинаются с "07"за которыми следуют 9 других цифр,
    например "07454876120".

    Иногда перед номером стоит код страны, префикс "+44", который заменяет "0" в ‘07’,
    например "+447454876120".

    Иногда вы встретите числа с тире между цифрами или по обеим сторонам, например
    "+44--745---487-6120" или "-074-54-87-61-20-". Как видите, тире могут идти подряд.

Удачи, Ромео/Джульетта!

"""
import re
import typing
import unittest


def validate_number(st: str) -> str:
    """
    Проверяет, является ли введенный номер, номером великобритании.
    """
    return ['In with a chance', 'Plenty more fish in the sea'][not re.match(r'^(\+447|07)(\d{9})$', st.replace('-', ''))]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(validate_number, (
        ("07454876120", "In with a chance"),
        ("0754876120", "Plenty more fish in the sea"),
        ("0745--487-61-20", "In with a chance"),
        ("+447535514555", "In with a chance"),
        ("-07599-51-4555", "In with a chance"),
        ("075335440555", "Plenty more fish in the sea"),
        ("+337535512555", "Plenty more fish in the sea"),
        ("00535514555", "Plenty more fish in the sea"),
        ("+447+4435512555", "Plenty more fish in the sea"),
        ("+44", "Plenty more fish in the sea"),
    ))
