"""
Палиндром — это серия символов, которые читаются одинаково как в прямом,
так и в обратном направлении, например «hannah», «racecar» и «lol».

Для этого Ката вам нужно написать функцию, которая принимает строку символов
и возвращает длину в виде целого значения самого длинного буквенно-цифрового
палиндрома, который можно создать, комбинируя символы в любом порядке, но
используя каждый символ только один раз. Функция не должна быть чувствительной
к регистру.

Например, если передано «Hannah», оно должно вернуть 6, а если передано
«aabbcc_yYx_», оно должно вернуть 9, потому что одним из возможных палиндромов
будет «abcyxycba».
"""


import re
from collections import Counter


def longest_palindrome(s: str) -> int:
    """
    Подсчитывает длинну самого большого палиндрома, который можно составить из заданной строки.
    """
    tmp = [[0, v][::[-1, 1][v % 2]] for v in Counter(re.sub(r'[^a-z0-9]', '', s.lower())).values()]
    tmp = [[n - 1 if i else n for i, n in enumerate(sorted(x)[::-1]) if n] if i else x for i, x in enumerate(zip(*tmp))]
    return sum(n for x in tmp for n in x)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("A", 1),
        ("Hannah", 6),
        ("xyz__a_/b0110//a_zyx", 13),
        ("$aaabbbccddd_!jJpqlQx_.///yYabababhii_", 25),
        ("", 0),
    )
    for key, val in data:
        assert longest_palindrome(key) == val


if __name__ == '__main__':
    test()
