"""
Для данной строки sнайди персонажа c(или C) с самым длинным последовательным
повторением и возвратом:

(c, l)

где l(или L) — длина повторения. Если есть два или более символов с одинаковым
l верните первый в порядке появления.

Для возврата пустой строки:

('', 0)
"""


from itertools import groupby


def longest_repetition(chars: str) -> tuple:
    """
    В заданной строке находит самую длинную последовательность.
    """
    return min([((a, len(list(b))), i) for i, (a, b) in enumerate(groupby(chars))], key=lambda x: (-x[0][1], x[1]), default=(('', 0), 0))[0]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ["aaaabb", ('a', 4)],
        ["bbbaaabaaaa", ('a', 4)],
        ["cbdeuuu900", ('u', 3)],
        ["abbbbb", ('b', 5)],
        ["aabb", ('a', 2)],
        ["ba", ('b', 1)],
        ["", ('', 0)],
    )
    for key, val in data:
        assert longest_repetition(key) == val


if __name__ == '__main__':
    test()
