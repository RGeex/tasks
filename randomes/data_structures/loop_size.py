"""
Вам дан узел, который является началом связанного списка.
Этот список содержит висящий кусок и петлю. Ваша цель — определить длину цикла.
"""


def loop_size(node: 'Node') -> int:
    """
    Определяет длинну петли связного списка.
    """
    nodes = {}
    while nodes.get(node) is None:
        nodes[node], node = len(nodes), node and node.next
    return len(nodes) - nodes[node] if node and node.next else 0


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    class Node:
        """
        Узел дерева.
        """
        next = None

    nodes = [Node() for _ in range(7)]
    nodes[4].next = nodes[5]
    for node, i in zip(nodes, [1, 2, 3, 1]):
        node.next = nodes[i]

    assert loop_size(nodes[4]) == 0
    assert loop_size(nodes[6]) == 0
    assert loop_size(nodes[0]) == 3
    assert loop_size(nodes[1]) == 3


if __name__ == '__main__':
    test()
