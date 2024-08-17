"""
Вы получаете «текст» и должны сдвинуть гласные на «n» позиций вправо.
(Отрицательное значение n должно сместиться влево.)
«Позиция» означает позицию гласной, если рассматривать ее как один элемент в
списке всех гласных в строке.
Сдвиг на 1 будет означать, что каждая гласная сдвигается на место следующей
гласной.

Смещение по краям текста должно продолжаться с другого края.

Example:

text = "This is a test!"
n = 1
output = "Thes is i tast!"

text = "This is a test!"
n = 3
output = "This as e tist!"

If text is null or empty return exactly this value.
Vowels are "a,e,i,o,u".
"""


import re
from collections import deque
from itertools import zip_longest as zl


def vowel_shift(text: str, n: int) -> str:
    """
    Сдвигает гласные на N шагов, оставляя согласные на своих местах.
    """
    s = ['', text][isinstance(text, str)]
    x = [(x := deque(k := re.split(r'([AEIOUaeiou])', s)[i::2])).rotate(bool(set(k) & set('AEIOUaeiou')) and n % len(k)) or x for i in range(2)]
    return ''.join([a for b in list(zl(*x, fillvalue='')) for a in b]) or text


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("This is a test!", 0), "This is a test!"),
        (("This is a test!", 1), "Thes is i tast!"),
        (("This is a test!", 3), "This as e tist!"),
        (("This is a test!", 4), "This is a test!"),
        (("This is a test!", -1), "This as e tist!"),
        (("This is a test!", -5), "This as e tist!"),
        (("Brrrr", 99), "Brrrr"),
        (("AEIOUaeiou", 1), "uAEIOUaeio"),
    )
    for key, val in data:
        assert vowel_shift(*key) == val


if __name__ == '__main__':
    test()
