"""
Счастливых праздников, дорогие воины кода!

Теперь, Дэшер! Теперь, Дэнсер! Теперь, Прэнсер и Виксен! Вперёд, Комета! Вперёд, Купидон! Вперёд,
Дондер и Блитцен! Именно в таком порядке Санта хотел видеть своих оленей... верно? Что ты имеешь
в виду, когда говоришь, что он хочет, чтобы они были в порядке их фамилий!? Похоже, нам нужна
твоя помощь, Воин Кода!
Сортировать оленей Санты

Напишите функцию, которая принимает последовательность имен оленей и возвращает последовательность
с именами оленей, отсортированными по фамилиям.
Примечания:

    Гарантируется, что каждая строка состоит из двух слов, разделенных одним пробелом.
    В случае двух одинаковых фамилий сохраните первоначальный порядок.

Примеры

Для этого ввода:

[
  "Dasher Tonoyan",
  "Dancer Moore",
  "Prancer Chua",
  "Vixen Hall",
  "Comet Karavani",
  "Cupid Foroutan",
  "Donder Jonker",
  "Blitzen Claus"
]

Вы должны вернуть следующий вывод:

[
  "Prancer Chua",
  "Blitzen Claus",
  "Cupid Foroutan",
  "Vixen Hall",
  "Donder Jonker",
  "Comet Karavani",
  "Dancer Moore",
  "Dasher Tonoyan",
]


"""
import typing
import unittest


def sort_reindeer(reindeer_names: list[str]) -> list[str]:
    """
    Сортировка списка имен, по фамилиям.
    """
    return sorted(reindeer_names, key=lambda x: x.split()[-1])
    

def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_reindeer, (
        (['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada'],['Kenjiro Mori', 'Juzo Okita', 'Akira Sanada', 'Susumu Tokugawa']),
        ([],[]),
        (['Yasuo Kodai', 'Kenjiro Sado', 'Daisuke Aihara', 'Susumu Shima', 'Akira Sanada', 'Yoshikazu Okita', 'Shiro Yabu', 'Sukeharu Nanbu', 'Sakezo Yamamoto', 'Hikozaemon Ohta', 'Juzo Mori', 'Saburo Tokugawa'],['Daisuke Aihara', 'Yasuo Kodai', 'Juzo Mori', 'Sukeharu Nanbu', 'Hikozaemon Ohta', 'Yoshikazu Okita', 'Kenjiro Sado', 'Akira Sanada', 'Susumu Shima', 'Saburo Tokugawa', 'Shiro Yabu', 'Sakezo Yamamoto']),
        (['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'],['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']),
        (["Sukeharu Yamamoto", "Juzo Yabu", "Saburo Shima", "Shiro Sanada", "Daisuke Mori"],['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']),
    ))
