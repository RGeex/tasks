"""
Гэри любит картинки, но ему также нравятся слова и чтение. У него давно было желание увидеть,
как бы выглядели слова и книги, если бы их можно было рассматривать как изображения.

Для этой задачи вам необходимо взять непрерывную строку, которая может состоять из любой
комбинации слов или символов, а затем преобразовать слова, составляющие эту строку,
в шестнадцатеричные значения, которые затем можно будет прочитать как значения цвета.

Слово определяется как последовательность символов ASCII между двумя пробелами или
первым или последним словом последовательности слов.

Каждое слово будет представлять собой шестнадцатеричное значение, если взять первые
три буквы каждого слова и найти код символа ASCII для каждого символа. Это даст вам одно
шестнадцатеричное значение, которое представляет красный, зеленый или синий цвета.
Затем вы объедините эти значения в одно читаемое шестнадцатеричное значение RGB, например #ffffff.

Если ваше слово состоит менее чем из 3 букв, вам следует использовать шестнадцатеричное
значение. 00, то есть "It" вернет значение #497400.

Ваш ответ должен представлять собой массив шестнадцатеричных значений, соответствующих
каждому слову, составляющему исходную строку.
Пример

Будет дана следующая строка:

"Hello, my name is Gary and I like cheese."

Эта строка вернет следующий массив:

['#48656c', '#6d7900', '#6e616d','#697300','#476172','#616e64','#490000','#6c696b','#636865']
"""


def words_to_hex(words: str) -> list[str]:
    """
    Преобразует слова предложения в цвета, по первым 3-м символам слова.
    """
    return [f"#{''.join([hex(ord(x))[2:] for x in w[:3]]):0<6}" for w in words.split()]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("Hello, my name is Gary and I like cheese.", ['#48656c', '#6d7900', '#6e616d','#697300','#476172','#616e64','#490000','#6c696b','#636865']),
        ("0123456789", [ '#303132' ]),
        ("ThisIsOneLongSentenceThatConsistsOfWords", [ '#546869' ]),
        ("Blah blah blah blaaaaaaaaaaaah", [ '#426c61', '#626c61', '#626c61', '#626c61' ]),
        ("&&&&& $$$$$ ^^^^^ @@@@@ ()()()()(", [ '#262626', '#242424', '#5e5e5e', '#404040', '#282928' ]),
    )
    for key, val in data:
        assert words_to_hex(key) == val


if __name__ == '__main__':
    test()
