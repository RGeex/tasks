"""
В России имеется армейская станция УВБ-76 или «Зуммер».

Большую часть времени транслируется характерный «жужжащий» шум, но в очень редких случаях сигнал
зуммера прерывается и происходит голосовая передача на русском языке.

Передаваемые сообщения всегда имеют один и тот же формат:

MDZHB 01 213 SKIF 38 87 23 95

или

MDZHB 80 516 GANOMATIT 21 23 86 25

Формат сообщения состоит из следующих частей:

    Начальное ключевое слово «МДЖБ»;
    Две группы цифр, в первой — 2 цифры, во второй — 3;
    Некоторое ключевое слово произвольной длины, состоящее только из заглавных букв;
    Конечные 4 группы цифр по 2 цифры в каждой группе.

Ваша задача — написать функцию, которая может проверить корректность сообщения УВБ-76. Функция
должна возвращать trueесли сообщение в правильном формате и false в противном случае.

"""
import re
import typing
import unittest


def validate(message: str) -> bool:
    """
    Проверка соответствие строки заданному формату.
    """
    return bool(re.search(r'^MDZHB \d{2} \d{3} [A-Z]+ \d{2} \d{2} \d{2} \d{2}$', message))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(validate, (
        ("Is this a right message?", False),
        ("MDZHB 85 596 KLASA 81 00 02 91", True),
        ("MDZHB 12 733 EDINENIE 67 79 66 32", True),
        ("MDZHV 60 130 VATRUKH 58 89 54 54", False),
    ))
