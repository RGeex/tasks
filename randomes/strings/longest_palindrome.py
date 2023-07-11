"""
Самый длинный палиндром
Найдите длину самой длинной подстроки в заданной строке s,
которая совпадает в обратном порядке.

Если длина входной строки равна 0, возвращаемое значение должно
быть равно 0.
"""


def longest_palindrome(s: str) -> int:
    """Поиск в строке длины максимального палиндрома"""
    res = 0
    for i in range(len(s)):
        for x in range(i+1, len(s)+1):
            val = s[i:x]
            if val == val[::-1]:
                res = max(res, len(val))

    return res


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ("a", 1),
        ("aa", 2),
        ("baa", 2),
        ("aab", 2),
        ("abcdefghba", 1),
        ("baablkj12345432133d", 9),
    )

    for key, val in data:
        assert longest_palindrome(key) == val


if __name__ == '__main__':
    test()
