"""
Четыре в ряд.

Правила игры: игроки ходят по очереди, добавляя к любому ряду,
не заполненному, фишку своего цвета. Игра закончится, если один
из игроков соберет 4 фишки своего цвета, по горизонтали,
вертикали, диагонали или не останется ходов.

Дана последовательность очередности ходов игроков,
необходимо определить победителя или вывести Ничья.

Длина последовательности не превышает размер игрового поля
6 х 7, где 6 ряды, 7 столбцы.
"""


def diagonals(grid: list) -> list:
    """Значения диагоналей игрового поля."""
    lst = []
    for i, val in enumerate(grid):
        for j in range(int(bool(i)) or len(val)):
            tmp = []
            for k in range(len(val) - int(j or (i and i - 1))):
                tmp.append(grid[i+k][j+k])
            lst.append(tmp)

    return lst


def who_win(grid: list) -> str | bool:
    """Поиск 4 подряд значений одного из игроков."""
    data = [
        grid,
        zip(*grid),
        diagonals(grid),
        diagonals(grid[::-1]),
    ]
    for lines in data:
        for line in lines:
            prev, count = 0, 1
            for val in line:
                count = int(prev and val == prev and count) + 1
                if count == 4:
                    return val
                prev = val

    return False


def who_is_winner(pieces_position_list: list[str]) -> str:
    """Определение победителя по входящему списку последовательности ходов."""

    # создание пустого поля 6 х 7
    grid = [[0] * 6 for _ in range(7)]
    temp = ['Red', 'Yellow']

    # заполнение поля значениями из последовательности
    for cur in pieces_position_list:
        # парсинг строки
        col, val = [(x in temp and x) or ord(x) - ord('A') for x in cur.split('_')]
        # заполнение поля
        grid[col][len(list(filter(bool, grid[col])))] = val

        # поиск победителя
        if winner := who_win(grid):
            return winner

    return 'Draw'


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red",
        "B_Yellow", "G_Red", "C_Yellow", "C_Red", "D_Yellow", "F_Red",
        "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red",
        "F_Yellow", "D_Red", "B_Yellow", "E_Red", "D_Yellow", "A_Red",
        "G_Yellow", "D_Red", "D_Yellow", "C_Red",
    ]

    assert who_is_winner(data) == 'Yellow'


if __name__ == '__main__':
    test()
