"""
Можно ли вычислить куб как сумму?

В этой Ката вам будет присвоен номер n(где n >= 1) и ваша задача найти nпоследовательные нечетные
числа, сумма которых в точности равна кубу n.

Математически:
куб = n**3
сумма = a1 + a2 + a3 + ..... + an
сумма == куб
а2 == а1 + 2, а3 == а2 + 2, .......

Например:

find_summands(3) = [7,9,11] # because 7 + 9 + 11 = 27, the cube of 3. Note that there are only
n = 3 elements in the array.

Функция записи findSummands(n)который вернет массив из n последовательных нечетных чисел с суммой,
равной кубу n (n*n*n).
"""


def find_summands(n: int) -> list:
    """
    Декомпозиция куба числа на сумму нечетных чисел.
    """
    x, r = n ** 3, []

    for i in range(1, x + 1, 2):
        if sum(r) < x:
            r.append(i)
        if sum(r) > x:
            r.pop(0)
        if sum(r) == x:
            return r


data = (
    (1, [1]),
    (3, [7, 9, 11]),
    (4, [1, 3, 5, 7, 9, 11, 13, 15]),
)
for key, val in data:
    assert find_summands(key) == val
