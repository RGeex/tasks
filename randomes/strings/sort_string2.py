"""
Задача

Ваша задача — отсортировать символы в строке по следующим правилам:

- Правило 1: английские алфавиты расположены от А до Я, без учета регистра.
  то есть. "Type" --> "epTy"
- Правило 2: Если в английском алфавите существуют прописные и строчные буквы
  при этом они располагаются в порядке ввода.
  то есть. "BabA" --> "aABb"
- Правило 3: неанглийский алфавит остается на исходном месте.
  то есть. "By?e" --> "Be?y"
"""


def sort_string(st: str) -> str:
    """
    Сортирует переданную строку по заданному алгоритму.
    """
    x = sorted([x for x in st if x.isalpha()], key=lambda x: x.lower())
    return ''.join(x.pop(0) if w.isalpha() else w for w in st)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("a","a"),
        ("cba","abc"),
        ("Cba","abC"),
        ("cCBbAa","AaBbcC"),
        ("!","!"),
        ("c b a","a b c"),
        ("-c--b--a-","-a--b--c-"),
        ("cbaCcC","abcCcC"),
        ("Codewars","aCdeorsw"),
    )
    for key, val in data:
        assert sort_string(key) == val


if __name__ == '__main__':
    test()
