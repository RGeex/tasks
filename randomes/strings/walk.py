"""
Вы робот.

Как робот, вы запрограммированы на прогулки по тропинке.

Путь вводится в виде строки из следующих символов, где:

    "^" -> шаг вперед
    "v" -> уйти в отставку
    ">" -> шаг вправо
    "<" -> шаг влево

Например, правильный путь будет выглядеть так:

"^^vv>><<^v>"

Однако вы робот, который не может понять эту строку символов, просто взглянув
на нее. Вам нужны подробные инструкции о том, как следовать по пути.

Ваша цель — написать программу, преобразующую входной путь в набор подробных и
читаемых инструкций, которые сможет понять даже такой робот, как вы.

Для этого необходимо перевести предыдущий пример

"^^vvvv>><<^v>"

на «строку, разделенную переводом строки», эквивалентную:

Take 2 steps up
Take 4 steps down
Take 2 steps right
Take 2 steps left
Take 1 step up
Take 1 step down
Take 1 step right

Обратите внимание, что группы одних и тех же символов преобразуются только в
одну инструкцию, предписывающую вам выполнить несколько шагов.

Примечания:

    Входной путь НИКОГДА не будет содержать недопустимые символы, только
    четыре символа для направлений.

    Строки инструкций разделяются только новой строкой ( "\n") характер. Этот
    символ отсутствует ни в начале первой командной строки, ни в конце
    последней командной строки.

    Пустой путь без символов должен выводить "Paused" строка, означающая, что
    вы, робот, не должны никуда двигаться и находитесь в состоянии паузы.
"""


from itertools import groupby as gb


def walk(path: str) -> str:
    """
    По переданным стрелкам направления расписывает кол-во шагов.
    """
    return '\n'.join([f'Take {(n := len(list(b)))} step{["", "s"][n > 1]} {dict(zip("^v><", "up down right left".split()))[a]}' for a, b in gb(path)]) or 'Paused'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("^", "Take 1 step up"),
        ("v", "Take 1 step down"),
        (">>", "Take 2 steps right"),
        ("<<>", "Take 2 steps left\nTake 1 step right"),
        ("", "Paused"),
    )
    for key, val in data:
        assert walk(key) == val


if __name__ == '__main__':
    test()
