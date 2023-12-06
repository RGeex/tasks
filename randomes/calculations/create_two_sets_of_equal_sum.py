"""
Задача

Если возможно, разделите целые числа 1,2,…,n на два набора одинаковой суммы.
Вход

Положительное целое число n <= 1 000 000.
Выход

Если это невозможно, верните []
Примеры:

Для n = 8 действительные ответы включают:

[1, 3, 6, 8], [2, 4, 5, 7] (или [[1, 3, 6, 8], [2, 4, 5, 7]])

[8, 1, 3, 2, 4], [5, 7, 6]

[7, 8, 3], [6, 1, 5, 4, 2] и другие.

Для n = 9 это невозможно. Например, попробуйте [6, 8, 9] и [1, 2, 3, 4, 5, 7],
но первая сумма равна 23, а вторая — 22. Никакие другие наборы тоже не работают.
"""


def create_two_sets_of_equal_sum1(n: int) -> list:
    """
    Деление списка числе на 2 равные части по их сумме, если это возможно.
    """
    tmp, lst, res = 0, range(n, 0, -1), []
    if not (s := sum(range(1, n + 1))) % 2:
        x = s // 2
        for i in lst:
            if tmp + i <= x:
                res.append(i)
                tmp += i
        res = [res, list(set(lst) - set(res))]
    return res


def create_two_sets_of_equal_sum2(n: int) -> list:
    """
    Деление списка числе на 2 равные части по их сумме, если это возможно.
    """
    r = [*range(1, n + 1)]
    a = r[0::4] + r[1+2*(n % 2 == 0)::4]
    b = r[2::4] + r[1+2*(n % 2 != 0)::4]
    return [a, b] if sum(a) == sum(b) else []


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    for n in range(1, 100):
        x, s = divmod(sum(range(1, n + 1)), 2)
        tmp1 = create_two_sets_of_equal_sum1(n)
        tmp2 = create_two_sets_of_equal_sum2(n)
        assert not tmp1 if s else all(sum(i) == x for i in tmp1)
        assert not tmp2 if s else all(sum(i) == x for i in tmp2)


if __name__ == '__main__':
    test()
