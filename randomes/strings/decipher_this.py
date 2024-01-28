"""
Вам дано секретное сообщение, которое нужно расшифровать. Вот что вам нужно знать, чтобы расшифровать его:

Для каждого слова:

    вторая и последняя буквы меняются местами (например Helloстановится Holle)
    первая буква заменяется ее кодом символа (например, Hстановится 72)

    специальные символы не используются, только буквы и пробелы
    слова разделяются одним пробелом
    нет ведущих или конечных пробелов

Примеры

'72olle 103doo 100ya' --> 'Hello good day'
'82yade 115te 103o'   --> 'Ready set go'


"""


def decipher_this(s: str) -> str:
    """
    Расшифровывает сообщение.
    """
    r = []
    for w in s.split():
        i = next((i for i, x in enumerate(w) if x.isalpha()), len(w))
        r.append(chr(int(w[:i])) + f'{w[i+1:-1]}'.join(w[-1:-len(w[i:]) - 1:-len(w[i:]) + 1 or 1] or w[i:]))
    return ' '.join(r)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("65 119esi 111dl 111lw 108dvei 105n 97n 111ka", "A wise old owl lived in an oak"),
        ("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp", "The more he saw the less he spoke"),
        ("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare", "The less he spoke the more he heard"),
        ("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri",
        "Why can we not all be like that wise old bird"),
        ("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple", "Thank you Piotr for all your help"),
    )
    for key, val in data:
        assert decipher_this(key) == val


if __name__ == '__main__':
    test()
