"""
Языки

Сочинения Гэндальфа уже давно доступны для изучения, но никто до сих пор не выяснил, на каком языке
они написаны. Недавно благодаря программной работе хакера, известного только под кодовым именем
ROT13, было обнаружено, что Гэндальф не использовал ничего, кроме простая схема замены букв, и,
кроме того, она сама по себе обратна: одна и та же операция шифрует сообщение, как и расшифровывает
его.

Данная операция выполняется путем замены гласных в последовательности 'a' 'i' 'y' 'e' 'o' 'u' с
тремя гласными, циклически продвигаясь вперед, сохраняя регистр (т. е. нижний или верхний).

Аналогично заменяются согласные из последовательности
'b' 'k' 'x' 'z' 'n' 'h' 'd' 'c' 'w' 'g' 'p' 'v' 'j' 'q' 't' 's' 'r' 'l' 'm' 'f' продвинув вперед
десять букв.

Так, например, фраза 'One ring to rule them all.' переводится на 'Ita dotf ni dyca nsaw ecc.'

Самое интересное в этом преобразовании то, что в результате получается произносимые слова. Для
решения этой задачи вы напишете код для перевода рукописей Гэндальфа в обычный текст.

Ваша задача — написать функцию, которая расшифровывает записи Гэндальфа.
Вход

Функции будет передана строка для декодирования. Каждая строка будет содержать до 100 символов,
представляющих текст, написанный Гэндальфом. Все символы будут в формате ASCII в диапазоне от (32)
до тильды (126).
Выход

Для каждой строки, переданной функции декодирования, возвращается ее перевод.
"""
import typing


def tongues(st: str) -> str:
    """
    Производит замену букв, гласных со сдвигом на 3 символа,
    согласных на 10 символов.
    """
    trans = (
        'aiyeoubkxznhdcwgpvjqtsrlmfAIYEOUBKXZNHDCWGPVJQTSRLMF',
        'eouaiypvjqtsrlmfbkxznhdcwgEOUAIYPVJQTSRLMFBKXZNHDCWG'
    )
    return st.translate(str.maketrans(*trans))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(tongues, (
        ('Ita dotf ni dyca nsaw ecc.', 'One ring to rule them all.'),
        ('Tim oh nsa nowa gid ecc fiir wat ni liwa ni nsa eor ig nsaod liytndu.', 'Now is the time for all good men to come to the aid of their country.'),
        ('Giydhlida etr hakat uaedh efi iyd gidagensadh pdiyfsn ytni nsoh', 'Fourscore and seven years ago our forefathers brought unto this'),
        ('litnotatn e tam tenoit.', 'continent a new nation.'),
        ('Nsa zyolv pdimt gij xywbar ikad nsa cequ rifh.', 'The quick brown fox jumped over the lazy dogs.'),
    ))
