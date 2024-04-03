"""
FizzBuzz часто является одной из первых головоломок по программированию, которые люди изучают.
Теперь отмените это с помощью обратного FizzBuzz!

Напишите функцию, которая принимает строку, которая всегда будет допустимым разделом FizzBuzz.
Ваша функция должна возвращать массив, содержащий числа, чтобы сгенерировать данный раздел FizzBuzz.

Примечания:

    Если последовательность может появляться в FizzBuzz несколько раз, верните числа, генерирующие
    первый экземпляр этой последовательности.
    Все числа в последовательности будут больше нуля.
    Вы никогда не получите пустую последовательность.

Примеры

reverse_fizzbuzz("1 2 Fizz 4 Buzz")        -->  [1, 2, 3, 4, 5]
reverse_fizzbuzz("Fizz 688 689 FizzBuzz")  -->  [687, 688, 689, 690]
reverse_fizzbuzz("Fizz Buzz")              -->  [9, 10]
"""


def reverse_fizzbuzz(s: str) -> str:
    """
    Преобразует правильную строку "FizzBuzz" в числовую последовательность.
    """
    s, c = s.split(), dict(zip('Fizz Buzz FizzBuzz'.split(), [3, 5, 15]))
    def f(x=1):
        for i, v in enumerate(s):
            r = r if i else c.get(v, .1) * x
            if (r + i) % c.get(v, .1):
                return f(x+1)
        return r
    x = sum(next(((-i, int(v)) for i, v in enumerate(s) if v.isdigit()), [])) or f()
    return list(range(x, x + len(s)))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("1 2 Fizz 4 Buzz", [1, 2, 3, 4, 5]),
        ("Fizz 688 689 FizzBuzz", [687, 688, 689, 690]),
        ("Fizz Buzz", [9, 10]),
    )
    for key, val in data:
        assert reverse_fizzbuzz(key) == val


if __name__ == '__main__':
    test()
