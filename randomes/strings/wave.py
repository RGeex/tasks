"""
Волна (известная как мексиканская волна в англоязычном мире за пределами Северной Америки)
является примером метахронного ритма, достигаемого на переполненном стадионе,
когда последовательные группы зрителей ненадолго встают, кричат ​​и поднимают руки.
Сразу после вытягивания в полный рост зритель возвращается в обычное сидячее положение.

  В результате возникает волна стоящих зрителей, которая проходит сквозь толпу, хотя отдельные
  зрители никогда не отходят от своих мест.   На многих крупных аренах толпа сидит по непрерывному
  кругу по всему спортивному полю, и поэтому волна может непрерывно перемещаться по арене;
  при несмежном расположении сидений волна может вместо этого отражаться взад и вперед через толпу.
  Когда щель в сидении узкая, волна иногда может пройти через нее.   Обычно в любой момент времени
  на арене присутствует только один гребень волны, хотя одновременно возникают волны, вращающиеся в
  противоположных направлениях.   (Источник  Википедия )
 

Задача

В этом простом ката ваша задача — создать функцию, которая превращает строку в мексиканскую волну.
Вам будет передана строка, и вы должны вернуть эту строку в массиве, где заглавная буква — это
стоящий человек.
 

Правила

1. Входная строка всегда будет в нижнем регистре, но может быть пустой.

 2. Если символ в строке является пробелом, пропустите его, как если бы это было пустое место.
 

Пример

wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
"""


def wave(s: str) -> list[str]:
    """
    Создает из строки список - "Мексиканскую волну".
    """
    return [s[:i] + s[i:].capitalize() for i in range(len(list(s))) if s[i] != ' ']


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("", []),
        ("hello", ["Hello", "hEllo", "heLlo", "helLo", "hellO"]),
        ("codewars", ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]),
        ("two words", ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]),
    )
    for key, val in data:
        assert wave(key) == val


if __name__ == '__main__':
    test()
