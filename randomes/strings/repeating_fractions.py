"""
Писать

function repeating_fractions(numerator, denominator)

что, учитывая два числа, представляющие числитель и знаменатель дроби, возвращает дробь в строковом формате.
Если в дробной части есть повторяющиеся цифры, замените эти цифры одной цифрой в скобках.

Например:

repeating_fractions(1,1) === '1'
repeating_fractions(1,3) === '0.(3)'
repeating_fractions(2,888) === '0.(0)(2)5(2)5(2)5(2)5(2)5(2)'
"""


from itertools import groupby as gb


def repeating_fractions(a: int, b: int) -> str:
    """
    Объединение подряд идущих цифр знаменателя в скобки.
    """
    return '.'.join(''.join([key, f'({key})'][1 < len(list(val))] for key, val in gb(x)) if i else x for i, x in enumerate(str(a / b).split('.')))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((0, 1), '0.0'),
        ((18018018, 80000000000), '0.(0)(2)5(2)5(2)5'),
        ((1, 1), '1.0'),
        ((1, 2), '0.5'),
        ((1, 3), '0.(3)'),
        ((1554, 70), '22.2'),
    )
    for key, val in data:
        assert repeating_fractions(*key) == val


if __name__ == '__main__':
    test()
