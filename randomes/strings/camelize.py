"""
Вы должны создать метод, который может преобразовывать строку из любого
формата в PascalCase. Это также должно поддерживать символы. Не думайте,
что разделителей слишком много, иначе вы можете быть удивлены. 
"""

import re


def camelize(string: str) -> str:
    """
    Преобразование строки в PascalCase.
    """
    return ''.join(x.capitalize() for x in re.findall(r'[^\W_]+', string))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("testing ABC", "TestingAbc"),
        ("example name", "ExampleName"),
        ("your-NaMe-here", "YourNameHere"),
        ("Arabian_string-Test", "ArabianStringTest"),
        ("Y6r pbg0p qCq1gvCCz0rXjYAik  ye4dca9eK0ngfa. yCKofKM?",
         "Y6rPbg0pQcq1gvccz0rxjyaikYe4dca9ek0ngfaYckofkm"),
    )

    for key, val in data:
        assert camelize(key) == val


if __name__ == '__main__':
    test()
