"""

Радж должен был подняться по лестнице с заданным номером (n).
Помогите ему добраться до вершины, используя функцию лестницы.

Иметь ввиду :

Если n<1, то вернуть ' '.
Перед началом лестницы много пробелов:

pattern(6)
                    1 1
                1 2 2 1
            1 2 3 3 2 1
        1 2 3 4 4 3 2 1
    1 2 3 4 5 5 4 3 2 1
1 2 3 4 5 6 6 5 4 3 2 1
"""


def stairs(n: int) -> str:
    """Возвращает лестницу, учитывая пробелы"""
    outs = []
    for line in range(1, n + 1):
        data = ' '.join('1234567890'[k % 10] for k in range(line))
        outs.append(f"{'    ' * (n - line)}{data} {data[::-1]}")

    return '\n'.join(outs) or ' '


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        (0, " "),
        (1, '1 1'),
        (2, '    1 1\n1 2 2 1'),
        (3, '        1 1\n    1 2 2 1\n1 2 3 3 2 1'),
        (4, '            1 1\n        1 2 2 1\n    1 2 3 3 2 1\n1 2 3 4 4 3 2 1'),
    )

    for key, val in data:
        assert stairs(key) == val


if __name__ == '__main__':
    test()