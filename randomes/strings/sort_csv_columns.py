"""
Вы получаете строку с содержимым csv-файла. Столбцы разделяются точкой с запятой.
Первая строка содержит названия столбцов.
Напишите метод, который сортирует столбцы по именам столбцов в алфавитном порядке с учетом регистра.

Пример:

Before sorting:
As table (only visualization):
|myjinxin2015|raulbc777|smile67|Dentzil|SteffenVogel_79|
|17945       |10091    |10088  |3907   |10132          |
|2           |12       |13     |48     |11             |

The csv-file:
myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n
17945;10091;10088;3907;10132\n
2;12;13;48;11

----------------------------------

After sorting:
As table (only visualization):
|Dentzil|myjinxin2015|raulbc777|smile67|SteffenVogel_79|
|3907   |17945       |10091    |10088  |10132          |
|48     |2           |12       |13     |11             |

The csv-file:
Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n
3907;17945;10091;10088;10132\n
48;2;12;13;11

Нет необходимости в предварительной проверке. Вы всегда получите правильную строку, содержащую
более 1 строки и более 1 строки. Все столбцы будут иметь разные имена.
"""


def sort_csv_columns(csv_file_content: str) -> str:
    res = []
    for i, w in enumerate(csv_file_content.split('\n')):
        csv_file_content = w.split(';')
        if not i:
            c = [n for n, _ in sorted(enumerate(csv_file_content), key=lambda x: x[1].lower())]
        res.append(';'.join(k for _, k in sorted(
            enumerate(csv_file_content), key=lambda x: c.index(x[0]))))
    return '\n'.join(res)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((
            "myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n"
            "17945;10091;10088;3907;10132\n"
            "2;12;13;48;11"
        ),
            (
            "Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n"
            "3907;17945;10091;10088;10132\n"
            "48;2;12;13;11"
        )),
        ((
            "Captain America;Hulk;IronMan;Thor\n"
            "honorably;angry;arrogant;divine\n"
            "shield;greenhorn;armor;hammer\n"
            "Steven;Bruce;Tony;Thor"
        ),
            (
            "Captain America;Hulk;IronMan;Thor\n"
            "honorably;angry;arrogant;divine\n"
            "shield;greenhorn;armor;hammer\n"
            "Steven;Bruce;Tony;Thor"
        )),
    )
    for key, val in data:
        assert sort_csv_columns(key) == val


if __name__ == '__main__':
    test()
