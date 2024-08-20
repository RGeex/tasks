"""
Ваша задача в этой ката — эмулировать выравнивание текста прямо моноширинным
шрифтом. Вам будет предоставлен однострочный текст и ожидаемая ширина
выравнивания. Самое длинное слово никогда не будет больше этой ширины.

Вот правила:

    Используйте пробелы, чтобы заполнить пробелы в левой части слов.
    Каждая строка должна содержать как можно больше слов.
    Используйте '\n' для разделения строк.
    Пробел между словами не может отличаться более чем на один пробел.
    Строки должны заканчиваться словом, а не пробелом.
    '\n' не включается в длину строки.
    Последняя строка не должна содержать '\n'

Пример с шириной = 30:

        Bacon ipsum dolor amet
excepteur ut kevin burgdoggen,
   shankle cupim dolor officia
       ground round id ullamco
   deserunt nisi. Commodo tail
    qui salami, brisket boudin 
tri-tip. Labore flank laboris,
  cow enim proident aliqua sed
      hamburger consequat. Sed
     consequat ut non bresaola
   capicola shoulder excepteur
 veniam, bacon kevin. Pastrami
   shank laborum est excepteur
 non eiusmod bresaola flank in
nostrud. Corned beef ex pig do
   kevin filet mignon in irure
 deserunt ipsum qui duis short
        loin. Beef ribs dolore
  meatball officia rump fugiat
  in enim corned beef non est.

"""


def align_right(text: str, width: int) -> str:
    """
    Выразнивает заданный текст по правому краю, ограничивая заданным значением длину строки.
    """
    res, tmp = [], ''
    for w in text.split() + [None]:
        tmp = not res.append(f'{tmp:>{width}}') and w if w is None or len(w) + len(tmp) + 1 > width else tmp + f'{" " * bool(tmp)}{w}'
    return '\n'.join(res)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("abc def",10),'   abc def'),
        (("I take up the whole line",24),'I take up the whole line'),
        (("Two lines, I am",10),'Two lines,\n      I am'),
    )
    for key, val in data:
        assert align_right(*key) == val


if __name__ == '__main__':
    test()
