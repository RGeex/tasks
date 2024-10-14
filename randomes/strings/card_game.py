"""
Давайте создадим функцию для игры в карты. Вы получаете 3 аргумента: card1 и
card2 являются картами из одной колоды; trump – это основная масть, которая
превосходит все остальные.

У вас есть предустановленный deck (если вам это нужно):

deck = ["joker","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣",
                "2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦",
                "2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♥",
                "2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠"]

Правила игры

    Если обе карты имеют одну и ту же масть, выигрывает более старшая из них.
    Если обе карты козырные, выигрывает более старшая карта.
    Если карты разной масти и ни у кого нет козыря, верните "Let us play again."
    Если у одной карты есть козырь, а у другой нет, то выигрывает тот, у кого есть козырь.
    Если есть победитель, верните "The first/second card won."
    Если две карты одинаковы, верните "Someone cheats."
    Джокер всегда побеждает

Примеры

"3♣", "Q♣", "♦"  -->  "The second card won."
"5♥", "A♣", "♦"  -->  "Let us play again."
"8♠", "8♠", "♣"  -->  "Someone cheats."
"2♦", "A♠", "♦"  -->  "The first card won."
"joker", "joker", "♦"  -->  "Someone cheats."
"""


def card_game(card_1: str, card_2: str, trump: str) -> str:
    """
    Определяет победителя среди 2-х карт по старшинству.
    """
    c1, c2 = [[x.translate(str.maketrans({b:str(a) for a, b in enumerate('JQKA', 11)})), f'15{trump}'][x == 'joker'] for x in (card_1, card_2)]
    r = ["Someone cheats.", f"The {['second', 'first'][max(c1, c2, key=lambda x: (x[-1] == trump, int(x[:-1]))) == c1]} card won.", "Let us play again."]
    return r[0 if c1 == c2 else 1 if trump in c1 + c2 or c1[-1] == c2[-1] else 2]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("Q♣", "3♣", "♦"), "The first card won."),
        (("3♣", "Q♣", "♦"), "The second card won."),
        (("5♥", "A♣", "♦"), "Let us play again."),
        (("8♠", "8♠", "♣"), "Someone cheats."),
        (("2♦", "A♠", "♦"), "The first card won."),
        (("A♠", "2♦", "♦"), "The second card won."),
        (("joker", "joker", "♦"), "Someone cheats."),
        (("joker", "10♣", "♠"), "The first card won."),
        (("10♣", "joker", "♠"), "The second card won."),
    )
    for key, val in data:
        assert card_game(*key) == val


if __name__ == '__main__':
    test()
