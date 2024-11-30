"""
Дана строка с друзьями для посещения в разных штатах:

ad3="John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Sal Carpenter, 73 6th Street, Boston MA"

мы хотим получить результат, который сортирует имена по штатам и выводит название штата, за которым следуют имена каждого человека, проживающего в этом штате (отсортированные имена людей). Когда результат напечатан, мы получаем:

Massachusetts
.....^John Daggett 341 King Road Plymouth Massachusetts
.....^Sal Carpenter 73 6th Street Boston Massachusetts
^Virginia
.....^Alice Ford 22 East Broadway Richmond Virginia

Пространства не всегда хорошо видны в приведенном выше результате. ^ означает белое пространство.

Результирующая строка (если она не напечатана) будет:

"Massachusetts\n..... John Daggett 341 King Road Plymouth Massachusetts\n..... Sal Carpenter 73 6th Street Boston Massachusetts\n Virginia\n..... Alice Ford 22 East Broadway Richmond Virginia"

или (разделитель \n или \r\n в зависимости от языка)

"Massachusetts\r\n..... John Daggett 341 King Road Plymouth Massachusetts\r\n.....
Sal Carpenter 73 6th Street Boston Massachusetts\r\n Virginia\r\n..... Alice Ford 22
East Broadway Richmond Virginia"

Примечания

    В данной строке адресов может быть пустая последняя строка.
    Тесты содержат только CA, MA, OK, PA, VA, AZ, ID, IN для состояний.
    Другой пример вы можете увидеть в разделе «Примеры тестов».

Штаты

Для ленивых:

'AZ': 'Arizona',
'CA': 'California',
'ID': 'Idaho',
'IN': 'Indiana',
'MA': 'Massachusetts',
'OK': 'Oklahoma',
'PA': 'Pennsylvania',
'VA': 'Virginia'
"""

x = {
    'AZ': 'Arizona',
    'CA': 'California',
    'ID': 'Idaho',
    'IN': 'Indiana',
    'MA': 'Massachusetts',
    'OK': 'Oklahoma',
    'PA': 'Pennsylvania',
    'VA': 'Virginia',
}


def by_state(s: str) -> str:
    """
    Разбиение и сортировка адресной книги на штатам по алфавиту.
    """
    res = {}
    for line in s.split('\n'):
        res[w] = res.get(w := x.get(line[-2:], line[-2:]), []) + [f"..... {line.replace(',', '').strip()[:-2]}{w}"]
    return '\r\n '.join([f'{a}\r\n' + "\r\n".join(sorted(b)) for a, b in sorted(res.items())]).strip('. \r\n')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("""John Daggett, 341 King Road, Plymouth MA
        Alice Ford, 22 East Broadway, Richmond VA
        Orville Thomas, 11345 Oak Bridge Road, Tulsa OK
        Terry Kalkas, 402 Lans Road, Beaver Falls PA
        Eric Adams, 20 Post Road, Sudbury MA
        Hubert Sims, 328A Brook Road, Roanoke MA
        Amy Wilde, 334 Bayshore Pkwy, Mountain View CA
        Sal Carpenter, 73 6th Street, Boston MA""",

        "California\r\n..... Amy Wilde 334 Bayshore Pkwy Mountain View California\r\n " +
        "Massachusetts\r\n..... Eric Adams 20 Post Road Sudbury Massachusetts\r\n..... " +
        "Hubert Sims 328A Brook Road Roanoke Massachusetts\r\n..... John Daggett 341 King " +
        "Road Plymouth Massachusetts\r\n..... Sal Carpenter 73 6th Street Boston " +
        "Massachusetts\r\n Oklahoma\r\n..... Orville Thomas 11345 Oak Bridge Road Tulsa " +
        "Oklahoma\r\n Pennsylvania\r\n..... Terry Kalkas 402 Lans Road Beaver Falls " +
        "Pennsylvania\r\n Virginia\r\n..... Alice Ford 22 East Broadway Richmond Virginia"),
    )
    for key, val in data:
        assert by_state(key) == val


if __name__ == '__main__':
    test()
