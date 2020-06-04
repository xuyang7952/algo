"""
循环队列
"""
from typing import Optional
from itertools import chain


class CircularQueue:
    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        # 循环队列，队列满的时候，当队满时，(tail+1)%n=head
        if (self._tail + 1) % (self._capacity) == self._head:
            return False
        self._items.append(item)
        self._tail = (self._tail + 1) % (self._capacity)
        return True

    def dequeue(self) -> Optional[str]:
        if self._tail != self._head:
            item = self._items[self._head]
            self._head = (self._head + 1) % (self._capacity)
            return item

    def __repr__(self) -> str:
        print("item:", self._items)
        if self._tail >= self._head:
            return " ".join(str(item) for item in self._items[self._head:self._tail])
        else:
            return " ".join(str(item) for item in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == '__main__':
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(i)
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)
    q.enqueue(5)
    print(q)

