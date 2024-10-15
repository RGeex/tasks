"""
Вашего очень пассивно-агрессивного коллегу только что уволили. Пока он собирал
свои вещи, он быстро вставил в вашу систему ошибку, которая переименовывала все,
что выглядело как бред. Он оставил на своем столе две записки: одна гласит:
«ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz», а другая гласит:
«Uif usjdl up uijt lbub jt tjnqmf kvtu sfqmbdf fwfsz mfuufs xjui uif mfuufs uibu dpnft cfgpsf ju».

Вместо того, чтобы тратить часы на поиск самой ошибки, вы решаете попытаться
расшифровать ее.

Если ввод не является строкой, ваша функция должна вернуть «Ввод не является
строкой». Ваша функция должна иметь возможность обрабатывать заглавные и строчные
буквы. Вам не придется беспокоиться о пунктуации.
"""


def one_down(txt: str) -> str:
    """
    Заменяет каждую букву на предыдущую.
    """
    return ''.join(chr((ord(x) - [98, 66][x.isupper()]) % 26 + [97, 65][x.isupper()]) if x.isalpha() else x for x in txt) if isinstance(txt, str) else "Input is not a string"


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("Ifmmp", "Hello"),
        ("Uif usjdl up uijt lbub jt tjnqmf", "The trick to this kata is simple"),
        (45, "Input is not a string"),
        ("XiBu BcPvU dSbAz UfYu", "WhAt AbOuT cRaZy TeXt"),
        (["Hello there", "World"], "Input is not a string"),
        ("BMM DBQT NBZCF", "ALL CAPS MAYBE"),
        ("qVAamFt BsF gVo", "pUZzlEs ArE fUn"),
        ("CodeWars RockZ", "BncdVzqr QnbjY"),
        ("", ""),
        ("J ipqf zpv bsf ibwjoh b ojdf ebz", "I hope you are having a nice day"),
    )
    for key, val in data:
        assert one_down(key) == val


if __name__ == '__main__':
    test()
