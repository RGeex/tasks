"""
Учитывая положительное целое число n, возвращает первые n цифр
последовательности Туэ-Морса в виде строки (см. примеры).

Последовательность Туэ-Морса — это двоичная последовательность с 0 в качестве
первого элемента. Остальная часть последовательности получается добавлением
логического (двоичного) дополнения к полученной на данный момент группе.

For example:

0
01
0110
01101001
and so on...

все

Бывший.:

 1 --> "0"
 2 --> "01"
 5 --> "01101"
10 --> "0110100110"

    Вам не нужно проверять, является ли n допустимым — оно всегда будет
    положительным целым числом.
    n будет между 1 и 10000
"""


def thue_morse(n: int, r: str='0') -> str:
    """
    Выводит последовательнсть Туэ-Морса заданной длины.
    """
    return r if len(r) == n else thue_morse(n, (r + ''.join([str(int(not int(x))) for x in r]))[:n])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1, "0"),
        (2, "01"),
        (5, "01101"),
        (10, "0110100110"),
        (100, "0110100110010110100101100110100110010110011010010110100110010110100101100110100101101001100101100110"),
    )
    for key, val in data:
        assert thue_morse(key) == val


if __name__ == '__main__':
    test()
