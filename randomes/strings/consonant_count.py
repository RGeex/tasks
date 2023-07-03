"""
Завершите функцию, которая принимает строку текста на английском языке и
возвращает количество согласных в строке.

Согласные — это все буквы, используемые в английском языке, за исключением
гласных a, e, i, o, u.
"""


def consonant_count(string: str) -> int:
    """Подсчет согласных в строке."""
    data = set(map(chr, range(97, 123))) - set('aeiou')
    return sum(char in data for char in string.lower())


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ('', 0),
        ('aaaaa', 0),
        ('Bbbbb', 5,),
        ('XaeiouX', 2),
        ('012345_Cb', 2),
        ('0123456789', 0),
        ('helLo world', 7),
        ('h^$&^#$&^elLo world', 7),
    )

    for key, val in data:
        assert consonant_count(key) == val


if __name__ == '__main__':
    test()
