"""
    Stack based upon linked list
    基于链表实现的栈

    Author: Xuyang
"""
from typing import Optional


class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next


class LinkedStack:
    """A stack based upon singly-linked list.
    """

    def __init__(self):
        self.top: Node = None

    def push(self, value: int):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

    def pop(self) -> Optional[int]:
        if self.top:
            value = self.top.data
            self.top = self.top.next
            return value

    def __repr__(self):
        nums = []
        cur = self.top
        while cur:
            nums.append(cur.data)
            cur = cur.next
        return "->".join(f'{num}' for num in nums)


if __name__ == '__main__':
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        print(stack.pop())
    print(stack)
