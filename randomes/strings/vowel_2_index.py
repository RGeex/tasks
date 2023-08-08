"""
Напишите функцию, которая принимает строку и заменяет все гласные [a,e,i,o,u]
их соответствующими позициями в этой строке.
"""


def vowel_2_index(string: str) -> str:
    """Заменяет гласные Английского языка в слове их позицией в строке."""
    return ''.join(str(i) if x.lower() in 'aeiou' else x for i, x in enumerate(string, 1))


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ('', ''),
        ('this is my string', 'th3s 6s my str15ng'),
        ('Tomorrow is going to be raining',
         'T2m4rr7w 10s g1415ng t20 b23 r2627n29ng'),
        ('Codewars is the best site in the world',
         'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'),
    )

    for key, val in data:
        assert vowel_2_index(key)[:20] == val[:20]


if __name__ == '__main__':
    test()
