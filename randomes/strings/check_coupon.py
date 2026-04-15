"""
История

Ваш интернет-магазин любит раздавать купоны по особым случаям.
Некоторые покупатели пытаются обмануть систему, вводя недействительные коды
или используя просроченные купоны.
Задача

Ваша миссия:
Напишите функцию с именем checkCouponЭто позволяет проверить, действителен ли промокод и не
просрочен ли он.

    Купон становится недействительным на следующий день после истечения срока его действия.
    Все даты будут передаваться в виде строк в следующем формате: "MONTH DATE, YEAR".
    Для того чтобы правильный код и введенный код совпадали, их значения и типы данных должны быть
    одинаковыми. Это означает, например, что false и 0не одно и то же, и ни одно из них не является
    одинаковым. 123 и "123".

Примеры:

("123", "123", "July 9, 2015", "July 9, 2015")  ===>  true
(0,  false,    "July 9, 2015", "July 9, 2015")  ===>  false
("123", "123", "July 9, 2015", "July 2, 2015")  ===>  false

"""
import unittest
from typing import Any, Callable, Tuple
from datetime import datetime
from operator import le


def check_coupon(entered_code: Any, correct_code: Any, current_date: str, expiration_date: str) -> bool:
    """
    Определяет ситатус купона.
    """
    return type(entered_code) == type(correct_code) and entered_code == correct_code and le(*[datetime.strptime(x, '%B %d, %Y') for x in (current_date, expiration_date)])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(check_coupon, (
        (('123', '123', 'September 5, 2014', 'October 1, 2014'), True),
        (('123a', '123', 'September 5, 2014', 'October 1, 2014'), False),
        (('12abcd3', '12abcd3', 'January 5, 2014', 'January 1, 2014'), False),
        (('123ablqc0', '123ablqc0', 'July 5, 2000', 'July 5, 2000'), True),
        (('abc', 'abc', 'November 8, 2013', 'November 5, 2014'), True),
        ((0, False, 'September 5, 2014', 'September 25, 2014'), False),
        (('0', False, 'September 5, 2014', 'September 25, 2014'), False),
        (('1', True, 'September 5, 2014', 'September 25, 2014'), False),
        ((1+1, '2', 'September 5, 2014', 'September 25, 2014'), False),
        (('a12v564', 'a12v564', 'March 5, 1998', 'March 25, 1998'), True),
        (('0a12bc64', '0a12bc64', 'March 6, 2005', 'March 5, 2006'), True),
        ((1, True, 'September 5, 2014', 'September 25, 2014'), False),
        (("blah", "blahblah"[:4], 'September 5, 2014', 'September 25, 2014'), True),
    ))
