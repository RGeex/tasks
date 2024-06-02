"""
Создайте функцию, которая принимает строку в качестве параметра и выполняет
следующие действия в следующем порядке:

    Заменяет каждую букву буквой, следующей за ней в алфавите
    (см. примечание ниже).
    Делает любые гласные заглавными
    Переводит любые согласные в нижний регистр

Примечание:

    алфавит должен повторяться, поэтому Z становится A
    в этой ката, y не считается гласной.

Так, например, строка "Cat30" вернусь "dbU30" ( Cat30 --> Dbu30 --> dbU30)
"""


def changer1(s: str) -> str:
    """
    Заменяет буквы в строке, согласно заданию.
    """
    return s.lower().translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'bcdEfghIjklmnOpqrstUvwxyzA'))


def changer2(s: str) -> str:
    """
    Заменяет буквы в строке, согласно заданию.
    """
    return ''.join([dict(zip('abcdefghijklmnopqrstuvwxyz', 'bcdEfghIjklmnOpqrstUvwxyzA')).get(x, x) for x in s.lower()])


def changer3(s: str) -> str:
    """
    Заменяет буквы в строке, согласно заданию.
    """
    return ''.join([(x.upper() if (x := chr((ord(w) - 96) % 26 + 97)) in 'aeoiu' else x) if w.isalpha() else w for w in s.lower()])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('Cat30', 'dbU30'),
        ('Alice', 'bmjdf'),
        ('sponge1', 'tqpOhf1'),
        ('Hello World', 'Ifmmp xpsmE'),
        ('dogs', 'Epht'),
        ('z', 'A'),
    )
    for key, val in data:
        assert changer1(key) == val
        assert changer2(key) == val
        assert changer3(key) == val


if __name__ == '__main__':
    test()
