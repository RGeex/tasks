"""
Удалите круглые скобки

В этой ката вам дана строка, например:

"example(unwanted thing)example"

Ваша задача — удалить все, что находится внутри скобок, а также сами скобки.

Пример выше вернет:

"exampleexample"

Примечания

    Кроме круглых скобок, в строке могут встречаться только буквы и пробелы.
    Не беспокойтесь о других скобках, таких как "[]"и "{}"поскольку они
    никогда не появятся.
    Круглых скобок может быть несколько.
    Круглые скобки могут быть вложенными.
"""


import re


def remove_parentheses(s: str) -> str:
    """
    Убирает из строки выражения в скобках.
    """
    return re.sub(r'\(.*\)', '', s)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("example(unwanted thing)example", "exampleexample"),
        ("example (unwanted thing) example", "example  example"),
        ("a (bc d)e", "a e"),
        ("a(b(c))", "a"),
        ("hello example (words(more words) here) something", "hello example  something"),
    )
    for key, val in data:
        assert remove_parentheses(key) == val


if __name__ == '__main__':
    test()
