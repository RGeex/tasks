"""
Дети пьют Тедди.
Подростки пьют Кола.
Молодые люди пьют Пиво.
Взрослые пьют Виски.

Сделайте функцию, которая получает возраст и возвращает то,
что они пьют.

Правила:

Дети до 14 лет.
Подростки до 18 лет.
Молодые до 21 года.
У взрослых 21 и более.
"""


def people_with_age_drink(age: int) -> str:
    """По введеному возрасту определяет предпочтительный написток."""
    data = {
        age < 31: "whisky",
        age < 21: "beer",
        age < 19: "beer",
        age < 18: "coke",
        age < 14: "toddy",
    }
    return f'drink {data.get(1)}'


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = (
        (0, 'drink toddy'),
        (17, 'drink coke'),
        (15, 'drink coke'),
        (14, 'drink coke'),
        (20, 'drink beer'),
        (18, 'drink beer'),
        (13, 'drink toddy'),
        (22, 'drink whisky'),
        (21, 'drink whisky'),
    )

    for key, val in data:
        assert people_with_age_drink(key) == val

if __name__ == '__main__':
    test()