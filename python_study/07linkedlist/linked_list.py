"""
    1) Reverse singly-linked list
    2) Detect cycle in a list
    3) Merge two sorted lists
    4) Remove nth node from the end
    5) Find middle node

    Author: Xuyang
"""

from typing import Optional


class Node:

    def __init__(self, data: int, next=None):
        self.data = data
        self._next = next


# Reverse singly-linked list
# 单链表反转
# Note that the input is assumed to be a Node, not a linked list.
def reverse(head: Node) -> Optional[Node]:
    reverse_head = None
    current = head
    while current:
        reverse_head, reverse_head._next, current = current, reverse_head, current._next
    return reverse_head


# Detect cycle in a list
# 检测环
def has_cycle(head: Node) -> bool:
    slow, fast = head, head
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        if slow == fast:
            return True
    return False


# Merge two sorted linked list
# 有序链表合并
def merge_sorted_list(l1: Node, l2: Node) -> Optional[Node]:
    if l1 and l2:
        p1, p2 = l1, l2
        fake_head = Node(None)
        current = fake_head
        while p1 and p2:
            if p1.data <= p2.data:
                current._next = p1
                p1 = p1._next
            else:
                current._next = p2
                p2 = p2._next
            current = current._next
        # p1,p2 还有剩余
        current._next = p1 if p1 else p2
        return fake_head._next
    return l1 or l2


# Remove nth node from the end
# 删除倒数第n个节点。假设n大于0
def remove_nth_from_end(head: Node, n: int) -> Optional[Node]:
    fast, slow = head, head
    cnt = 0
    while fast and cnt < n:
        fast = fast._next
        cnt += 1
    if not fast and cnt < n:
        return head
    if not fast and cnt == n:
        return head._next

    while fast._next:
        fast, slow = fast._next, slow._next
    # 执行删除
    slow._next = slow._next._next


def find_middle_node(head: Node) -> Optional[Node]:
    slow, fast = head, head
    fast = fast._next if fast else None
    while fast and fast._next:
        slow, fast = slow._next, fast._next._next
    return slow


def print_all(head: Node) -> Optional[Node]:
    nums = []
    cur = head
    while cur:
        nums.append(str(cur.data))
        cur = cur._next
    print('->'.join(nums))
