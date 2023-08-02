"""
Вы ставите коня и короля на доску.

Завершите метод, который говорит нам, какой из них может захватить другой.

Вам предоставляется массив из двух объектов; каждый содержит целое число
(ранг, первый элемент) и строку/символ (файл, второй элемент),
чтобы показать положение фигур на шахматной доске.

Вернуть:
"Knight" если конь ставит короля под шах,
"King" если король атакует коня,
"None" если ничего из вышеперечисленного не происходит.

"""

from operator import sub


def knight_vs_king(king: tuple, knight: tuple) -> str:
    """
    Определяет по установленным на поле фигурам (конь и король),
    может ли кто либо из нихнапасть на второго.
    """

    outs = []
    data = {(0, 1): 'King', (1, 1): 'King', (1, 2): 'Knight'}

    for pos in zip(king, knight):
        temp = abs(sub(*map(ord, map(str, pos))))
        outs.insert(not outs or outs[0] < temp, temp)

    return data.get(tuple(outs), 'None')


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        (((2, "F"), (6, "B")), "None"),
        (((7, "B"), (6, "C")), "King"),
        (((4, "C"), (6, "D")), "Knight"),
    )
    for key, val in data:
        assert knight_vs_king(*key) == val


if __name__ == '__main__':
    test()
