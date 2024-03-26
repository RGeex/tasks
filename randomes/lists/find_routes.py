"""
Мы усердно преследуем нашего неуловимого оперативника Мэтью Найта , который также известен под псевдонимом Рой Миллер .
Чтобы избежать обнаружения, он ведет кочевой образ жизни, постоянно перемещаясь из одного места в другое, причем каждое
из его путешествий следует запутанной и нестандартной последовательности маршрутов . Наша задача — расшифровать маршруты,
которые он будет проходить во время каждого своего путешествия.
Задача

Вам предоставлен массив маршрутов routes, расшифровать точные пункты назначения, которые он посетит в правильной
последовательности, согласно его тщательно спланированным маршрутам.
Пример

По предоставленным маршрутам:

[ [USA, BRA], [JPN, PHL], [BRA, UAE], [UAE, JPN] ]

Правильная последовательность пунктов назначения:

"USA, BRA, UAE, JPN, PHL"

Примечание:

    Вы можете с уверенностью предположить, что не будет повторяющихся местоположений с разными routes.
    Все routesпредоставленные маршруты будут иметь непустые маршруты .
    Всегда будет хотя бы один (1) маршрут, соединяющий одну промежуточную точку с другой.
"""


def find_routes(arr: list[list[str]]) -> str:
    """
    Поиск марсшрута через заданные поинты.
    """
    r = [next(x for x in list(dict(arr)) if not dict(x[::-1] for x in arr).get(x))]
    while x := dict(arr).get(r[-1]):
        r.append(x)
    return ', '.join(r)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([('one','two')], 'one, two'),
        ([('one','two'), ('two','three')], 'one, two, three'),
        ([('two','three'), ('one','two')], 'one, two, three'),
        ([('MNL','TAG'), ('CEB','TAC'), ('TAG','CEB'), ('TAC','BOR')], 'MNL, TAG, CEB, TAC, BOR'),
        ([('ITA','GER'), ('GER','BEL'), ('BEL','CAN')], 'ITA, GER, BEL, CAN'),
        ([('Chicago','Winnipeg'), ('Halifax','Montreal'), ('Montreal','Toronto'), ('Toronto','Chicago'), ('Winnipeg','Seattle')], 'Halifax, Montreal, Toronto, Chicago, Winnipeg, Seattle'),
        ([('Calgary','Fargo'), ('Spokane','Toronto'), ('Winnipeg','Montreal'), ('Toronto','Calgary'), ('Fargo','Winnipeg')], 'Spokane, Toronto, Calgary, Fargo, Winnipeg, Montreal'),
        ([('BRA','KSA'), ('USA','BRA'), ('JPN','PHL'), ('KSA','UAE'), ('UAE','JPN')], 'USA, BRA, KSA, UAE, JPN, PHL'),
    )
    for key, val in data:
        assert find_routes(key) == val


if __name__ == '__main__':
    test()