"""
Как и в предыдущем ката , вам нужно будет вернуть логическое значение,
если базовая строка может быть выражена как повторение одного подшаблона.

На этот раз есть два небольших изменения:

    если подшаблон использовался, он будет присутствовать как минимум дважды,
    то есть подшаблон должен быть короче исходной строки;
    строки, которые вам будут предоставлены, могут быть созданы, а могут и не
    быть созданы, повторяя заданный подшаблон, а затем перетасовывая результат.

Например:

has_subpattern("a") == False #no repeated shorter sub-pattern, just one character
has_subpattern("aaaa") == True #just one character repeated
has_subpattern("abcd") == False #no repetitions
has_subpattern("babababababababa") == True #repeated "ba"
has_subpattern("bbabbaaabbaaaabb") == True #same as above, just shuffled

Строки никогда не будут пустыми, могут состоять из любых символов
(просто считайте прописные и строчные буквы разными объектами) и могут быть
довольно длинными (следите за производительностью!).
"""


from math import gcd
from collections import Counter


def has_subpattern(s: str) -> bool:
    """
    Проверяет есть ли закономерность в заданной строке.
    """
    return gcd(*Counter(s).values()) > 1


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("a", False),
        ("aaaa", True),
        ("abcd", False),
        ("babababababababa", True),
        ("ababababa", False),
        ("123a123a123a", True),
        ("123A123a123a", False),
        ("12aa13a21233", True),
        ("12aa13a21233A", False),
        ("abcdabcaccd", False),
    )
    for key, val in data:
        assert has_subpattern(key) == val


if __name__ == '__main__':
    test()
