"""
Джон пригласил нескольких друзей. Его список:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;
Raphael:Corwill;Alfred:Corwill";

Не могли бы вы сделать программу, которая

    делает эту строку прописной
    отсортирует его в алфавитном порядке по фамилии.

Если фамилии совпадают, отсортируйте их по имени. Фамилия и имя гостя
указываются в круглых скобках, разделенных запятой.

Итак, результат функции meeting(s)будет:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL,
BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

Может случиться так, что в двух разных семьях с одной и той же фамилией два
человека тоже будут иметь одно и то же имя.
Примечания

    Другие примеры вы можете увидеть в разделе «Примеры тестов».
"""


def meeting(s: str) -> str:
    """
    Сортирует строку по фамилии и имени и форматирует в заданный форма, полученный результат.
    """
    return ''.join(sorted([f"({', '.join(x.split(':')[::-1])})" for x in s.upper().split(';')]))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn", 
        "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)"),
        ("John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Steve;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell", 
        "(BELL, MEGAN)(CORNWELL, AMBER)(DORNY, JAMES)(DORRIES, PAUL)(GATES, JOHN)(KERN, ANN)(KORN, ANNA)(META, ALEX)(RUSSEL, ELIZABETH)(STEVE, LEWIS)(WAHL, MICHAEL)"),
        ("Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:Dorries;Ann:Kern;Haley:Arno;Paul:Dorny;Madison:Kern", 
        "(ARNO, ALEX)(ARNO, HALEY)(BELL, SARAH)(CORNWELL, ALISSA)(DORNY, PAUL)(DORRIES, ANDREW)(KERN, ANN)(KERN, MADISON)"),
        ("Anna:Wahl;Grace:Gates;James:Russell;Elizabeth:Rudd;Victoria:STAN;Jacob:Wahl;Alex:Wahl;Antony:Gates;Alissa:Meta;Megan:Bell;Amandy:Stan;Anna:Steve", 
        "(BELL, MEGAN)(GATES, ANTONY)(GATES, GRACE)(META, ALISSA)(RUDD, ELIZABETH)(RUSSELL, JAMES)(STAN, AMANDY)(STAN, VICTORIA)(STEVE, ANNA)(WAHL, ALEX)(WAHL, ANNA)(WAHL, JACOB)"),
        ("Ann:Russel;John:Gates;Paul:Wahl;Alex:Tolkien;Ann:Bell;Lewis:Kern;Sarah:Rudd;Sydney:Korn;Madison:Meta", 
        "(BELL, ANN)(GATES, JOHN)(KERN, LEWIS)(KORN, SYDNEY)(META, MADISON)(RUDD, SARAH)(RUSSEL, ANN)(TOLKIEN, ALEX)(WAHL, PAUL)"),
        ("Paul:Arno;Matthew:Schwarz;Amandy:Meta;Grace:Meta;Ann:Arno;Alex:Schwarz;Jacob:Rudd;Amber:Cornwell", 
        "(ARNO, ANN)(ARNO, PAUL)(CORNWELL, AMBER)(META, AMANDY)(META, GRACE)(RUDD, JACOB)(SCHWARZ, ALEX)(SCHWARZ, MATTHEW)"),
        ("Abba:Bell;Lewis:Cornwell;Jacob:STAN;Matthew:Schwarz;Ann:STAN;Sophia:Gates;Victoria:Korn;Anna:Bell;Paul:Kern;Alissa:Tolkien", 
        "(BELL, ABBA)(BELL, ANNA)(CORNWELL, LEWIS)(GATES, SOPHIA)(KERN, PAUL)(KORN, VICTORIA)(SCHWARZ, MATTHEW)(STAN, ANN)(STAN, JACOB)(TOLKIEN, ALISSA)"),
        ("Victoria:Thorensen;Ann:Arno;Alexis:Wahl;Emily:Stan;Anna:STAN;Jacob:Korn;Sophia:Gates;Amber:Kern", 
        "(ARNO, ANN)(GATES, SOPHIA)(KERN, AMBER)(KORN, JACOB)(STAN, ANNA)(STAN, EMILY)(THORENSEN, VICTORIA)(WAHL, ALEXIS)"),
        ("Andrew:Arno;Jacob:Russell;Anna:STAN;Antony:Gates;Amber:Korn;Lewis:Dorries;Ann:Burroughs;Alex:Kern;Anna:Arno;Elizabeth:Kern;John:Schwarz;Sarah:STAN", 
        "(ARNO, ANDREW)(ARNO, ANNA)(BURROUGHS, ANN)(DORRIES, LEWIS)(GATES, ANTONY)(KERN, ALEX)(KERN, ELIZABETH)(KORN, AMBER)(RUSSELL, JACOB)(SCHWARZ, JOHN)(STAN, ANNA)(STAN, SARAH)"),
        ("Megan:Wahl;Alexis:Arno;Alex:Wahl;Grace:STAN;Amber:Kern;Amandy:Schwarz;Alissa:Stan;Paul:Kern;Ann:Meta;Lewis:Burroughs;Andrew:Bell", 
        "(ARNO, ALEXIS)(BELL, ANDREW)(BURROUGHS, LEWIS)(KERN, AMBER)(KERN, PAUL)(META, ANN)(SCHWARZ, AMANDY)(STAN, ALISSA)(STAN, GRACE)(WAHL, ALEX)(WAHL, MEGAN)"),
    )
    for key, val in data:
        assert meeting(key) == val


if __name__ == '__main__':
    test()
