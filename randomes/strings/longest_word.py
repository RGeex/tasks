"""
#Деталь

«Обратный отсчет» — британское игровое шоу с головоломками с числами и словами.
Раунд с буквами состоит из того, что участник выбирает 9 перетасованных букв -
либо из стопки гласных, либо из стопки согласных. Участникам дается 30 секунд,
чтобы попытаться придумать самое длинное английское слово, которое они могут
придумать, из имеющихся букв - буквы не могут использоваться более одного раза,
если нет другого такого же символа.

#Задача

Учитывая строку из 9 букв в верхнем регистре, letters, найдите самое длинное
слово, которое можно составить из некоторых или всех букв. Предварительно
загруженный массив words (или $words в Ruby) содержит кучу слов в верхнем
регистре, которые вам придется перебирать. Возвращайте только самое длинное
слово; если их несколько, верните слова одинаковой длины в алфавитном порядке.
Если из данных букв нет слов, которые можно составить, верните None/nil/null.

##Примеры

letters = "ZZZZZZZZZ"
longest word = None

letters = "POVMERKIA", 
longest word = ["VAMPIRE"]

letters = "DVAVPALEM"
longest word = ["VAMPED", "VALVED", "PALMED"]
"""


from collections import Counter


words = [
    'ALIBI', 'BAIL', 'BALL', 'BEAT', 'BILL', 'BITE', 'BRAIN',
    'BUOYS', 'BUSES', 'BYTE', 'CAGES', 'CAUSE', 'CAVES', 'CODERS',
    'DATA', 'DATE', 'DATES', 'DECAY', 'DOSES', 'FEED', 'FIRE',
    'FORCES', 'GAME', 'GASOLINE', 'GATE', 'GATES', 'GUEST', 'HERE',
    'ISSUE', 'IVORY', 'KEEL', 'KILL', 'LABOR', 'LOOK', 'LORAN',
    'NEED', 'OCEANS', 'PAIL', 'RAISE', 'REASON', 'SAILS', 'SALES',
    'SEALS', 'SECOND', 'SLEDS', 'SOLES', 'STAGE', 'TODAY', 'TOWER',
    'TRADE', 'USAGE', 'VIEW', 'WAGE', 'WATER', 'WEEK', 'WIRE',
    'WIRES', 'YOLK',
]


def longest_word(letters: str) -> list[str] | None:
    """
    Поиск в словаре слов, которые можно составить из заданных букв.
    """
    arr = [(len(word), word) for word in words if not Counter(word) - Counter(letters)]
    return [word for n, word in arr if n == max(arr)[0]] or None


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = [
        ('GQEMAUVXY', ['GAME']),
        ('TDWAYZROE', ['TODAY', 'TOWER', 'TRADE', 'WATER']),
        ('EAEEAYITB', ['BEAT', 'BITE', 'BYTE']),
        ('AKUIYOOLO', ['LOOK', 'YOLK']),
        ('GVDTCAESU', ['CAGES', 'CAUSE', 'CAVES', 'DATES', 'GATES', 'GUEST', 'STAGE', 'USAGE']),
        ("WTGAEUAUD", ['DATA', 'DATE', 'GATE', 'WAGE']),
        ("MVIIIZEKQ", None),
        ("SIARIERRW", ['RAISE', 'WIRES']),
        ("YIOVOORUF", ['IVORY']),
        ("EWFEREIUH", ['FIRE', 'HERE', 'WIRE']),
        ("NLGIEOTSA", ['GASOLINE']),
        ("ASIULSIEI", ['ISSUE', 'SAILS', 'SALES', 'SEALS']),
        ("AFDEEONEA", ['FEED', 'NEED']),
        ("OFRDACESN", ['CODERS', 'FORCES', 'OCEANS', 'REASON', 'SECOND']),
        ("YBOEDSLSU", ['BUOYS', 'BUSES', 'DOSES', 'SLEDS', 'SOLES']),
        ("GIABBLPBL", ['BAIL', 'BALL', 'BILL', 'PAIL']),
        ("RAOQILBIN", ['ALIBI', 'BRAIN', 'LABOR', 'LORAN']),
        ("KIEWVELIL", ['KEEL', 'KILL', 'VIEW', 'WEEK']),
        ("DDAYCEEQR", ['DECAY']),
    ]
    for key, val in data:
        assert longest_word(key) == val


if __name__ == '__main__':
    test()
