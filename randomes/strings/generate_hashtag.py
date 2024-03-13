"""
Маркетинговая команда тратит слишком много времени на ввод хэштегов.
Давайте поможем им с помощью нашего собственного генератора хэштегов!

Вот сделка:

    Он должен начинаться с хэштега ( #).
    Во всех словах первая буква должна быть заглавной.
    Если окончательный результат длиннее 140 символов, он должен вернуть false.
    Если ввод или результат представляют собой пустую строку, он должен вернуть false.

Примеры

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


def generate_hashtag(s: str) -> str | bool:
    """
    Из заданной строки создает её хештег если эти возможно или возвращает False.
    """
    return 0 < len(x := ''.join(s.title().split())) < 140 and f'#{x}'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('', False),
        ('c i n', '#CIN'),
        ('Codewars', '#Codewars'),
        (f'L{"o" * 150}ng Cat', False),
        ('Codewars      ', '#Codewars'),
        ('      Codewars', '#Codewars'),
        ('CoDeWaRs is niCe', '#CodewarsIsNice'),
        ('Codewars Is Nice', '#CodewarsIsNice'),
        ('codewars is nice', '#CodewarsIsNice'),
        ('codewars  is  nice', '#CodewarsIsNice'),
    )
    for key, val in data:
        assert generate_hashtag(key) == val


if __name__ == '__main__':
    test()
