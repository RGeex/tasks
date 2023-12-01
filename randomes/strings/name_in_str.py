"""
Что в имени?

...Вернее, в чём заключается имя? Для нас конкретная строка — это место, где мы ищем имя.
Задача

Напишите функцию, принимающую в качестве параметра две строки и проверяющую, содержит ли первая
строка все буквы второй строки по порядку.

Функция должна вернуть trueесли это так, и еще false. Сравнение букв должно быть чувствительным
к регистру.

Примеры

    "Across the rivers", "chris" --> true
      ^      ^  ^^   ^
      c      h  ri   s
                
    Contains all of the letters in "chris", in order.
----------------------------------------------------------
    "Next to a lake", "chris" --> false

    Contains none of the letters in "chris".
--------------------------------------------------------------------
    "Under a sea", "chris" --> false
         ^   ^
         r   s

    Contains only some of the letters in "chris".
--------------------------------------------------------------------
    "A crew that boards the ship", "chris" --> false
       cr    h              s i
       cr                h  s i  
       c     h      r       s i
                 ...
          
    Contains all of the letters in "chris", but not in order.
--------------------------------------------------------------------
    "A live son", "Allison" --> false
     ^ ^^   ^^^
     A li   son
            
    Contains all of the correct letters in "Allison", in order, but not enough of all of them
    (missing an 'l').
"""


def name_in_str(a: str, b: str) -> bool:
    """
    Проверяет сохраняется ли порядок букв в одной строке из другой, если они есть.
    """
    return bool(next((1 for i, x in enumerate(a.lower()) if b.lower()[(n := not i or n) - 1] == x and (n := n + 1) == len(b) + 1), 0))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("Across the rivers", "chris"), True),
        (("Next to a lake", "chris"), False),
        (("Under a sea", "chris"), False),
        (("A crew that boards the ship", "chris"), False),
        (("A live son", "Allison"), False),
        (("Just enough nice friends", "Jennifer"), False),
        (("thomas", "Thomas"), True),
        (("pippippi", "Pippi"), True),
        (("pipipp", "Pippi"), False),
        (("ppipip", "Pippi"), False),
    )
    for key, val in data:
        assert name_in_str(*key) == val


if __name__ == '__main__':
    test()
