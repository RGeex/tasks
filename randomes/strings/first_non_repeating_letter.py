"""
Напишите функцию с именем first_non_repeating_letter† который принимает
строковый ввод и возвращает первый символ, который не повторяется нигде в
строке.

Например, если ввести входные данные 'stress', функция должна вернуть 't',
поскольку буква t встречается в строке только один раз и встречается в
строке первой.

В качестве дополнительной проблемы прописные и строчные буквы считаются одним
и тем же символом , но функция должна возвращать правильный регистр для
начальной буквы. Например, ввод 'sTreSS'должен вернуться 'T'.

Если строка содержит все повторяющиеся символы , она должна возвращать пустую
строку ( "");

† Примечание: функция называется firstNonRepeatingLetterпо историческим
причинам, но ваша функция должна обрабатывать любой символ Юникода.
"""


def first_non_repeating_letter(s:str) -> str:
    """
    Поиск первого в строке не дублирующегося символа без учета регистра.
    """
    return next((s[i] for i, w in enumerate(s.lower()) if s.lower().count(w) == 1), '')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('a', 'a'),
        ('stress', 't'),
        ('moonmen', 'e'),
        ('', ''),
        ('abba', ''),
        ('aa', ''),
        ('~><#~><', '#'),
        ('hello world, eh?', 'w'),
        ('sTreSS', 'T'),
        ('Go hang a salami, I\'m a lasagna hog!', ','),
    )
    for key, val in data:
        assert first_non_repeating_letter(key) == val


if __name__ == '__main__':
    test()
