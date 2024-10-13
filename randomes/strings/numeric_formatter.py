"""
Ваша цель — создать функцию для форматирования числа по шаблону;
если номера нет, используйте цифры 1234567890 чтобы заполнить пробелы.

Несколько правил:

    шаблон может состоять из других цифр, специальных символов и т.п.:
    заменять нужно только буквы алфавита (как строчные, так и прописные);
    если заданная строка или строка по умолчанию, представляющая число,
    короче шаблона, просто повторите ее, чтобы заполнить все пробелы.

Несколько примеров:

numeric_formatter("xxx xxxxx xx","5465253289") == "546 52532 89"
numeric_formatter("xxx xxxxx xx") == "123 45678 90"
numeric_formatter("+555 aaaa bbbb", "18031978") == "+555 1803 1978"
numeric_formatter("+555 aaaa bbbb") == "+555 1234 5678"
numeric_formatter("xxxx yyyy zzzz") == "1234 5678 9012"
"""


from itertools import cycle


def numeric_formatter(template : str, strng : str = '1234567890') -> str:
    s = cycle(strng)
    return ''.join(next(s) if x.isalpha() else x for x in template)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("xxx xxxxx xx","5465253289"), "546 52532 89"),
        (("xxx xxxxx xx",), "123 45678 90"),
        (("+555 aaaa bbbb", "18031978"), "+555 1803 1978"),
        (("+555 aaaa bbbb",), "+555 1234 5678"),
        (("xxxx yyyy zzzz",), "1234 5678 9012"),
    )
    for key, val in data:
        assert numeric_formatter(*key) == val


if __name__ == '__main__':
    test()
