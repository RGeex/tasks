"""
Вам нужно написать регулярное выражение, которое будет проверять
пароль, чтобы убедиться, что он соответствует следующим критериям:

    Длина не менее шести символов
    содержит строчную букву
    содержит заглавную букву
    содержит цифру
    содержит только буквенно-цифровые символы,
    (обратите внимание, что '_' не буквенно-цифровой)
"""

import re


def clean_pass(password: str) -> bool:
    """
    Проверка пароля по условию через регулярные выражения.
    """
    regex = r'^(?=.*\d+)(?=.*[a-z])(?=.*[A-Z])([^\W_]{6,})$'
    return bool(re.match(regex, password))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('fjd3IR9', True),
        ('ghdfj32', False),
        ('DSJKHD23', False),
        ('dsF43', False),
        ('4fdg5Fj3', True),
        ('DHSJdhjsU', False),
        ('fjd3IR9.;', False),
        ('fjd3  IR9', False),
        ('djI38D55', True),
        ('a2.d412', False),
        ('JHD5FJ53', False),
        ('!fdjn345', False),
        ('jfkdfj3j', False),
        ('123', False),
        ('abc', False),
        ('123abcABC', True),
        ('ABC123abc', True),
        ('Password123', True),
    )
    for key, val in data:
        assert clean_pass(key) == val


if __name__ == '__main__':
    test()
