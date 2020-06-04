"""
    Author: Wenru
"""

from typing import Optional


class Dynamicq:

    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0: return False

            self._items[0: self._tail - self._head] = self._items[self._head: self._tail]
            self._tail -= self._head
            self._head = 0
            print(self._items)

        # 保证列表的长度，列表未满的时候，直接添加，列表满的时候，tail的值不等于列表长度，直接用下标赋值，保证列表不会像insert那样超出长度
        if self._tail == len(self._items):
            self._items.append(item)
            print(self._items)
        else:
            self._items[self._tail] = item
            print(self._items)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item

    def __repr__(self) -> str:
        print(self._items)
        return " ".join(str(item) for item in self._items[self._head:self._tail])


if __name__ == "__main__":
    q = Dynamicq(5)
    for i in range(6):
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
