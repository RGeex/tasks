"""
Поскольку не существует детерминированного способа определить, какой шаблон
действительно был исходным среди всех возможных перестановок подходящего
подшаблона, верните подшаблон с отсортированными символами, в противном
случае верните базовую строку с отсортированными символами (этот случай
можно рассматривать как крайний случай). , при этом подшаблон повторяется
только один раз и, таким образом, равен исходной входной строке).

Например:

has_subpattern("a") == "a"; #no repeated pattern, just one character
has_subpattern("aaaa") == "a" #just one character repeated
has_subpattern("abcd") == "abcd" #base pattern equals the string itself, no repetitions
has_subpattern("babababababababa") == "ab" #remember to return the base string sorted"
has_subpattern("bbabbaaabbaaaabb") == "ab" #same as above, just shuffled
"""


from math import gcd
from collections import Counter


def has_subpattern(s: str) -> str:
    """
    Поиск минимального шаблона для строки.
    """
    return (c := Counter(s)) and ''.join(sorted([n // gcd(*c.values()) * w for w, n in c.items()]))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("a", "a"),
        ("aaaa", "a"),
        ("abcd", "abcd"),
        ("babababababababa", "ab"),
        ("bbabbaaabbaaaabb", "ab"),
        ("123a123a123a", "123a"),
        ("123A123a123a", "111222333Aaa"),
        ("12aa13a21233", "123a"),
        ("12aa13a21233A", "111222333Aaaa"),
        ("abcdabcaccd", "aaabbccccdd"),
    )
    for key, val in data:
        assert has_subpattern(key) == val


if __name__ == '__main__':
    test()
