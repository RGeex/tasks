"""
Для заданной химической формулы, представленной строкой, подсчитайте
количество атомов каждого элемента, содержащегося в молекуле, и верните
объект (ассоциативный массив в PHP, Dictionary<string, int> в C#,
Map<String,Integer> в Java).

Например:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}

Как видите, в некоторых формулах есть скобки. Индекс вне скобок говорит вам,
что вам нужно умножить количество каждого атома внутри скобок на этот индекс.
Например, в Fe(NO3)2 имеется один атом железа, два атома азота и шесть атомов
кислорода.

Обратите внимание, что скобки могут быть круглыми, квадратными или фигурными,
а также могут быть вложенными . Индекс после фигурных скобок не является
обязательным .
"""


import re


def parse_molecule(formula: str) -> dict:
    """
    Разделяет химическую формулу на отдельные элементы.
    """
    def calc(s: str, n: int = 1, res: dict = {}) -> dict:
        x = re.split(r'(\{.*?\}|\[.*?\]|\(.*?\))(\d*)', s)
        for el, v in re.findall(r'([A-Z][a-z]?)(\d*)', ''.join(x[::3])):
            res[el] = res.get(el, 0) + int(v or 1) * n
        for el, v in zip(x[1::3], x[2::3]):
            calc(el[1:-1], n * int(v or 1))
        return res
    return calc(formula)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("H2O", {'H': 2, 'O': 1}),
        ("B2H6", {'B': 2, 'H': 6}),
        ("C6H12O6", {'C': 6, 'H': 12, 'O': 6}),
        ("Mo(CO)6", {'Mo': 1, 'C': 6, 'O': 6}),
        ("Mg(OH)2", {'Mg': 1, 'O': 2, 'H': 2}),
        ("Fe(C5H5)2", {'Fe': 1, 'C': 10, 'H': 10}),
        ("C2H2(COOH)2", {'C': 4, 'H': 4, 'O': 4}),
        ("(C5H5)Fe(CO)2CH3", {'C': 8, 'H': 8, 'Fe': 1, 'O': 2}),
        ("Pd[P(C6H5)3]4", {'Pd': 1, 'P': 4, 'C': 72, 'H': 60}),
        ("K4[ON(SO3)2]2", {'K': 4,  'O': 14,  'N': 2,  'S': 4}),
        ("As2{Be4C5[BCo3(CO2)3]2}4Cu5", {'As': 2,  'Be': 16,
         'C': 44,  'B': 8,  'Co': 24,  'O': 48,  'Cu': 5}),
        ("{[Co(NH3)4(OH)2]3Co}(SO4)3", {
         'Co': 4, 'N': 12, 'H': 42, 'O': 18, 'S': 3}),
    )
    for key, val in data:
        assert parse_molecule(key) == val


if __name__ == '__main__':
    test()
