"""
Пара перчаток

Приближается зима, пора готовиться к лыжному отдыху. Цель этого ката —
определить количество пар перчаток, которые вы можете составить из
перчаток, имеющихся в вашем ящике.

Учитывая массив, описывающий цвет каждой перчатки, верните количество пар,
которые вы можете составить, предполагая, что только перчатки одного цвета
могут образовывать пары.
Примеры:

input = ["red", "green", "red", "blue", "blue"]
result = 2 (1 red pair + 1 blue pair)

input = ["red", "red", "red", "red", "red", "red"]
result = 3 (3 red pairs)
"""


from collections import Counter


def number_of_pairs(gloves: list[str]) -> int:
    """
    Учитывя список перчаток, определяет кол-во имеющихся пар,
    определением пары является цвет.
    """
    return sum(x // 2 for x in Counter(gloves).values() if 1 < x)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (["red","red"], 1),
        (["red","green","blue"], 0),
        (["gray","black","purple","purple","gray","black"], 3),
        ([], 0),
        (["red","green","blue","blue","red","green","red","red","red"], 4),
    )
    for key, val in data:
        assert number_of_pairs(key) == val


if __name__ == '__main__':
    test()
