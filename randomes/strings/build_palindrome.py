"""
Задача

Учитывая строку str, найдите кратчайшую возможную строку, которую можно получить,
добавив символы в конец исходной строки, чтобы сделать ее палиндромом.
Пример

Для str = "abcdc", вывод должен быть "abcdcba".
"""


def build_palindrome(s: str) -> str:
    """
    Находит самую короткую строку, добавив которую к исхдной получится палиндром и возвращает палиндром.
    """
    return next((x for i in range(-1, len(s) + 1) if (x := s + [s[i::-1], ''][i < 0]) == x[::-1]), '')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("ccc", "ccc"),
        ("abcdc", "abcdcba"),
        ("ababab", "abababa"),
    )
    for key, val in data:
        assert build_palindrome(key) == val


if __name__ == '__main__':
    test()
