"""
Книготорговец имеет множество книг, отнесенных к 26 категориям с обозначениями
A, B, ... Z. У каждой книги есть код cиз 3, 4, 5 и более символов. Первый .
символ кода — заглавная буква, определяющая категорию книги

В списке книготорговца каждый код cза которым следует пробел и целое
положительное число n (int n >= 0) что указывает на количество книг
данного кода на складе.

Например, выдержка из номенклатуры может быть такой:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or
L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....

Вам будет предоставлен список товаров (например: L) и список категорий,
написанный заглавными буквами. например:

M = {"A", "B", "C", "W"} 
or
M = ["A", "B", "C", "W"] or ...

и ваша задача найти все книги Л с кодами принадлежащие каждой категории М, и
просуммировать их количество по каждой категории.

Для списков L и M примера вам нужно вернуть строку
(в Haskell/Clojure/Racket/Prolog список пар):

(A : 20) - (B : 114) - (C : 50) - (W : 0)

где A, B, C, W — категории, 20 — сумма единственной книги категории A, 114 —
сумма, соответствующая для «BKWRK» и «BTSQZ», 50 соответствует «CDXEF» и 0 —
категории «W», поскольку коды, начинающиеся с W, отсутствуют.

Если L или M пусты, возвращаемая строка равна
""(Вместо этого Clojure/Racket/Prolog должен возвращать пустой массив/список).
Примечания:

    В результирующих кодах и их значениях тот же порядок, что и в М.
    См. «Образцы тестов» для получения информации о возврате.
"""


def stock_list(list_of_art: list, list_of_cat: list) -> str:
    """
    Поиск кол-ва книз по искомым артикулам.
    """
    tmp = {x: [] for x in list_of_cat}
    for art in list_of_art:
        tmp.get(art[0], []).append(int(art.split()[1]))
    return ' - '.join([f'({k} : {sum(v)})' for k, v in tmp.items()]) if any(map(sum, tmp.values())) else ''


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B", "C", "D"]), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"),
        ((["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"]), "(A : 200) - (B : 1140)"),
    )
    for key, val in data:
        assert stock_list(*key) == val


if __name__ == '__main__':
    test()
