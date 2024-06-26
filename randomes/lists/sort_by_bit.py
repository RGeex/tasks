"""
В этом ката вам предстоит отсортировать массив 32-битных целых чисел в порядке
возрастания количества имеющихся в них битов .

Например, учитывая массив [7, 6, 15, 8]

    7 имеет 3 бита (000...0 111 )
    6 имеет 2 бита (000...0 11 0)
    15 имеет 4 бита (000... 1111 )
    8 имеет 1 бит (000... 1 000)

Таким образом, отсортированный массив будет иметь вид [8, 6, 7, 15] .

В тех случаях, когда два числа имеют одинаковое количество бит, вместо этого
сравните их реальные значения.

Например, между 10 (...1010) и 12 (...1100) они оба имеют одинаковое
количество битов ' 2 ', но целое число 10 меньше 12, поэтому оно идет
первым в отсортированном порядке.

Ваша задача — написать функцию, которая принимает массив целых чисел и
сортирует их, как описано выше.

Примечание. Ваше решение должно сортировать массив на месте .

Пример:

[3, 8, 3, 6, 5, 7, 9, 1]   =>    [1, 8, 3, 3, 5, 6, 9, 7]
"""

def sort_by_bit(arr: list[int]) -> list[int]:
    """
    Сортирует список чисел по кол-ву бит в нем, по номиналу. 
    """
    return sorted(arr, key=lambda x: (sum(map(int, f'{x:b}')), x))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([3, 8, 3, 6, 5, 7, 9, 1], [1, 8, 3, 3, 5, 6, 9, 7]),
        ([9,4,5,3,5,7,2,56,8,2,6,8,0], [0, 2, 2, 4, 8, 8, 3, 5, 5, 6, 9, 7, 56]),
    )
    for key, val in data:
        assert sort_by_bit(key) == val


if __name__ == '__main__':
    test()
