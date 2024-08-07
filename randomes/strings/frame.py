"""
Описание:

*************************
*  Create a frame!      *
*           __     __   *
*          /  \~~~/  \  *
*    ,----(     ..    ) *
*   /      \__     __/  *
*  /|         (\  |(    *
* ^  \  /___\  /\ |     *
*    |__|   |__|-..     *
*************************

Учитывая массив строк и символ, который будет использоваться в качестве
границы, выведите фрейм с содержимым внутри.

Примечания:

    Всегда оставляйте пробел между входной строкой и левой и правой границами.
    Самая большая строка внутри массива всегда должна помещаться в рамку.
    Входной массив никогда не бывает пустым.

Пример

frame(['Create', 'a', 'frame'], '+')

Выход:

++++++++++
+ Create +
+ a      +
+ frame  +
++++++++++
"""


def frame(arr: list[str], w: str) -> str:
    """
    Обрамляет рамкой заданный текст.
    """
    return '\n'.join((x := [w * ((m := max(map(len, arr))) + 4)]) + [f'{w} {x:<{m}} {w}' for x in arr] + x)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((['Small', 'frame'], '~'), '~~~~~~~~~\n~ Small ~\n~ frame ~\n~~~~~~~~~'),
        ((['Create','this','kata'], '+'), '++++++++++\n+ Create +\n+ this   +\n+ kata   +\n++++++++++'),
        ((['This is a very long single frame'], '-'), '------------------------------------\n- This is a very long single frame -\n------------------------------------'),
    )
    for key, val in data:
        assert frame(*key) == val


if __name__ == '__main__':
    test()
