"""
Анаграмма – это слово, фраза или предложение, образованное из другого путем перестановки его букв.
Примером этого является слово «ангел», которое является анаграммой слова «подбирать».

Напишите функцию, которая получает массив слов и возвращает общее количество различных пар
анаграммных слов внутри него.

Некоторые примеры:

    В массиве 2 анаграммы ["dell", "ledl", "abc", "cba"]
    В массиве 7 анаграмм. ["dell", "ledl", "abc", "cba", "bca", "bac"]
"""

from collections import Counter


def anagram_counter(words: list[str]) -> int:
    """
    Подсчет колличеств анаграм в списке.
    """
    return sum(x * (x - 1) // 2 for x in Counter(''.join(sorted(x)) for x in words).values())


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([], 0),
        (['dell', 'ledl', 'abc', 'cba'], 2),
        (['dell', 'ledl', 'lled', 'cba'], 3),
        (['dell', 'ledl', 'abc', 'cba', 'bca', 'bac', 'cab'], 11),
    )
    for key, val in data:
        assert anagram_counter(key) == val


if __name__ == '__main__':
    test()
