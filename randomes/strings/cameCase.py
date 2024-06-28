"""
Завершите решение так, чтобы функция разбивала верблюжий регистр,
используя пробел между словами.
Пример

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


import re


def cameCase(s: str) -> str:
    """
    Разделяет camelCase слово на отдельные слова.
    """
    return re.sub(r'([A-Z])', r' \1', s)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("helloWorld", "hello World"),
        ("camelCase", "camel Case"),
        ("breakCamelCase", "break Camel Case"),
        ('nocapitals', 'nocapitals'),
        ('', ''),
        ('consecutiveCApitals', 'consecutive C Apitals'),
    )
    for key, val in data:
        assert cameCase(key) == val


if __name__ == '__main__':
    test()
