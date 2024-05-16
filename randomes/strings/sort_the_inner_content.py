"""
Вам необходимо отсортировать внутреннее содержимое каждого слова строки в
порядке убывания.

Внутреннее содержимое — это содержимое слова без первого и последнего символа.

Некоторые примеры:

"sort the inner content in descending order"  -->  "srot the inner ctonnet in
dsnnieedcg oredr"
"wait for me"        -->  "wiat for me"
"this kata is easy"  -->  "tihs ktaa is esay"

Слова состоят из строчных букв.

Строка никогда не будет нулевой и никогда не будет пустой. В C/C++ строка
всегда заканчивается нулем.
"""


def sort_the_inner_content(words: str) -> str:
    """
    Сортирует в порядке убывания символы каждого слова, не
    затрагивая первый и последний.
    """
    return ' '.join(f'{"".join(sorted(w[1:-1], reverse=True))}'.join(w[::len(w) - 1 or 1]) for w in words.split())


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("sort the inner content in descending order", "srot the inner ctonnet in dsnnieedcg oredr"),
        ("wait for me", "wiat for me"),
        ("this kata is easy", "tihs ktaa is esay"),
    )
    for key, val in data:
        assert sort_the_inner_content(key) == val


if __name__ == '__main__':
    test()
