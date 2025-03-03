"""
Популярная азартная игра Джокер состоит в вытягивании из барабана 6 шаров,
на которых написаны числа. от 1 до 45. Выигрышный номер джокера формируется
из выпавших чисел так, что в том же порядке, в котором выпадают шары, мы
записываем их последние цифры.

Например, если числа 12, 35, 1, 2, 23 и 39 вытянуты по порядку,
то это джокер №251239.

1[2], 3[5], [1], [2], 2[3], 3[9] --> 251239

Игроки покупают выигрышные билеты и с нетерпением ждут возможности вытянуть и
вычислить число джокера, чтобы рассчитать свой возможный выигрыш. Выигрыш билета
рассчитывается путем сравнения серийного номера, написанного на билете, с
рассчитанным номером джокера таким образом, чтобы подсчитать, сколько последних
цифр этих двух номеров совпадают, как показано в следующей таблице.

Serial No. | Name of prize
-----------+---------------
251239     |   I type
X51239     |   II type
XX1239     |   III type
XXX239     |   IV type
XXXX39     |   V type
XXXXX9     |   Losing card
XXXXXX     |   Losing card

В левом столбце указаны серийные номера билетов, где X обозначает произвольные
цифры. В правом столбце таблицы указаны названия выигрышей для каждой формы
серийного номера. Таким образом, если серийный номер в точности равен номеру
Джокера, то мы получаем выигрыш типа I, если последние 5 цифр равны, мы получаем
выигрыш типа II и так далее, пока не получим выигрыш типа V, который мы получить,
когда последние две цифры равны. Все остальные сериалы не выигрышные.

Напишите программу, которая будет возвращать названия выигрышей для заданного
номера Джокера и заданных билетов. Названия выигрышей необходимо писать точно
так, как указано в таблице выше (количество выигрышей записывается римскими
цифрами с заглавными буквами «I» и «V», после которых следует пробел и строчные
буквы «тип»).
Вход

joker_nums --> массив из 6 чисел, из которого нужно составить выигрышный номер
Джокера

Ticket_serials --> массив из трех серийных номеров билетов.
Выход

Вам необходимо вернуть список с названиями выигрышей по 3-м данным билетам.

joker_card([12, 35, 1, 2, 23, 39], ['151239', '251229', '251339']) --> ["II type", "Losing card", "V type"]

Примечание

    некоторые билеты могут иметь ведущие нули
    некоторые числа-джокеры могут иметь ведущие нули
    ведущие нули по-прежнему учитываются в общей сумме

Задача взята из кантонального конкурса по информатике 2016, Тузла.
"""


def joker_card(num: list[int], ser: list[str]) -> list[str]:
    """
    Расчитывает выйгрышные билеты и тип выиграша.
    """
    x, r = ''.join(str(x)[-1] for x in num)[::-1], {6: 'I type', 5: 'II type', 4: 'III type', 3: 'IV type', 2: 'V type'}
    return [r.get(next((i for i, (a, b) in enumerate(zip(n[::-1], x)) if a != b), 6), 'Losing card') for n in ser]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([12, 35, 1, 2, 23, 39], ['151239', '251229', '251339']), ["II type", "Losing card", "V type"]),
        (([5, 45, 35, 25, 15, 1], ['555551', '235551', '555552']), ["I type", "III type", "Losing card"]),
        (([2, 17, 33, 12, 39, 44], ['000022', '001194', '232294']), ["Losing card", "V type", "IV type"]),
        (([20, 30, 40, 1, 2, 3], ['000123', '000125', '520123']), ["I type", "Losing card", "III type"]),
    )
    for key, val in data:
        assert joker_card(*key) == val


if __name__ == '__main__':
    test()
