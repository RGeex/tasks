"""
Ваша задача — отсортировать заданную строку. Каждое слово в строке будет содержать одно число.
Это число обозначает позицию, которую слово должно занимать в результате.

Примечание. Числа могут быть от 1 до 9. Таким образом, первым словом будет 1 (а не 0).

Если входная строка пуста, верните пустую строку. Слова во входной строке будут содержать только
допустимые последовательные числа.
Примеры

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""


def order(s: str) -> str:
    """
    Сортирует слова в строке по цифре, содержащийся в их тексте.
    """
    return ' '.join(sorted(s.split(), key=lambda x: next((int(n) for n in x if n.isdigit()), 0)))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("is2 Thi1s T4est 3a", "Thi1s is2 3a T4est"),
        ("4of Fo1r pe6ople g3ood th5e the2", "Fo1r the2 g3ood 4of th5e pe6ople"),
        ("", ""),
    )
    for key, val in data:
        assert order(key) == val


if __name__ == '__main__':
    test()
