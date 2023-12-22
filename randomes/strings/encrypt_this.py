"""
Описание:

Зашифруйте это!

Вы хотите создавать секретные сообщения, которые можно расшифровать с помощью команды
«Расшифруй это!». ката. Вот условия:

    Ваше сообщение представляет собой строку, содержащую слова, разделенные пробелами.
    Вам необходимо зашифровать каждое слово в сообщении, используя следующие правила:
        Первую букву необходимо преобразовать в ее код ASCII.
        Вторую букву необходимо поменять местами с последней буквой.
    Сохраним простоту: во входных данных нет специальных символов.

Примеры:

encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
"""


def encrypt_this(s: str) -> str:
    """
    Шифрование строки по заданному алгоритму.
    """
    return ' '.join([str(ord(w[0:1])) + f'{w[2:-1]}'.join(w[-1:0:2-len(w) or -1]) for w in s.split()])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("", ""),
        ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
        ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
        ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
        ("Why can we not all be like that wise old bird",
         "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
        ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
    )
    for key, val in data:
        assert encrypt_this(key) == val


if __name__ == '__main__':
    test()
