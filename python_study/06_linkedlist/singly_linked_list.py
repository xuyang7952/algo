"""
    1) Insertion, deletion and search of singly-linked list;
    2) Assumes int type for data in list nodes.

    Author: Xuyang
"""
from typing import Optional


class Node:
    def __init__(self, data: int, next_node=None):
        self.data = data
        self._next = next_node


class SinglyLinkedList:

    def __init__(self):
        self._head = None

    def find_by_value(self, value: int) -> Optional[Node]:
        p = self._head
        while p and p.data != value:
            p = p._next
        return p

    def find_by_index(self, index: int) -> Optional[Node]:
        p = self._head
        pos = 0
        while p and pos != index:
            p = p._next
            pos += 1
        return p

    def insert_node_to_head(self, new_node: Node):
        if new_node:
            new_node._next = self._head
            self._head = new_node

    def insert_value_to_head(self, value: int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_after(self, node: Node, new_node: Node):
        if not node or not new_node:
            return
        new_node._next = node._next
        node._next = new_node

    def insert_value_after(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        if not node or not new_node:
            return

        if node == self._head:
            self.insert_node_to_head(new_node)
        pro = self._head
        while pro._next and pro != node:
            pro = pro._next
        if not pro._next:  # 没有找到node，无法插入
            return
        new_node._next = node
        pro._next = new_node

    def insert_value_before(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def print_all(self):
        current = self._head
        if current:
            print(f"{current.data}", end="")
            current = current._next
        while current:
            print(f"->{current.data}", end="")
            current = current._next
        print("\n", flush=True)


if __name__ == '__main__':
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_node_to_head(i)
    print(l)
