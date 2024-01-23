"""
Вам предоставляется небольшой отрывок из каталога:

s = "<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>

<prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>

<prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>

<prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>

<prod><name>saw</name><prx>9</prx><qty>10</qty></prod>

...

( prxозначает price, qtyдля quantity) и артикль т.е. "видел".

The function catalog(s, "saw")возвращает строку(и), соответствующую статье с $до цен:

"table saw > prx: $1099.99 qty: 5\nsaw > prx: $9 qty: 10\n..."

Если товара нет в каталоге, верните «Ничего».
Примечания

    Между двумя строками каталога находится пустая строка.

    Одна и та же статья может появляться более одного раза. Если это произойдет,
    верните все строки, о которых идет речь в статье (в том же порядке, что и в каталоге;
    однако см. ниже примечание для языка Пролог).

    Разделитель строк результатов может зависеть от языка. \n или \r\n.

    в Perl перед ценами используйте «£» вместо «$».

    Посмотреть примеры можно в разделе «Примеры тестов».

Примечание для языка Пролог

    Если товара нет в каталоге, то R равно "".

    Подстроки R (разделенные символом «\n») должны быть в алфавитном порядке.

"""


import re


def catalog(s: str, article: str) -> str:
    """
    Поиск данных о товаре из каталога.
    """
    res = []
    for line in s.split('\n'):
        if article in line:
            name, prx, qty = [re.findall(rf'<{tag}>(.*)</{tag}>', line)[0]
                              for tag in 'name prx qty'.split()]
            res.append(f'{name} > prx: ${prx} qty: {qty}')

    return '\r\n'.join(res) or 'Nothing'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    s = """<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>
    <prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>
    <prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>
    <prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>
    <prod><name>saw</name><prx>9</prx><qty>10</qty></prod>
    <prod><name>chair</name><prx>100</prx><qty>20</qty></prod>
    <prod><name>fan</name><prx>50</prx><qty>8</qty></prod>
    <prod><name>wire</name><prx>10.8</prx><qty>15</qty></prod>
    <prod><name>battery</name><prx>150</prx><qty>12</qty></prod>
    <prod><name>pallet</name><prx>10</prx><qty>50</qty></prod>
    <prod><name>wheel</name><prx>8.80</prx><qty>32</qty></prod>
    <prod><name>extractor</name><prx>105</prx><qty>17</qty></prod>
    <prod><name>bumper</name><prx>150</prx><qty>3</qty></prod>
    <prod><name>ladder</name><prx>112</prx><qty>12</qty></prod>
    <prod><name>hoist</name><prx>13.80</prx><qty>32</qty></prod>
    <prod><name>platform</name><prx>65</prx><qty>21</qty></prod>
    <prod><name>car wheel</name><prx>505</prx><qty>7</qty></prod>
    <prod><name>bicycle wheel</name><prx>150</prx><qty>11</qty></prod>
    <prod><name>big hammer</name><prx>18</prx><qty>12</qty></prod>
    <prod><name>saw for metal</name><prx>13.80</prx><qty>32</qty></prod>
    <prod><name>wood pallet</name><prx>65</prx><qty>21</qty></prod>
    <prod><name>circular fan</name><prx>80</prx><qty>8</qty></prod>
    <prod><name>exhaust fan</name><prx>62</prx><qty>8</qty></prod>
    <prod><name>window fan</name><prx>62</prx><qty>8</qty></prod>"""

    data = (
        ((s, 'ladder'), 'ladder > prx: $112 qty: 12'),
        ((s, 'saw'), 'table saw > prx: $1099.99 qty: 5\r\nsaw > prx: $9 qty: 10\r\nsaw for metal > prx: $13.80 qty: 32'),
        ((s, 'wood pallet'), 'wood pallet > prx: $65 qty: 21'),
        ((s, 'extractor'), 'extractor > prx: $105 qty: 17'),
        ((s, 'nails'), 'Nothing'),
        ((s, 'battery'), 'battery > prx: $150 qty: 12'),
        ((s, 'wheel'), 'wheel > prx: $8.80 qty: 32\r\ncar wheel > prx: $505 qty: 7\r\nbicycle wheel > prx: $150 qty: 11'),
        ((s, 'table saw'), 'table saw > prx: $1099.99 qty: 5'),
        ((s, 'exhaust fan'), 'exhaust fan > prx: $62 qty: 8'),
        ((s, 'platform'), 'platform > prx: $65 qty: 21'),
        ((s, 'fan'), 'fan > prx: $50 qty: 8\r\ncircular fan > prx: $80 qty: 8\r\nexhaust fan > prx: $62 qty: 8\r\nwindow fan > prx: $62 qty: 8'),
        ((s, 'hoist'), 'hoist > prx: $13.80 qty: 32'),
        ((s, 'big hammer'), 'big hammer > prx: $18 qty: 12'),
        ((s, 'window fan'), 'window fan > prx: $62 qty: 8'),
        ((s, 'screwdriver'), 'screwdriver > prx: $5 qty: 51'),
        ((s, 'hammer'), 'hammer > prx: $10 qty: 50\r\nbig hammer > prx: $18 qty: 12'),
        ((s, 'scissors'), 'Nothing'),
        ((s, 'bicycle wheel'), 'bicycle wheel > prx: $150 qty: 11'),
    )
    for key, val in data:
        assert catalog(*key) == val


if __name__ == '__main__':
    test()
