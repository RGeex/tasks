"""
Учитывая строку слов, вам нужно найти слово с наибольшим количеством очков.

Каждая буква слова набирает очки в зависимости от ее положения в алфавите: a = 1, b = 2, c = 3и т. д.

Например, оценка abadявляется 8 (1 + 2 + 1 + 4).

Вам нужно вернуть слово с наивысшим баллом в виде строки.

Если два слова имеют одинаковую оценку, верните слово, которое встречается первым в исходной строке.

Все буквы будут строчными, и все вводимые данные будут действительными.

"""


def high(x: str) -> str:
    """
    Поиск слова в переданной строке с макс кол-вом балов.
    """
    return max(x.split(), key=lambda x: (sum(ord(n) - 96 for n in x)))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('man i need a taxi up to ubud', 'taxi'),
        ('what time are we climbing up the volcano', 'volcano'),
        ('take me to semynak', 'semynak'),
        ('massage yes massage yes massage', 'massage'),
        ('take two bintang and a dance please', 'bintang'),
        ('aa b', 'aa'),
        ('b aa', 'b'),
        ('bb d', 'bb'),
        ('d bb', 'd'),
        ("aaa b", "aaa"),
    )
    for key, val in data:
        assert high(key) == val


if __name__ == '__main__':
    test()