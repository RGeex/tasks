"""
В этом ката мы собираемся определить, может ли количество каждого символа в
строке быть равным, если мы удалим один символ из этой строки.

Например:

solve('abba') = false -- if we remove any character, the count of each
character will not be equal.
solve('abbba') = true -- if we remove one b, the count of each character
becomes 2.
solve('aaaa') = true -- if we remove one character, the remaining characters
have same count.
solve('wwwf') = true -- if we remove f, the remaining letters have same count.

Больше примеров в тестовых примерах. Пустая строка не проверяется. 
"""


from collections import Counter


def align_symb(s: str) -> bool:
    """
    Проверяет, можно ли убрать 1 символ из строки, что бы кол-во одинаковых символов было равное.
    """
    return any(len(set(Counter(sorted(s, key=s.count)[i:None if i else -1]).values())) == 1 for i in range(2))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('aaaa',True),
        ('abba',False),
        ('abbba',True),
        ('aabbcc',False),
        ('aaaabb',False),
        ('aabbccddd',True),
        ('aabcde',True),
        ('abcde',True),
        ('aaabcde',False) ,
        ('abbccc',False),
        ('aabbccdddeee',False),
    )
    for key, val in data:
        assert align_symb(key) == val


if __name__ == '__main__':
    test()
