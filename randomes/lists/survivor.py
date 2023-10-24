"""
Чангу и Мангу — отличные друзья. Однажды они нашли бесконечную бумагу,
на которой было написано 1,2,3,4,5,6,7,8,......до бесконечности.

Им обоим не понравилась последовательность, и они начали удалять некоторые
числа следующим образом.

First they deleted every 2nd number.

So remaining numbers on the paper: 1,3,5,7,9,11..........till infinity.

Then they deleted every 3rd number.

So remaining numbers on the paper: 1,3,7,9,13,15..........till infinity..

Then they deleted every 4th number.

So remaining numbers on the paper: 1,3,7,13,15..........till infinity.

Затем продолжали это делать (удаляя каждый 5-й, затем каждый 6-й...), пока они
не состарились и не умерли.

Очевидно, что некоторые числа никогда не будут удалены (например, 1,3,7,13..)
и, следовательно, известны нам как оставшиеся в живых.

Учитывая число n, проверьте, является ли это номером выжившего или нет.
Ввод, вывод

    [input]целое число n

0 < n <= 10^8

    [output]логическое значение

trueесли номер выживший, иначе false.
"""


def survivor1(n: int) -> bool:
    """
    Принадлежит ли число последовательности.
    Метод перебора списка.
    """
    arr, x = list(range(1, n + 1)), 2
    while x <= len(arr):
        arr = [v for i, v in enumerate(arr, 1) if i % x]
        x += 1
    return n in arr


def survivor2(n: int, s: int = 2) -> bool:
    """
    Принадлежит ли число последовательности.
    Метод вычисления с помощью рекурсии.
    """
    if not n % s:
        return False
    if n < s:
        return True
    return survivor2(n - n // s, s + 1)


def survivor3(n: int) -> bool:
    """
    Принадлежит ли число последовательности.
    Метод вычисления с цикла.
    """
    s = 2
    while s <= n and n % s:
        n -= n // s
        s += 1
    return n % s > 0


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1, True),
        (5, False),
        (8, False),
        (9, False),
        (13, True),
        (15, False),
        (134, False),
        (289, True),
    )
    for key, val in data:
        assert survivor1(key) == val
        assert survivor2(key) == val
        assert survivor3(key) == val


if __name__ == '__main__':
    test()
