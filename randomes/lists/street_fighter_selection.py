"""
Короткое вступление

Некоторые из вас, возможно, помнят, как проводили дни, играя в Street Fighter 2 в какой-нибудь аркаде еще в 90-х, или эмулировали ее сегодня с помощью многочисленных эмуляторов для ретро-консолей.

Сможете ли вы решить это ката? Суууре-ты-можешь!

доступна новая, более сложная версия ката ОБНОВЛЕНИЕ: здесь .

Слово

Вам придется смоделировать поведение экрана выбора персонажа в видеоигре, точнее, сетку выбора. Такой экран выглядит следующим образом:

Экран:

экран

Макет сетки выделения в тексте:

| Ryu  | E.Honda | Blanka  | Guile   | Balrog | Vega    |
| Ken  | Chun Li | Zangief | Dhalsim | Sagat  | M.Bison |

Вход

    список игровых персонажей в сетке 2х6;
    исходное положение курсора выбора (вверху слева (0,0));
    список перемещений курсора выбора (которые up, down, left, right);

Выход

    список персонажей, на которых наведен курсор выбора после всех ходов (по порядку и с повторением, все после хода, успешные или нет, см. тесты);

Правила

Курсор выбора имеет круглую форму по горизонтали , но не по вертикали !

Как вы, наверное, помните из игры, курсор выбора вращается горизонтально, а не вертикально; это означает, что если я нахожусь крайним слева и попытаюсь снова пойти налево, я попаду в крайний правый угол (примеры: от Рю до Веги, от Кена до М.Бисона) и наоборот от крайнего правого до крайнего левого.

Вместо этого, если я попытаюсь подняться дальше от самого верхнего или ниже от самого нижнего, я просто останусь там, где нахожусь (примеры: вы не можете опуститься ниже самого нижнего ряда: Кен, Чун Ли, Зангиев, Дхалсим, Сагат и М.Бисон на изображении выше; вы не можете подняться выше верхнего ряда: Рю, Э.Хонда, Бланка, Гайл, Балрог и Вега на изображении выше).

Тест

В этой простой версии расположение сетки бойцов и исходное положение всегда
будут одинаковыми во всех тестах, меняется только список приемов.

Примечание : изменение некоторых входных данных может вам не помочь.

Примеры

    fighters = [
      ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
      ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]
    initial_position = (0,0)
    moves = ['up', 'left', 'right', 'left', 'left']

    тогда я должен получить:

    ['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog']

    как персонажи, на которых я наводил курсор выбора во время своих ходов.
    Примечание: Рю первый только потому, что он «проваливает» первый. up
    Дополнительные примеры см. в тестовых примерах.

    fighters = [
      ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
      ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]
    initial_position = (0,0)
    moves = ['right', 'down', 'left', 'left', 'left', 'left', 'right']

    Результат:

    ['E.Honda', 'Chun Li', 'Ken', 'M.Bison', 'Sagat', 'Dhalsim', 'Sagat']
"""


from itertools import permutations as pm


def street_fighter_selection(fighters: list[list[str]], cur: tuple[int], moves: list[str]) -> list[str]:
    """
    Навигация по игровому меню, перемещение вверх и вниз ограничены размером списка,
    влево и вправо переходят за границы в противоположный конец списка, учитывая возможную
    разницу длин вложенных списков.
    """
    res, cur, mov = [], list(cur), dict(zip('up left right down'.split(), filter(sum, pm(range(-1, 2), 2))))
    for m in moves:
        for i, p in enumerate(zip(cur, mov[m])):
            if m in list(mov)[::len(mov) - 1]:
                cur[i] = min(max(sum(p), 0), len([fighters, fighters[cur[0]]][i]) - 1)
            else:
                cur[i] = [sum(p), len(fighters[cur[0]]) - 1][sum(p) < 0] % len(fighters[cur[0]])
        res.append(fighters[cur[0]][cur[1]])
    return res


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    fighters = [
        ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
        ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]

    data = (
        ((fighters, (0, 0), []), []),
        ((fighters, (0, 0), ["up"]*4), ['Ryu', 'Ryu', 'Ryu', 'Ryu']),
        ((fighters, (0, 0), ["down"]*4), ['Ken', 'Ken', 'Ken', 'Ken']),
        ((fighters, (0, 0), ["left"]*8), ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']),
        ((fighters, (0, 0), ["right"]*8), ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']),
        ((fighters, (0, 0), ["up","left","down","right"]*2), ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']),
        ((fighters, (0, 0), ["down","right","up","left"]*2), ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']),
    )
    for key, val in data:
        assert street_fighter_selection(*key) == val


if __name__ == '__main__':
    test()
