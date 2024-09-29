"""
Задача

Учитывая строку цифр, верните самую длинную подстроку с чередующимися
odd/even или even/odd digits. Если две или более подстроки имеют одинаковую
длину, верните подстроку, которая встречается первой.
Примеры

longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.

longest_substring("20") ➞ "2"

longest_substring("") ➞ ""

Входные ограничения

    0 <= len(цифры) <= 10^5
"""


def longest_substring(s: str) -> str:
    """
    Возвращает самую длинную подстроку с чередующимися чет/нечет. цифрами.
    """
    return max([s[i:i + next((k - int(x) % 2 for k, n in enumerate(s[i:], int(x) % 2) if int(n) % 2 != k % 2), len(s[i:]))] for i, x in enumerate(s)], key=len, default='')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("225424272163254474441338664823", "272163254"),
        ("594127169973391692147228678476", "16921472"),
        ("721449827599186159274227324466", "7214"),
        ("20", "2"),
        ("", ""),
    )
    for key, val in data:
        assert longest_substring(key) == val


if __name__ == '__main__':
    test()
