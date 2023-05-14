"""
Каждый следующий элемент ряда Фибоначчи получается при сложении
двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не
превышают четыре миллиона.
"""

from typing import Generator


def fibonacci() -> Generator:
    """Генератор бесконечного ряда чисел Фибоначчи"""
    n1, n2 = 1, 2
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


def get_fib_lst(num: int, *_, limit: bool = False):
    """Генерирует список чисел фибоначи:
    если limit == True, то num ограничивает max значение,
    если limit == False, то num ограничивает длинну списка"""
    lst = []
    for i, data in enumerate(fibonacci()):
        if (not limit and i == num) or (limit and data > num):
            break
        lst.append(data)
    return lst


def sums(*args, **kwargs):
    """Подсчитывает сумму всех четных элементов ряда Фибоначчи."""
    return sum(i for i in get_fib_lst(*args, **kwargs) if not i % 2)


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert get_fib_lst(10) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert get_fib_lst(22, limit=True) == [1, 2, 3, 5, 8, 13, 21]
    assert sums(4_000_000, limit=True) == 4613732


if __name__ == '__main__':
    test()
