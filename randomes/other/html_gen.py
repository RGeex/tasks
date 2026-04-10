"""
Ещё один замечательный день в стремительном мире веб-разработки. Да, ты любишь свою работу!
Но, как и в любой работе, иногда бывает немного утомительно. Часть сайта, над которым ты
работаешь, имеет очень повторяющуюся структуру, и писать весь HTML вручную — скучно.
Пора автоматизировать! Ты хочешь написать несколько функций,
которые будут генерировать HTML за тебя.

Для организации кода сделайте все ваши функции методами класса с именем HTMLGen.
Функции тегов следует называть в честь тега создаваемого элемента. Каждая функция
будет принимать один аргумент — строку, которая представляет собой внутренний HTML-код
создаваемого элемента. Функции будут возвращать строку для соответствующего HTML-элемента.

Например,

Python:

g = HTMLGen();
paragraph = g.p('Hello, World!')
block = g.div(paragraph)

# The following are now true
paragraph == '<p>Hello, World!</p>'
block == '<div><p>Hello, World!</p></div>'

В вашем классе HTMLGen должны быть методы для создания следующих элементов:

    а
    б
    п
    тело
    див
    охватывать
    заголовок
    комментарий

Примечание: Метод `comment` должен заключать свой аргумент в HTML-комментарий.
Это единственный метод, имя которого не совпадает с HTML-тегом. Таким образом,
g.comment('i am a comment')должен производить <!--i am a comment-->.
"""
import unittest
from typing import Any, Callable, Tuple


class HTMLGen:
    """
    Генерирует HTML тэги.
    """
    def __getattr__(self, name):
        if name in 'a b p body div span title comment'.split():
            return lambda val: f'<!--{val}-->' if name == 'comment' else f'<{name}>{val}</{name}>'
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    htmlGen = HTMLGen()
    test(lambda x: x, (
        (htmlGen.a('test'), '<a>test</a>'),
        (htmlGen.comment('test'), '<!--test-->'),
    ))
