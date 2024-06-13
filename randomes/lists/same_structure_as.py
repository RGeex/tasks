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


from itertools import zip_longest


def same_structure_as(original: list, other: list) -> bool:
    """
    Проверяет 2 списка на идентичную вложенность по типу элементов.
    """
    stack = [[original, other]]
    while stack:
        cur = stack.pop()
        for x in zip_longest(*cur):
            if len(set(map(type, x))) != 1:
                return False
            if all(isinstance(n, list) for n in x):
                stack.append(x)
    return True


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([1, [1, 1]], [2, [2, 2]]), True),
        (([1, [1, 1]], [[2, 2], 2]), False),
    )
    for key, val in data:
        assert same_structure_as(*key) == val


if __name__ == '__main__':
    test()
