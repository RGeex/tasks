"""
Если представить слово как последовательность и не ограничиваться лишь
словарными словами, то для другого слова состоящего из 2 и более разлиных
букв, существуют другие слова состоящие из тех же букв, но в другом порядке.

Затем мы можем присвоить номер каждому слову в зависимости от того, где оно
находится в отсортированном по алфавиту списке всех слов, состоящих из одной
и той же группы букв. Один из способов сделать это — сгенерировать весь
список слов и найти нужное, но это будет медленно, если слово длинное.

По слову вернуть его номер. Ваша функция должна иметь возможность принимать
любое слово длиной 25 или менее букв (возможно, с повторением некоторых букв)
и выполняться не более 500 миллисекунд.
"""

from itertools import permutations as pm
from collections import Counter
from functools import reduce


def func(word: str) -> int:
    """Правильный, но медленный способ, потому что создает
    все возможные варианты."""
    result = {''.join(v): i for i, v in enumerate(
        sorted(set(pm(word))), 1)}.get(word)
    return result


def factorial(x):
    """Возвращает факториал числа N > 0."""
    res = 1
    for num in range(1, x + 1):
        res *= num
    return res


def position(word):
    """Поиск порядкового номера слова из возможных вариантов букв
    исходного слова."""
    res = 1
    for i, char in enumerate(word):
        ort = sorted(word[i:])
        pos = ort.index(char)
        tmp = len(word[i:])

        den = reduce(lambda a, b: a * b, map(factorial, Counter(ort).values()))
        fac = factorial(tmp - 1) if tmp > 1 else 0

        res += fac * pos // den

    return res


def test() -> None:
    """Тестирование работы алгоритмов."""

    word1 = 'baaaa'
    word2 = 'QUESTION'

    assert position(word1) == func(word1)
    assert position(word2) == func(word2)


if __name__ == '__main__':
    test()
