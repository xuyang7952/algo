"""
    Queue based upon array
    用数组实现的队列

    Author: Xuyang
"""
from typing import Optional


class ArrayQueue:
    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        # tail 已经到达数组最后一个节点
        if self._tail == self._capacity:
            # head ==0 意味着满了，不然需要进行数据搬移
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                    # print(self._items)
                self._tail = self._tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None

    def __repr__(self) -> str:
        # print(self._items)
        return " ".join(str(item) for item in self._items[self._head:self._tail])


if __name__ == '__main__':
    arrayqueue = ArrayQueue(5)
    for i in range(6):
        arrayqueue.enqueue(i)
    print(arrayqueue)
    arrayqueue.dequeue()
    arrayqueue.dequeue()
    print(arrayqueue)
    arrayqueue.enqueue(5)
    arrayqueue.enqueue(6)
    print(arrayqueue)
    arrayqueue.dequeue()
    arrayqueue.dequeue()
    print(arrayqueue)
    arrayqueue.enqueue(7)
    arrayqueue.enqueue(8)
    print(arrayqueue)
