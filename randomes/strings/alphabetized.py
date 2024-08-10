"""
Ката в алфавитном порядке

Измените порядок символов строки, чтобы они были объединены в новую строку в
порядке «алфавитный порядок появления без учета регистра». Пробелы и знаки
препинания просто удаляются!

Ввод не должен содержать цифр и только слов, содержащих буквы английского
алфавита.

Пример:

alphabetized("The Holy Bible") # "BbeehHilloTy"
"""


def alphabetized(s: str) -> str:
    """
    Сортирует строку независимо от регистра,
    убирает из строки все кроме букв.
    """
    return ''.join(sorted(filter(str.isalpha, s), key=str.lower))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("", ""),
        (" ", ""),
        (" a", "a"),
        ("a ", "a"),
        (" a ", "a"),
        ("A b B a", "AabB"),
        ("!@$%^&*()_+=-`,", ""),
        ("The Holy Bible", "BbeehHilloTy"),
        ("CodeWars can't Load Today", "aaaaCcdddeLnooorstTWy"),
    )
    for key, val in data:
        assert alphabetized(key) == val


if __name__ == '__main__':
    test()
