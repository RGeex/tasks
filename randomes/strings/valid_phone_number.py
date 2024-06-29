"""
Напишите функцию, которая принимает строку и возвращает true,
если она имеет форму номера телефона.
Предположим, что любое целое число от 0 до 9 в любом месте даст
действительный номер телефона.

Беспокойтесь только о следующем формате:
(123) 456-7890 (не забудьте пробел после закрывающих скобок)

Примеры:

"(123) 456-7890"  => true
"(1111)555 2345"  => false
"(098) 123 4567"  => false
"""


import re


def valid_phone_number1(phone_number: str) -> bool:
    """
    Проверяет валидность телефонного номера.
    """
    return bool(re.search(r'^\(\d{3}\) \d{3}-\d{4}$', phone_number))


def valid_phone_number2(phone_number: str) -> bool:
    """
    Проверяет валидность телефонного номера.
    """
    return ''.join([x, 'x'][x.isdigit()] for x in phone_number) == '(xxx) xxx-xxxx'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("(123) 456-7890", True),
        ("(1111)555 2345", False),
        ("(098) 123 4567", False),
        ("(123)456-7890", False),
        ("abc(123)456-7890", False),
        ("(123)456-7890abc", False),
        ("abc(123)456-7890abc", False),
        ("abc(123) 456-7890", False),
        ("(123) 456-7890abc", False),
        ("abc(123) 456-7890abc", False),
        ("(333) 185-0594", True),
    )
    for key, val in data:
        assert valid_phone_number1(key) == val
        assert valid_phone_number2(key) == val


if __name__ == '__main__':
    test()
