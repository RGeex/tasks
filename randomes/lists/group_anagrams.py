"""
Ваша задача — сгруппировать слова в анаграммы.
Что такое анаграмма?

starи tsarявляются анаграммами друг друга, потому что вы можете переставлять буквы звезды,
чтобы получить царя .
Пример

Типичный тест может быть:

// input
["tsar", "rat", "tar", "star", "tars", "cheese"]

// output
[
  ["tsar", "star", "tars"],
  ["rat", "tar"],
  ["cheese"]
]

"""

from itertools import groupby as gb


def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Группировка слов исходного списка по анаграммам.
    """
    return [list(v) for _, v in gb(sorted(words, key=lambda x: (len(x), sorted(x))), key=sorted)]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            ["tsar", "rat", "tar", "star", "tars", "cheese"],
            [['rat', 'tar'], ['tsar', 'star', 'tars'], ['cheese']],
        ),
    )
    for key, val in data:
        assert group_anagrams(key) == val


if __name__ == '__main__':
    test()
