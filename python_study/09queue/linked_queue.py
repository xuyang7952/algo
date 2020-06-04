"""
    Queue based upon linked list

    Author: Xuyang
"""

from typing import Optional


class Node:
    def __init__(self, data: str, next=None):
        self.data = data
        self._next = next


class LinkedQueue:
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

    def enqueue(self, value: str):
        new_node = Node(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def dequeue(self) -> Optional[str]:
        if self._head:
            value = self._head.data
            self._head = self._head._next
            if not self._head:
                self._tail = None
            return value

    def __repr__(self):
        nums = []
        cur = self._head
        while cur:
            nums.append(cur.data)
            cur = cur._next
        return "->".join(str(item) for item in nums)


if __name__ == '__main__':
    q = LinkedQueue()
    for i in range(5):
        q.enqueue(i)
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)
    q.enqueue(5)
    q.enqueue(6)
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)
    q.enqueue(7)
    q.enqueue(8)
    print(q)
