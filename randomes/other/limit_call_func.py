"""
Необходимо сделать проверку на вызов функции не
более указанного числа раз, при привышении лимита
бросать исключение.
"""

from typing import Callable, Any
from functools import wraps


def limit_call_func(limit: int) -> Callable:
    """
    Позволяет переданной функции выполниться не более заданного кол-ва раз.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            func.limit_call = getattr(func, 'limit_call', 0)
            
            if limit <= func.limit_call:
                raise ValueError('Function call limit exceeded')

            result = func(*args, **kwargs)
            func.limit_call += 1
            return result
        return wrapper
    return decorator


def test():
    """
    Тестирование алгоритмов.
    """

    result, limit = 0, 3
    
    @limit_call_func(limit)
    def test_func(x: int) -> int:
        """
        Тестовая функция.
        """
        return x

    for n in range(limit + 1):
        try:
            result = test_func(n)
            assert result < limit
        except ValueError:
            assert result < limit


if __name__ == '__main__':
    test()
