"""
Завершите функцию/метод (в зависимости от языка), чтобы вернуться true/ True
когда его аргументом является массив, имеющий ту же структуру вложенности и
соответствующую длину вложенных массивов, что и первый массив.

Например:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""


from itertools import zip_longest as zl


def same_structure_as(*x: list) -> bool:
    """
    Проверяет 2 списка на идентичную вложенность по типу элементов.
    """
    return not set(map(type, x))-{list} and all(len(c)-2 and same_structure_as(*n) if list in (c:=set(map(type, n))) else len(set(map(len, x)))-2 for n in zl(*x))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([], 1), False),
        (([1, [1, 1]], [2, [2]]), False),
        (([1, [1, 1]], [2, [2, 2]]), True),
        (([1, [1, 1]], [[2, 2], 2]), False),
        (([1, '[', ']'], ['[', ']', 2]), True),
    )
    for key, val in data:
        assert same_structure_as(*key) == val


if __name__ == '__main__':
    test()
