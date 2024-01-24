"""
Как отличить экстраверта от интроверта в АНБ?
Ва, что ryringbef, что rkgebireg ybbxf ng, что BGURE thl'f ​​fubrf.

Я нашел эту шутку в USENET, но ее суть зашифрована. Может быть, вы сможете его расшифровать?
Согласно Википедии, ROT13 часто используется для запутывания шуток в USENET.

Для этой задачи вам нужно только заменить символы. Не пробелы, знаки препинания, цифры и т. д.

Примеры испытаний:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"


"""


def rot13(message: str) -> str:
    """
    Шифр строки ROT13.
    """
    data = [dict(zip(*[[chr((x + n) % 26 + i) for x in range(26)] for n in (0, 13)]))
            for i in (65, 97)]
    return ''.join(next((x.get(w) for x in data if x.get(w)), w) for w in message)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("EBG13 rknzcyr.", "ROT13 example."),
        ("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.",
         "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes."),
        ("123", "123"),
        ("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)",
         "This is actually the first kata I ever made. Thanks for finishing it! :)"),
        ("@[`{", "@[`{"),
    )
    for key, val in data:
        assert rot13(key) == val


if __name__ == '__main__':
    test()
