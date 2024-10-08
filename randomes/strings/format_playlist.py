"""
Ваша задача — написать функцию с именем format_playlist, для этого требуется список songs в качестве ввода.

Каждая песня представляет собой кортеж вида (song_name, duration, artist). Ваша задача — создать строковое представление этих песен.

Ваш плейлист должен быть отсортирован сначала по исполнителю, а затем по названию песни.

Примечание:

    Все введенные данные будут действительными.
    Продолжительность песни должна составлять не менее 1 минуты, но не 10 минут и более. Это будет иметь форму m:ss.
    Никогда не будет пустых полей (у каждой песни будет название, продолжительность и исполнитель).

Например, если вашей функции было передано следующее songs.

songs = [
    ('In Da Club', '3:13', '50 Cent'),
    ('Candy Shop', '3:45', '50 Cent'),
    ('One', '4:36', 'U2'),
    ('Wicked', '2:53', 'Future'),
    ('Cellular', '2:58', 'King Krule'),
    ('The Birthday Party', '4:45', 'The 1975'),
    ('In The Night Of Wilderness', '5:26', 'Blackmill'),
    ('Pull Up', '3:35', 'Playboi Carti'),
    ('Cudi Montage', '3:16', 'KIDS SEE GHOSTS'),
    ('What Up Gangsta', '2:58', '50 Cent')
]

Тогда ваша функция вернет следующее:

+----------------------------+------+-----------------+
| Name                       | Time | Artist          |
+----------------------------+------+-----------------+
| Candy Shop                 | 3:45 | 50 Cent         |
| In Da Club                 | 3:13 | 50 Cent         |
| What Up Gangsta            | 2:58 | 50 Cent         |
| In The Night Of Wilderness | 5:26 | Blackmill       |
| Wicked                     | 2:53 | Future          |
| Cudi Montage               | 3:16 | KIDS SEE GHOSTS |
| Cellular                   | 2:58 | King Krule      |
| Pull Up                    | 3:35 | Playboi Carti   |
| The Birthday Party         | 4:45 | The 1975        |
| One                        | 4:36 | U2              |
+----------------------------+------+-----------------+
""" 


def format_playlist(arr: list[tuple[str]]) -> str:
    """
    Отрисовывает плейлист в виде таблицы.
    """
    ttl, arr = ['Name Time Artist'.split()], sorted(arr, key=lambda x: (x[2], x[0]))

    def draw(txt: str='-') -> str:
        """
        Отрисовывает одну строку.
        """
        txt, c, dl = (['-'] * 3, txt, '+') if isinstance(txt, str) else (txt, ' ', '|')
        return dl + f'{dl}'.join([f'{c}{s:{c}<{n}}{c}' for n, s in zip([max(map(len, n)) for n in zip(*ttl + arr)], txt)]) + dl + '\n'

    return draw() + draw(*ttl) + [f'{draw()}'.join(['', ''.join(map(draw, arr)), '']), draw()][not arr].rstrip('\n')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            [],
            "+------+------+--------+\n" \
            "| Name | Time | Artist |\n" \
            "+------+------+--------+",
        ),
        (
            [('MILK', '4:55', 'BROCKHAMPTON')],
            "+------+------+--------------+\n" \
            "| Name | Time | Artist       |\n" \
            "+------+------+--------------+\n" \
            "| MILK | 4:55 | BROCKHAMPTON |\n" \
            "+------+------+--------------+", 
        ), 
        (
            [
                ('Stoned Again', '3:25', 'King Krule'),
                ('Serenade', '3:00', 'Travis Scott'),
                ('I Always Wanna Die (Sometimes)', '5:15', 'The 1975'),
                ('Stick Talk', '2:54', 'Future'),
                ('Nightcrawler', '5:22', 'Travis Scott')
            ],
            "+--------------------------------+------+--------------+\n" \
            "| Name                           | Time | Artist       |\n" \
            "+--------------------------------+------+--------------+\n" \
            "| Stick Talk                     | 2:54 | Future       |\n" \
            "| Stoned Again                   | 3:25 | King Krule   |\n" \
            "| I Always Wanna Die (Sometimes) | 5:15 | The 1975     |\n" \
            "| Nightcrawler                   | 5:22 | Travis Scott |\n" \
            "| Serenade                       | 3:00 | Travis Scott |\n" \
            "+--------------------------------+------+--------------+",
        ),                  
        (
            [
                ('In Da Club', '3:13', '50 Cent'),
                ('Candy Shop', '3:45', '50 Cent'),
                ('One', '4:36', 'U2'),
                ('Wicked', '2:53', 'Future'),
                ('Cellular', '2:58', 'King Krule'),
                ('The Birthday Party', '4:45', 'The 1975'),
                ('In The Night Of Wilderness', '5:26', 'Blackmill'),
                ('Pull Up', '3:35', 'Playboi Carti'),
                ('Cudi Montage', '3:16', 'KIDS SEE GHOSTS'),
                ('What Up Gangsta', '2:58', '50 Cent')
            ],
            "+----------------------------+------+-----------------+\n" \
            "| Name                       | Time | Artist          |\n" \
            "+----------------------------+------+-----------------+\n" \
            "| Candy Shop                 | 3:45 | 50 Cent         |\n" \
            "| In Da Club                 | 3:13 | 50 Cent         |\n" \
            "| What Up Gangsta            | 2:58 | 50 Cent         |\n" \
            "| In The Night Of Wilderness | 5:26 | Blackmill       |\n" \
            "| Wicked                     | 2:53 | Future          |\n" \
            "| Cudi Montage               | 3:16 | KIDS SEE GHOSTS |\n" \
            "| Cellular                   | 2:58 | King Krule      |\n" \
            "| Pull Up                    | 3:35 | Playboi Carti   |\n" \
            "| The Birthday Party         | 4:45 | The 1975        |\n" \
            "| One                        | 4:36 | U2              |\n" \
            "+----------------------------+------+-----------------+", 
        ), 
    )
    for key, val in data:
        assert format_playlist(key) == val


if __name__ == '__main__':
    test()
