"""
Многие товары имеют международный товарный номер
(ранее известный как «европейский товарный номер»),
сокращённо «EAN». EAN — это 13-значный штрихкод, состоящий из
12 цифр и однозначной контрольной суммы
(EAN-8 в данном случае не рассматривается).

Однозначная контрольная сумма рассчитывается следующим образом
(на основе первых 12 цифр):

    Цифры на первой, третьей, пятой и т.д. позициях
    (т.е. на нечетных позициях) умножаются на 1.
    Цифры на второй, четвертой, шестой и т.д. позициях
    (т.е. на четных позициях) умножаются на 3.
    Сложите эти результаты.

Если эта сумма делится на 10, контрольная сумма равна 0.
В противном случае контрольная сумма имеет следующую формулу:

checksum=10−(summod  10)\text{checksum} = 10 - (\text{sum} \mod 10)контрольная сумма = 10 − ( сумма mod 10 )

Таким образом, EAN-код — 400330101839 8 (12 цифр, за которыми следует
однозначная контрольная сумма).
Ваша задача

Проверить указанный EAN-код. Возврат True/trueесли данный EAN-код
действителен, в противном случае False/false.
Предположение

Можно предположить, что данный код синтаксически верный, т.е. он
состоит только из цифр и имеет длину ровно 13 символов.
Примеры

"4003301018398" - True
"4003301018392" - False

Удачи и получайте удовольствие.

"""
import typing
import unittest


def validate_ean(code: str) -> bool:
    """
    Проверяет, соответствует ли номер EAN стандарту.
    """
    return not sum((i % 2 or 3) * int(n) for i, n in enumerate(code, 1)) % 10


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(validate_ean, (
        ("9783815820865", True),
        ("9783815820864", False),
        ("9783827317100", True),
    ))
