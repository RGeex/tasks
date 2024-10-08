"""
Вам нужно поиграться с предоставленной строкой(ами).

Переместите согласные буквы вперед на 9 позиций в алфавите. Если они пройдут
«z», начните снова с «а».

Переместите гласные буквы на 5 мест назад по алфавиту. Если они пройдут «а»,
начните снова с «z». Для наших польских друзей эта ката не считает «у» гласной.

Исключения:

Если это символ «c» или «o», переместите его на 1 место назад. Для «d»
переместите его назад на 3, а для «e» — на 4 назад.

Если перемещенная буква становится «c», «o», «d» или «e», верните ей исходное
значение.

Предоставленная строка всегда будет в нижнем регистре, не будет пустой и не
будет содержать специальных символов.
"""


def vowel_back1(s: str) -> str:
    """
    Заменяет буквы в строке по заданным правилам.
    """
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "vkbaafpqistuvwnyzabtpvfghi"))


def vowel_back2(s: str) -> str:
    """
    Заменяет буквы в строке по заданным правилам.
    """
    return ''.join([x if (w := chr((ord(x) - 97 + [[[[9, -5][x in 'aiu'], -1][x in 'co'], -3][x == 'd'], -4][x == 'e']) % 26 + 97)) in 'code' else w for x in s.lower()])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("testcase", "tabtbvba"),
        ("codewars", "bnaafvab"),
        ("exampletesthere", "agvvyuatabtqaaa"),
    )
    for key, val in data:
        assert vowel_back1(key) == val
        assert vowel_back2(key) == val


if __name__ == '__main__':
    test()
