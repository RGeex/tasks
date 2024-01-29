"""
Упорядоченный след муравьев марширует по площадке для пикника в парке.

Это выглядит примерно так:

..ant..ant.ant...ant.ant..ant.ant....ant..ant.ant.ant...ant..
 

Но вдруг ходит слух, что впереди на земле заметили упавший сэндвич с курицей. Муравьи рвутся вперед! О нет, это муравьиная давка!!

Некоторые из более медленных муравьев растаптываются, а их бедные маленькие муравьиные тела разбиваются на разбросанные кусочки.

В результате кровавая бойня выглядит следующим образом:

...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t

Сможете ли вы узнать, сколько муравьев умерло?
Примечания

    Если у вас есть сомнения, предположите, что разбросанные кусочки принадлежат одному и тому же муравью.
    например 2 головы и 1 тело = 2 мертвых муравья, а не 3


"""


def dead_ant_count(ants: str) -> int:
    """
    Поиск кол-ва погибших муравьев.
    """
    return int(bool(ants) and max(map(lambda n: n in 'ant' and x.count(n), set(x := ants.replace('ant', '')))))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("ant ant ant ant", 0),
        ("", 0),
        (" ", 0),
        ("ant anantt aantnt", 2),
        ("ant ant .... a nt", 1),
        ("ant ant ant ant", 0),
        ("", 0),
        (" ", 0),
        ("ant anantt aantnt", 2),
        ("ant ant .... a nt", 1),
        ("antatn ant ant", 1),
        ("ant a ant anatttt", 4),
        ("antantantan", 1),
        ("aaaaannnntttt", 5),
        ("aaaannnnntttt", 5),
        ("aaaannnnttttt", 5),
        ("a n t", 1),
        ("... .. ...", 0),
        ("$$$ant..a", 1),
        (".n..tt.n.nt..t.ntant..aaaaa..tn.na.aaat..n..tn.ntan.t", 10),
        ("ant ant .... a nt", 1),
    )
    for key, val in data:
        assert dead_ant_count(key) == val


if __name__ == '__main__':
    test()
