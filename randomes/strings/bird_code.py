"""
В мире птицеводства существуют четырехбуквенные коды общепринятых названий
птиц. Эти коды создаются по нескольким простым правилам:

    Если в названии птицы есть только одно слово, код состоит из первых
    четырех букв этого слова.
    Если имя состоит из двух слов, код принимает первые две буквы каждого
    слова.
    Если имя состоит из трех слов, код создается путем взятия первой буквы
    первых двух слов и первых двух букв третьего слова.
    Если имя состоит из четырех слов, в коде используются первые буквы всех
    слов.

(Есть и другие способы создания кодов, но в этом Ката будут использоваться
только четыре правила, перечисленные выше)

Завершите функцию, которая принимает массив строк с распространенными
названиями птиц из Северной Америки, и создайте коды для этих названий на
основе приведенных выше правил. Функция должна возвращать массив кодов в
том же порядке, в котором были представлены входные имена.

Дополнительные соображения:

    Четырехбуквенные коды в возвращаемом массиве должны быть в ВЕРХНЕМ
    РЕГИСТРЕ.
    Если общее имя содержит дефис/тире, его следует рассматривать как
    пробел.

Пример

Если входной массив: ["Black-Capped Chickadee", "Common Tern"]

Возвращаемый массив будет: ["BCCH", "COTE"]
"""


def bird_code(arr: list[str]) -> list[str]:
    """
    Создает аббривиатуры из заданных строк.
    """
    return [''.join([x[:[4 // ln, 2][ln == 3 and i == 2]] for i, x in enumerate(w)]).upper() for x in arr if (ln := len(w := x.replace('-', ' ').split()))]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (["American Redstart", "Northern Cardinal", "Pine Grosbeak", "Barred Owl", "Starling", "Cooper's Hawk", "Pigeon"], ["AMRE","NOCA","PIGR","BAOW","STAR","COHA","PIGE"]),
        (["Great Crested Flycatcher", "Bobolink", "American White Pelican", "Red-Tailed Hawk", "Eastern Screech Owl", "Blue Jay"], ["GCFL","BOBO","AWPE","RTHA","ESOW","BLJA"]),
        (["Black-Crowned Night Heron", "Northern Mockingbird", "Eastern Meadowlark", "Dark-Eyed Junco", "Red-Bellied Woodpecker"], ["BCNH","NOMO","EAME","DEJU","RBWO"]),
        (["Scarlet Tanager", "Great Blue Heron", "Eastern Phoebe", "American Black Duck", "Mallard", "Canvasback", "Merlin", "Ovenbird"], ["SCTA","GBHE","EAPH","ABDU","MALL","CANV","MERL","OVEN"]),
        (["Fox Sparrow", "White-Winged Crossbill", "Veery", "American Coot", "Sora", "Northern Rough-Winged Swallow", "Purple Martin"], ["FOSP","WWCR","VEER","AMCO","SORA","NRWS","PUMA"]),
    )
    for key, val in data:
        assert bird_code(key) == val


if __name__ == '__main__':
    test()
