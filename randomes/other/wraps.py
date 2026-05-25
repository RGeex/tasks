"""
Реализуйте декоратор functools.wraps, который используется для сохранения имени и docstring декорируемой функции.
Ваш декоратор не должен изменять поведение декорируемой функции. Вот пример:

def identity(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    \"""Wraps func\"""
    return func(*args, **kwargs)
  return wrapper

@identity
def return_one():
  \"""Return one\"""
  return 1
  
return_one.__name__ == 'return_one' # If wraps hadn't been used, __name__ would be equal to 'wrapper'
return_one.__doc__ == 'Return one' # If wraps hadn't been used, __doc__ would be equal to 'Wraps func'

Примечание: разумеется, вы не можете использовать модуль functools для этого задания.

"""
import unittest
from typing import Any, Callable, Tuple


def wraps(func: Callable) -> Callable:
    """
    Копирует META данные из обернутой функции в обертку.
    """
    def wrapper(wrapped: Callable) -> Callable:
        wrapped.__doc__ = func.__doc__
        wrapped.__name__ = func.__name__
        return wrapped
    return wrapper


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    def identity(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Wraps func"""
            return func(*args, **kwargs)
        return wrapper

    @identity
    def return_one():
        """Return one"""
        return 1

    test(lambda x: x, (
        (return_one.__name__, "return_one"),
        (return_one.__doc__, "Return one"),
        (return_one(), 1),
    ))
