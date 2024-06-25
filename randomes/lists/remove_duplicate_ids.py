"""
Вам дана таблица, в которой каждый ключ представляет собой строковое число,
а каждое соответствующее значение представляет собой массив символов, например

{
  "1": ["A", "B", "C"],
  "2": ["A", "B", "D", "A"],
}

Создайте функцию, которая возвращает таблицу с теми же ключами, но каждый
символ должен появляться среди массивов значений только один раз, например

{
  "1": ["C"],
  "2": ["A", "B", "D"],
}

Правила

    Всякий раз, когда две клавиши используют один и тот же символ, их следует
    сравнивать численно , и больший ключ сохранит этот символ.
    Поэтому в примере выше массив под ключом "2" содержит "A" и "B", как 2 > 1.
    Если в одном и том же массиве обнаружены повторяющиеся символы, следует
    сохранить первое вхождение.

Пример 1

input = {
  "1": ["C", "F", "G"],
  "2": ["A", "B", "C"],
  "3": ["A", "B", "D"],
}

output = {
  "1": ["F", "G"],
  "2": ["C"],
  "3": ["A", "B", "D"],
}

Пример 2

input = {
  "1": ["A"],
  "2": ["A"],
  "3": ["A"],
}

output = {
  "1": [],
  "2": [],
  "3": ["A"],
}

Пример 3

input = {
  "432": ["A", "A", "B", "D"],
  "53": ["L", "G", "B", "C"],
  "236": ["L", "A", "X", "G", "H", "X"],
  "11": ["P", "R", "S", "D"],
}

output = {
  "11": ["P", "R", "S"],
  "53": ["C"],
  "236": ["L", "X", "G", "H"],
  "432": ["A", "B", "D"],
}
"""


from functools import reduce


def remove_duplicate_ids(obj: dict[str:list[str]]) -> dict[str:list[str]]:
    """
    Удаляет дубликаты значений среди всего свего словаря, оставляя значение
    максимальному ключу.
    """
    tmp, res = reduce(lambda a, b: a | b, [{x: k for x in set(v)} for k, v in sorted(obj.items(), key=lambda x: int(x[0]))]), {}
    for k, v in tmp.items():
        res[v] = res.get(v, []) + [k]
    return {k: sorted(v, key=obj[k].index) for k, v in res.items()} | {k: [] for k in set(obj) - set(res)}


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ({
            "1": ["A", "B", "C"],
            "2": ["A", "B", "D", "A"],
        },
        {
            "1": ["C"],
            "2": ["A", "B", "D"]
        }),
        ({
            "1": ["C", "F", "G"],
            "2": ["A", "B", "C"],
            "3": ["A", "B", "D"],
        },
        {
            "1": ["F", "G"],
            "2": ["C"],
            "3": ["A", "B", "D"]
        }),
        ({
            "1": ["A"],
            "2": ["A"],
            "3": ["A"],
        },
        {
            "1": [],
            "2": [],
            "3": ["A"]
        }),
        ({
            "432": ["A", "A", "B", "D"],
            "53": ["L", "G", "B", "C"],
            "236": ["L", "A", "X", "G", "H", "X"],
            "11": ["P", "R", "S", "D"],
        },
        {
            "11": ["P", "R", "S"],
            "53": ["C"],
            "236": ["L", "X", "G", "H"],
            "432": ["A", "B", "D"]
        }),
    )
    for key, val in data:
        assert remove_duplicate_ids(key) == val


if __name__ == '__main__':
    test()
