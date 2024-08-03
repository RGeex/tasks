"""
Создайте программу, которая будет принимать строку в качестве входных данных и,
если в строке есть дубликаты более двух буквенных символов, возвращает строку
со всеми лишними символами в скобках.

Например, ввод «aaaabbcdefffffffg» должен вернуть «aa[aa]bbcdeff[fffff]g».

Также убедитесь, что входные данные являются строкой, и верните «Пожалуйста,
введите действительную строку», если это не так.
"""

import re
from itertools import groupby as gb


def string_parse_1(s: str) -> str:
    """
    Поиск подряд идущих дубликатов в строке (более 2-х символов),
    возвращает строку со всеми лишними символами в скобках, если передана
    строка, или возвращает сообщение об ошибке.
    """
    return ''.join([a * 2 + f'[{a * (x - 2)}]' if (x:=len(list(b))) > 2 else a * x for a, b in gb(s)]) if isinstance(s, str) else 'Please enter a valid string'


def string_parse_2(s: str) -> str:
    """
    Поиск подряд идущих дубликатов в строке (более 2-х символов),
    возвращает строку со всеми лишними символами в скобках, если передана
    строка, или возвращает сообщение об ошибке.
    """
    return re.sub(r'(.)\1(\1+)', r'\1\1[\2]', s) if isinstance(s, str) else 'Please enter a valid string'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("aaaabbcdefffffffg", "aa[aa]bbcdeff[fffff]g"),
        (3, "Please enter a valid string"),
        ("boopdedoop", "boopdedoop"),
        ("helloookat", "helloo[o]kat"),
        (True, "Please enter a valid string"),
        ('', ''),
        ('aAAabbcdeffFfFffg', 'aAAabbcdeffFfFffg'),
        ('aAAabbcdeFFFffffg', 'aAAabbcdeFF[F]ff[ff]g'),
        ({}, "Please enter a valid string"),
        ([5.3], "Please enter a valid string"),
    )
    for key, val in data:
        assert string_parse_1(key) == val
        assert string_parse_2(key) == val


if __name__ == '__main__':
    test()
