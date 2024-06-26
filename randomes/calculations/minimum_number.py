"""
Задача :

Учитывая список из n целых чисел , найдите минимальное число , которое нужно
вставить в список , чтобы сумма всех элементов списка равнялась ближайшему
простому числу .
Примечания

    Размер списка не менее 2 .

    Числа списка будут только положительными (n > 0).

    повторение чисел в списке Возможно .

    Сумма нового списка должна равняться ближайшему простому числу .
"""


def minimum_number(numbers: list[int]) -> int:
    """
    Поиск недостающего числа в списке до ближайшего простого числа
    суммы всех чисел списка.
    """
    a = b = sum(numbers)
    while next((1 for x in range(2, a) if not a % x), 0):
        a += 1
    return a - b


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([5,2], 0),
        ([1,1,1], 0),
        ([3,1,2], 1),
        ([2,12,8,4,6], 5),
        ([50, 39, 49, 6, 17, 28], 2)
    )
    for key, val in data:
        assert minimum_number(key) == val


if __name__ == '__main__':
    test()
