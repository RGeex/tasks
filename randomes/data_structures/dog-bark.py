"""
#Заставьте их лаять

Вас нанял заводчик собак для написания программы по ведению учета его собак.

Вы уже создали конструктор. Dog,
чтобы никому не приходилось вручную прописывать код для каждого щенка.

Работа, кажется, завершена. Давно пора получить оплату.

...подождите! Заводчик собак говорит, что не заплатит вам, пока не заставит каждую собаку возражать.
.bark()Даже те, которые уже созданы с помощью вашего конструктора. «Все собаки лают», — говорит он.
И он отказывается их переписывать, несмотря на свою лень.

Вы даже не можете сосчитать, сколько предметов уже изготовил ваш мерзавец-клиент.
У него много собак, и ни одна из них не может... .bark().

Сможете ли вы решить эту проблему, или позволите клиенту перехитрить вас раз и навсегда?
Практическая информация:

    Он .bark()Метод собаки должен возвращать строку 'Woof!'.

    Созданный вами конструктор (он предварительно загружен) выглядит так:

class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age

    Подсказка: Ваш друг только что рассказал вам о том, как JavaScript обрабатывает классы иначе,
    чем другие языки программирования. Он не переставал рассуждать о «прототипах» или чем-то подобном.
    Возможно, это вам поможет...

"""
import unittest
from typing import Any, Callable, Tuple


class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age


Dog.bark = lambda x: 'Woof!'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    apollo = Dog('Apollo', 'Dobermann', 'male', 4)
    zeus = Dog('Zeus', 'Dobermann', 'male', 4)
    test(lambda x: x, (
        (apollo.bark(), 'Woof!'),
        (zeus.bark(), 'Woof!'),
    ))
