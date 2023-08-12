"""
Написать функцию, которая возвращает возможные ходы шахматной ферзя.
Возвращаемое значение должно быть списком с возможными ходами,
отсортированными по алфавиту, исключая начальную позицию.
"""


def available_moves(pos: str) -> list:
    """Поиск всех возможных ходов ферзя с заданной позиции."""
    res = set()
    if isinstance(pos, str) and len(pos) == 2:
        a, b = int(pos[1]) - 1, ord(pos[0]) % 65
        if all(x in range(8) for x in (a, b)):
            # row and col
            for x in range(8):
                res |= {(a, x), (x, b)}
            # diagonal
            for x in range(2):
                k = 7 - b if x else b
                m, n = [v - min(a, k) for v in (a, k)]
                res |= {(m + v, abs(7 * x - (n + v))) for v in range(8-max(m, n))}
            res = [f'{chr(b+65)}{a+1}' for a, b in res - {(a, b)}]
    return sorted(res)


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ["C5", ["A3", "A5", "A7", "B4", "B5", "B6", "C1", "C2", "C3", "C4", "C6",
                "C7", "C8", "D4", "D5", "D6", "E3", "E5", "E7", "F2", "F5", "F8",
                "G1", "G5", "H5"]],
        ["A1", ["A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "C1",
                "C3", "D1", "D4", "E1", "E5", "F1", "F6", "G1", "G7", "H1", "H8"]],
        ["H3", ["A3", "B3", "C3", "C8", "D3", "D7", "E3", "E6", "F1", "F3",
                "F5", "G2", "G3", "G4", "H1", "H2", "H4", "H5", "H6", "H7", "H8"]],
        [[1, 2, 3], []],
        ["work?", []],
        ["A10", []],
        ["B0", []],
        [None, []],
        [2, []],
    )
    for key, val in data:
        assert available_moves(key) == val


if __name__ == '__main__':
    test()
