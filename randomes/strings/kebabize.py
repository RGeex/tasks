"""
Измените kebabizeфункция, которая преобразует строку регистра верблюда в регистр кебаба.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"

Примечания:

    возвращаемая строка должна содержать только строчные буквы

"""


def kebabize(st: str) -> str:
    """
    конвертирует CamelCase кебаб, исключая все, кроме букв.
    """
    st = ''.join([x for x in st if x.isalpha()])
    x = [None] + [i for i, x in enumerate(st) if i and x.isupper()]
    return '-'.join([st[a:b].lower() for a, b in zip(x, x[1:] + [None])])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('42', ''),
        ('SOS', 's-o-s'),
        ('CodeWars', 'code-wars'),
        ('myCamelHas3Humps', 'my-camel-has-humps'),
        ('myCamelCasedString', 'my-camel-cased-string'),
    )
    for key, val in data:
        assert kebabize(key) == val


if __name__ == '__main__':
    test()
