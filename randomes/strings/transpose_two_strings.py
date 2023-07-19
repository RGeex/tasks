"""
Вам будет дан массив, содержащий две строки. Ваша задача — создать функцию,
которая возьмет эти две строки и переместит их так, чтобы строки шли сверху
вниз, а не слева направо.

например:
['Hello','World'] -> "H W\ne o\nl r\nl l\no d"


Несколько замечаний:
Между двумя символами должен быть один пробел
Вам не нужно изменять регистр (т.е. не нужно менять его на верхний или нижний)
Если одна строка длиннее другой, должен быть пробел, где символ будет
"""


from itertools import zip_longest


def transpose_two_strings(arr: list[str]) -> str:
    """Меняет строку по шаблону."""
    return '\n'.join(map(' '.join, zip_longest(*arr, fillvalue=' ')))


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        (["joey", "louise"], "j l\no o\ne u\ny i\n  s\n  e"),
        (["Hello", "World"], "H W\ne o\nl r\nl l\no d"),
        (["!a!a!", "?b?b"], "! ?\na b\n! ?\na b\n!  "),
        (["a", "cat"], "a c\n  a\n  t"),
        (["cat", ""], "c  \na  \nt  "),
    )

    for key, val in data:
        assert transpose_two_strings(key) == val


if __name__ == '__main__':
    test()
