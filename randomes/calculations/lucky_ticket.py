"""
Создайте функцию, которая вычисляет количество строк из n цифр с одинаковой суммой
для первой и второй половины их цифр. Эти цифры называются «счастливыми».

Примеры

Input: 2 ➞ Output: 10
# "00", "11", "22", "33", "44", "55", "66", "77", "88", "99"

Input: 4 ➞ Output: 670

Input: 6 ➞ Output: 55252
# "000000", "001010", "112220", ..., "999999"

Примечания
    Значение nвсегда будет четным.
    2 <= n <= 150
    Чтобы избежать жесткого кодирования, предел вашего кода должен составлять <= 250 символов.
"""

from collections import Counter


def lucky_ticket1(n: int) -> int:
    """
    Кол-во счастливых билетов в N значном билете.
    """
    return sum(x ** 2 for x in Counter(sum(map(int, str(x))) for x in range(10 ** (n // 2))).values())


def lucky_ticket2(n: int) -> int:
    """
    Кол-во счастливых билетов в N значном билете.
    """
    tmp = [1] * 10 + [0] * (n // 2 * 9 - 9)
    for _ in range(n // 2 - 1):
        tmp = [sum(tmp[:i + 1]) if i < 10 else sum(tmp[i - 9:i + 1])
               for i in range(len(tmp))]
    return sum(i ** 2 for i in tmp)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (2, 10),
        (4, 670),
        (6, 55252)
    )
    for key, val in data:
        assert lucky_ticket1(key) == val
        assert lucky_ticket2(key) == val


if __name__ == '__main__':
    test()
