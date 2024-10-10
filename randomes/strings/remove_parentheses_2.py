"""
Удалите круглые скобки

В этой ката вам дана строка, например:

"example(unwanted thing)example"

Ваша задача — удалить все, что находится внутри скобок, а также сами скобки.

Пример выше вернет:

"exampleexample"

Примечания

    Кроме круглых скобок, в строке могут встречаться только буквы и пробелы.
    Не беспокойтесь о других скобках, таких как "[]" и "{}" поскольку они никогда не появятся.
    Круглых скобок может быть несколько.
    Круглые скобки могут быть вложенными.


"""


import re


def remove_parentheses(s: str) -> str:
    """
    Удаляет все выражения в скобках из строки.
    """
    return remove_parentheses(re.sub(r'\([^\(\)]*\)', '', s)) if re.findall(r'[\(\)]', s) else s


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
        ("(first group) (second group) (third group)", "  "),
    )
    for key, val in data:
        assert remove_parentheses(key) == val


if __name__ == '__main__':
    test()
