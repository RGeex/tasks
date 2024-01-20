"""
Напишите функцию, которая принимает строку и возвращает массив повторяющихся символов
(букв, цифр, пробелов) в строке.

Если символ повторяется более одного раза, покажите его в массиве результатов только один раз.

Символы должны отображаться в порядке их первого повторения . Обратите внимание, что это может
отличаться от порядка первого появления персонажа.

Символы чувствительны к регистру.

Для F # верните «список символов»
Примеры:

remember("apple") => returns ["p"]
remember("apPle") => returns []          # no repeats, "p" != "P"
remember("pippi") => returns ["p","i"]   # show "p" only once
remember('Pippi') => returns ["p","i"]   # "p" is repeated first

"""


from collections import Counter


def remember(str_: str) -> list:
    """
    Поиск дубликатов в строке в порядке их дублирования.
    """
    return sorted([x for x, n in Counter(str_).items() if n > 1], key=lambda x: str_.find(x, str_.index(x) + 1))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('apple', ["p"]),
        ("limbojackassin the garden", ["a", "s", "i", " ", "e", "n"]),
        ("11pinguin", ["1", "i", "n"]),
        ("Claustrophobic", ["o"]),
        ("apPle", []),
        ("11 pinguin", ["1", "i", "n"]),
        ('pippi', ["p", "i"]),
        ('Pippi', ["p", "i"]),
        ('kamehameha', ["a", "m", "e", "h"]),
        ('', []),
    )
    for key, val in data:
        assert remember(key) == val


if __name__ == '__main__':
    test()
