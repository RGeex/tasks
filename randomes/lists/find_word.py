"""
Напишите функцию, которая определяет, является ли строка допустимым
предположением на доске Boggle в соответствии с правилами Boggle.
Доска Boggle представляет собой двумерный массив отдельных символов,
например:

[ ["I","L","A","W"],
  ["B","N","G","E"],
  ["I","U","A","O"],
  ["A","S","R","L"] ]

Допустимые предположения — это строки, которые можно сформировать путем
соединения соседних ячеек (по горизонтали, вертикали или диагонали) без
повторного использования ранее использованных ячеек.

Например, на приведенной выше доске «BINGO», «LINGO» и «ILNBIA» будут
действительными догадками, а «BUNGIE», «BINS» и «SINUS» — нет.

Ваша функция должна принимать два аргумента (двумерный массив и строку)
и возвращать true или false в зависимости от того, найдена ли строка в
массиве согласно правилам Boggle.

Тестовые случаи будут обеспечивать различные размеры массивов и строк
(квадратные массивы до 150x150 и строки до 150 заглавных букв). Вам не
нужно проверять, является ли строка реальным словом или нет, только если
это верное предположение.
"""


def find_word(board: list[list[str]], word: str) -> bool:
    """
    Проверяет, возможно ли составить заданное слово на доске Boggle.
    """
    db = {w: [x for n in [[(i, j) for j, x in enumerate(ln) if x == w] for i, ln in enumerate(board) if w in ln] for x in n] for w in word}

    def fn(s: str, pos: None | list = None):
        """
        Осуществляет рекурсивный поиск возможности составления слова.
        """
        for cur in db.get(s[0], []):
            if not pos or all(abs(a - b) < 2 for a, b in zip(pos[-1], cur)) and cur not in pos:
                if not s[1:] or fn(s[1:], (pos or []) + [cur]):
                    return True
        return False
    return fn(word)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    testBoard = [
        ["E","A","R","A"],
        ["N","L","E","C"],
        ["I","A","I","S"],
        ["B","Y","O","R"]
    ]
    data = ( 
        ((testBoard, "C"               ), True),
        ((testBoard, "EAR"             ), True),
        ((testBoard, "EARS"            ), False),
        ((testBoard, "BAILER"          ), True),
        ((testBoard, "RSCAREIOYBAILNEA"), True),
        ((testBoard, "CEREAL"          ), False),
        ((testBoard, "ROBES"           ), False),
    )
    for key, val in data:
        assert find_word(*key) == val


if __name__ == '__main__':
    test()
