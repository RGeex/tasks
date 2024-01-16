"""
Завершите решение так, чтобы функция разбивала верблюжий регистр, используя пробел между словами.
Пример

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""


"""

import re


def break_camel_case(s: str) -> str:
    """
    Разделяет строку написанную в CamelCase стиле.
    """
    return re.sub(r'(\w)([A-Z])', r'\1 \2', s)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("helloWorld", "hello World"),
        ("camelCase", "camel Case"),
        ("breakCamelCase", "break Camel Case"),
    )
    for key, val in data:
        assert break_camel_case(key) == val


if __name__ == '__main__':
    test()
