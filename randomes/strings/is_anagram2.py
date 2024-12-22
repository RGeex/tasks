"""
Создайте функию, проверяющую, являются ли все слова свлова
переданного списка анаграммами.
"""
from itertools import zip_longest as zl


def is_anagram(arr: list[str]) -> bool:
    """
    Проверяет, является ли все слова списка анагаммами.
    """
    return not next((1 for x in zl(*map(sorted, arr)) if 1 < len(set(x))), 0)


def test():
    """
    Тестирование алгоритмов.
    """
    data = (
        (['add', 'dad', 'dda'], True),
        (['add', 'dad', 'dda', 'dadzz'], False),
    )
    for key, val in data:
        assert is_anagram(key) is val


if __name__ == '__main__':
    test()
