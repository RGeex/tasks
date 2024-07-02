"""
Учитывая массив arrстрок, завершите функцию, вычислив общий периметр всех
островов. Каждый участок земли будет отмечен знаком 'X' а водные поля
представлены как 'O'. Считайте каждую плитку идеальной 1 x 1кусок земли.
Несколько примеров для лучшей визуализации:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO'] 

который представляет собой:

должен вернуться: "Total land perimeter: 24".

Следующий ввод:

['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']

который представляет собой:

должен вернуться: "Total land perimeter: 18"
"""


def land_perimeter(arr: list[str]) -> str:
    """
    Вычисляет периметр островов.
    """
    res, tmp = 0, []
    for i, x in enumerate(arr):
        for j, y in enumerate(x):
            res, tmp = res + (sum(abs(i - a) + abs(j - b) == 1 for a, b in tmp) if y == 'X' else 0), tmp + [[], [(i, j)]][y == 'X']
    return f'Total land perimeter: {len(tmp) * 4 - res * 2}'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"], "Total land perimeter: 60"),
        (["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"], "Total land perimeter: 52"),
        (["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"], "Total land perimeter: 40"),
        (["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"], "Total land perimeter: 54"),
        (["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"], "Total land perimeter: 40"),
    )
    for key, val in data:
        assert land_perimeter(key) == val


if __name__ == '__main__':
    test()
