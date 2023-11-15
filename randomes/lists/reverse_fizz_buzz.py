"""
Традиционно в FizzBuzz числа, кратные 3, заменяются на «Fizz», а числа, кратные 5,
заменяются на «Buzz». Но мы также можем сыграть в FizzBuzz с любой другой парой целых чисел.
[n, m]чьи кратные заменены на Fizz и Buzz.

Для последовательности чисел Fizzes, Buzzes и FizzBuzzes найдите числа, кратные которых заменяются
на Fizz и Buzz. Верните их как массив [n, m]

Числа Fizz и Buzz всегда будут целыми числами от 1 до 50, а максимальная длина последовательности
будет равна 100. Числа Fizz и Buzz могут быть равны или равны 1.
Примеры

    Классический ФиззБазз; числа, кратные 3, заменяются на Fizz, числа, кратные 5, заменяются на
    Buzz:

    [1, 2, "Fizz", 4, "Buzz", 6]  ==>  [3, 5]

    Число, кратное 2, заменяется на Fizz, кратное 3 заменяется на Buzz:

    [1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"]  ==>  [2, 3]

    Число, кратное 2, заменяется на Fizz и Buzz:

    [1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]  ==>  [2, 2]

    Шипение = 1, Гул = 6:

    ["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]  ==>  [1, 6]
"""


def reverse_fizz_buzz(array: list[int | str]) -> tuple:
    """
    Обратные преобразования Fizz Buzz для вычисления значений.
    """
    return tuple(next(i for i, v in enumerate(array, 1) if v in (x, 'FizzBuzz')) for x in ('Fizz', 'Buzz'))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([1, 2, "Fizz", 4, "Buzz"], (3, 5)),
        ([1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"], (2, 3)),
        ([1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"], (2, 2)),
        (["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"], (1, 6)),
    )
    for key, val in data:
        assert reverse_fizz_buzz(key) == val


if __name__ == '__main__':
    test()
