"""
Встроенная функция печати экземпляров классов Python не очень интересна.

В этой ката мы реализуем функцию show_me(instance) который принимает экземпляр
в качестве параметра и возвращает строку "Hi, I'm one of those (classname)s!
Have a look at my (attrs)." , где (classname) — имя класса, а (attrs) — его атрибуты.
Если (attrs) содержит только один элемент, просто напишите его. Для более чем одного
элемента (например, a, b, c) необходимо перечислить все элементы, отсортированные по
имени в порядке возрастания (например, «... посмотри на мои a, b и c.»).

Пример: Для примера porsche = Vehicle(2, 4, 'gas') класса

class Vehicle:
    def __init__(self, seats, wheels, engine):
        self.seats = seats
        self.wheels = wheels
        self.engine = engine

вызов функции show_me(porsche) должен вернуть строку "Hi, I'm one of those
Vehicles! Have a look at my engine, seats and wheels.".
"""


def show_me(s) -> str:
    """
    Получает класс с атрибутами и выводит в строку его название и названия атрибутов.
    """
    return f"Hi, I'm one of those {s.__class__.__name__}s! Have a look at my {' and'.join(', '.join(sorted(s.__dict__)).rsplit(',', 1))}."


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    class Vehicle:
        def __init__(self, seats, wheels, engine):
            self.seats = seats
            self.wheels = wheels
            self.engine = engine
        
    class Planet:
        def __init__(self, moon):
            self.moon = moon

    data = (
        (Vehicle(2, 4, 'Gas'), "Hi, I'm one of those Vehicles! Have a look at my engine, seats and wheels."),
        (Planet('moon'), "Hi, I'm one of those Planets! Have a look at my moon."),
    )
    for key, val in data:
        assert show_me(key) == val


if __name__ == '__main__':
    test()
