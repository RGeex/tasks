"""
Однажды, по пути через старый дикий гористый запад,...

…человеку дали указания пройти из одной точки в другую. Направления были «СЕВЕР», «ЮГ», «ЗАПАД»,
«ВОСТОК». Очевидно, что «СЕВЕР» и «ЮГ» противоположны, «ЗАПАД» и «ВОСТОК» тоже.

возвращаться в противоположном Идти в одном направлении и сразу же — бесполезное усилие.
Поскольку это Дикий Запад, с ужасной погодой и небольшим количеством воды, важно сэкономить немного
энергии, иначе вы можете умереть от жажды!
пересек гористую пустыню. Как я ловко

Указания, данные мужчине, например, следующие (в зависимости от языка):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]

Сразу видно, что идти «НА СЕВЕР» и сразу «ЮГ» не разумно, лучше оставаться на том же месте! Итак,
задача — дать человеку упрощенный вариант плана. Лучший план в этом случае:

["WEST"]
or
{ "WEST" }
or
[West]

Другие примеры:

В ["NORTH", "SOUTH", "EAST", "WEST"], направление "NORTH" + "SOUTH"идет на север и тут же
возвращается .

Путь становится ["EAST", "WEST"], сейчас "EAST"и "WEST"уничтожают друг друга, поэтому конечный
результат [](ноль в Clojure).

В ["СЕВЕР", "ВОСТОК", "ЗАПАД", "ЮГ", "ЗАПАД", "ЗАПАД"], "СЕВЕР" и "ЮГ" не являются прямо
противоположными, но становятся прямо противоположными после сокращения слова "ВОСТОК" и "WEST",
поэтому весь путь можно свести к ["WEST", "WEST"].
Задача

Напишите функцию dirReducкоторый принимает массив строк и возвращает массив строк с удаленными
ненужными направлениями (W<->E или S<->N рядом ).

    Версия Haskell принимает список направлений с data Direction = North | East | West | South.
    Версия Clojure возвращает ноль, когда путь сводится к нулю.
    Версия Rust требует немного enum Direction {North, East, West, South}.
"""


def dir_reduc(arr: list[str]) -> list[str]:
    """
    Убирает из маршрута лишние шаги.
    """
    way = dict(((w := 'NORTH SOUTH EAST WEST'.split()) + w[::-1])[i*2:i*2+2] for i in range(4))
    return next((dir_reduc(arr[:i] + arr[i+2:]) for i in range(len(arr) - 1) if arr[i] == way.get(arr[i+1])), arr)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([], []),
        (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"], []),
        (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"], ["NORTH"]),
        (["NORTH", "WEST", "SOUTH", "EAST"], ["NORTH", "WEST", "SOUTH", "EAST"]),
        (["NORTH", "WEST", "SOUTH", "EAST"], ["NORTH", "WEST", "SOUTH", "EAST"]),
        (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"], ['WEST']),
        (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"], ['WEST']),
        (["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"], ["EAST", "NORTH"]),
        (["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"], ["NORTH", "EAST"]),
        (["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH", "WEST", "EAST"], ['NORTH', 'NORTH']),
        (['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH'], ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH']),
    )
    for key, val in data:
        assert dir_reduc(key) == val


if __name__ == '__main__':
    test()
