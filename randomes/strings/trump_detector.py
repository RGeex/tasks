"""
Мы все любим будущего президента (или фюрера, или дуче, или сото, как он мог
бы найти их более подходящими) Дональда Трампа, но мы можем опасаться, что
некоторые из его многочисленных поклонников, таких как Джон Миллер или Джон
Бэррон, не воздают ему должного, что звучит слишком похоже на своего
(и нашего, конечно же!) героя и тем самым рискуя его скомпрометировать.

По этой причине нам нужно создать функцию для определения оригинального и
уникального ритма нашего любимого лидера, обычно имеющего много дополнительных
гласных, готовых бороться с истеблишментом.

Индекс рассчитывается на основе того, сколько гласных повторяется более одного
раза подряд, и деления их на общее количество гласных, которые употребил бы
мелкий враг Америки.

Например:

trump_detector("I will build a huge wall")==0 #definitely not our trump: 0 on
the trump score
trump_detector("HUUUUUGEEEE WAAAAAALL")==4 #4 extra "U", 3 extra "E" and 5
extra "A" on 3 different vowel groups: 12/3 make for a trumpy trumping score
of 4: not bad at all!
trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT")==1.56 #14
extra vowels on 9 base ones

Примечания: гласные — это только те, что входят в патриотическую группу
«aeiou»: «y» должна вернуться в Грецию, если она думает, что может иметь
те же права, что и настоящие американские гласные; всегда будет хотя бы гласная,
поскольку молчание — это выбор трусливых кенийских/террористических президентов
и их друзей.

Округлите каждый результат на две десятичные цифры: в Америке Трампа нет места
мелкой сошке.
"""


from itertools import groupby as gb


def trump_detector(s: str) -> float:
    """
    Подсчитывает в строке округленное до 2-х знаков кол-во повторяющихся гласных
    деленное на кол-во групп гласных.
    """
    return round(sum(x := [len(list(b)) - 1 for a, b in gb(s.lower()) if a in 'aeiou']) / (len(x) or 1), 2)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("I will build a huge wall", 0),
        ("HUUUUUGEEEE WAAAAAALL", 4),
        ("MEXICAAAAAAAANS GOOOO HOOOMEEEE", 2.5),
        ("America NUUUUUKEEEE Oooobaaaamaaaaa", 1.89),
        ("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT", 1.56),
    )
    for key, val in data:
        assert trump_detector(key) == val


if __name__ == '__main__':
    test()
