"""
В этом ката ваша цель — написать функцию, которая будет менять местами гласные
в строке. Любые символы, не являющиеся гласными, должны оставаться в исходном
положении. Вот некоторые примеры:

"Hello!" => "Holle!"
"Tomatoes" => "Temotaos"
"Reverse Vowels In A String" => "RivArsI Vewols en e Streng"

Для простоты вы можете рассматривать букву y как согласную, а не гласную.
"""

import re
from operator import add
from functools import reduce
from itertools import zip_longest as zl


def reverse_vowels(s: str) -> str:
    """
    Переворачивает гласные буквы в слове, оставляя согласные на своих местах.
    """
    return ''.join(reduce(add, zl(*[(x:=re.split(r'(?i:([aeiou]))', s)[i::2])[::[-1, 1][not set(x) & set('aeiouAEIOU')]] for i in range(2)], fillvalue='')))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("Hello!", "Holle!"),
        ("Tomatoes", "Temotaos"),
        ("Reverse Vowels In A String", "RivArsI Vewols en e Streng"),
    )
    for key, val in data:
        assert reverse_vowels(key) == val


if __name__ == '__main__':
    test()
