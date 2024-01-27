"""
Если мы запишем цифры «60» как английские слова, то получим «sixzero»;
количество букв в «sixzero» равно семи. Количество букв в слове «seven» — пять.
Количество букв в слове «five» — четыре. Количество букв в слове «four» — четыре:
мы достигли устойчивого равновесия.

Примечание: для целых чисел больше 9 запишите названия каждой цифры одним словом
(вместо собственного названия числа на английском языке). Например, напишите 12 как
«один два» (вместо двенадцати), а 999 — как «девять девять» (вместо девятисот девяноста девяти).

Для любого целого числа от 0 до 999 верните массив, показывающий путь от этого
целого числа к стабильному равновесию:
Примеры

numbersOfLetters(60) --> ["sixzero", "seven", "five", "four"]
numbersOfLetters(1) --> ["one", "three", "five", "four"]

"""


def numbers_of_letters(n: int) -> list:
    """
    Нахождение цепочки слов в виде числа для создание баланса.
    """
    r, s = [], 'zero one two three four five six seven eight nine'.split()
    while len(x := ''.join(s[int(x)] for x in str(n))) != n:
        n = not r.append(x) and len(x)
    return r + [x]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1, ["one", "three", "five", "four"]),
        (12, ["onetwo", "six", "three", "five", "four"]),
        (37, ["threeseven", "onezero", "seven", "five", "four"]),
        (311, ['threeoneone', 'oneone', 'six', 'three', 'five', 'four']),
        (999, ["nineninenine", "onetwo", "six", "three", "five", "four"]),
    )
    for key, val in data:
        assert numbers_of_letters(key) == val


if __name__ == '__main__':
    test()
