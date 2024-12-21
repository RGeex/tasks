"""
Напишите конвертер римских чисел в арабские. диапазон от 1 до 3999.
"""
import re
from operator import sub


def roman_to_arabic(s: str) -> int:
    """
    Конвертирует римские числа в арабские.
    """
    nums = dict(zip('IVXLCDM', [1, 5, 10, 50, 100, 500, 1000]))
    return sub(*[sum(map(nums.get, x)) for x in (s, re.findall(r'I(?=[VX])|X(?=[LC])|C(?=[DM])', f'{s}.' * 2))])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("XIV", 14),
        ("MCMXCIV", 1994),
    )
    for key, val in data:
        assert roman_to_arabic(key) == val


if __name__ == '__main__':
    test()
