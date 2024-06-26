"""
Учитывая целое число, вернуть строку с тире '-'знаки до и после каждой
нечетной цифры, но не начинают и не заканчивают строку тире.

Бывший:

274 -> '2-7-4'
6815 -> '68-1-5'
"""


def dashatize(n: int) -> str:
    """
    Формирует строку, заданным образом из полученного числа.
    """
    return ''.join([x, f'-{x}-'][int(x) % 2] for x in str(abs(n))).replace('--', '-').strip('-')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (0, "0"),
        (-1, "1"),
        (274, "2-7-4"),
        (5311, "5-3-1-1"),
        (86320, "86-3-20"),
        (-28369, "28-3-6-9"),
        (974302, "9-7-4-3-02"),
    )
    for key, val in data:
        assert dashatize(key) == val


if __name__ == '__main__':
    test()
