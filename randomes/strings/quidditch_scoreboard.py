"""
Ваш двоюродный брат-волшебник работает на стадионе для квиддича и хочет,
чтобы вы написали функцию, которая подсчитывает очки для табло квиддича!
История

Квиддич – это вид спорта, в котором участвуют две команды. Команды забивают
голы, бросая квоффл через кольцо, каждый гол приносит 10 очков .

Судья также вычитает 30 очков ( -30 очков ) из команды, виновной в совершении
любого из следующих нарушений: Блаттинг, Блёртинг, Шлепанье, Хейверстэкинг,
Квафл-тыканье, Шутирование.

Матч завершается, когда снитч пойман, и его поимка приносит 150 очков.
Допустим, квоффл проходит через кольцо через несколько секунд после того,
как пойман снитч, в этом случае очки за этот гол не должны попасть на табло,
поскольку матч уже завершен.

Вам не нужны какие-либо предварительные знания о том, как работает квиддич,
чтобы выполнить это ката, но если вы хотите узнать, что это такое, вот ссылка:
https://en.wikipedia.org/wiki/Quidditch
Задача

Вам будет предоставлена ​​строка с двумя аргументами: первый аргумент сообщит
вам, какие команды играют, а второй аргумент расскажет вам, что произошло в
матче. Подсчитайте очки и верните строку, содержащую итоговые результаты команд,
причем названия команд отсортированы в том же порядке, что и в первом аргументе.
Примеры:
Учитывая ввод:

quidditchScoreboard("Ilkley vs Yorkshire", "Ilkley: Quaffle goal, Yorkshire: Haverstacking foul, Yorkshire: Caught Snitch")

Ожидаемый результат будет:

"Ilkley: 10, Yorkshire: 120"

Отделите названия команд от соответствующих им очков двоеточием и разделите две команды запятой.

Удачи!
"""


def quidditch_scoreboard(teams: str, actions: str) -> str:
    """
    Подсчитывает результаты матча.
    """
    x = 'Blatching Blurting Bumphing Haverstacking Quaffle-pocking Stooging'.split()
    s, r = 0, dict(zip(teams.split(' vs '), (0, 0)))
    for line in actions.split(', '):
        if s:
            break
        a, b = line.split(':')
        for w in b.split():
            r[a] += [[[0, 150][w == 'Snitch'], 10][w == 'goal'], -30][w in x]
            if w == 'Snitch':
                s = 1
                break
    return str(r)[1:-1].replace('\'', '')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("Appleby Arrows vs Montrose Magpies",
        "Montrose Magpies: Quaffle goal, Montrose Magpies: Quaffle goal, Appleby Arrows: Quaffle goal, Appleby Arrows: Quaffle goal, Montrose Magpies: Haverstacking foul, Appleby Arrows: Quaffle goal, Appleby Arrows: Quaffle goal, Appleby Arrows: Quaffle goal, Appleby Arrows: Quaffle goal, Montrose Magpies: Caught Snitch"),
        "Appleby Arrows: 60, Montrose Magpies: 140"),
        (("Kenmare Kestrels vs Barnton",
        "Barnton: Quaffle goal, Kenmare Kestrels: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Kenmare Kestrels: Blurting foul, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Kenmare Kestrels: Caught Snitch"),
        "Kenmare Kestrels: 130, Barnton: 100"),
    )
    for key, val in data:
        assert quidditch_scoreboard(*key) == val


if __name__ == '__main__':
    test()
