# 1.单链表的插入、删除、查找操作；
# 2.链表中存储的数据类型是Int
#
# Author:Xuyang

class Node(object):
    """链表结构的Node节点"""

    def __init__(self, data, next_node=None):
        """Node节点的初始化方法
        参数：
            data：存储的数据
            next：下个Node节点的引用地址
        """
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        """Node节点存储数据的获取。
        返回:
            当前Node节点存储的数据
        """
        return self.__data

    @data.setter
    def data(self, data):
        """Node节点存储数据的设置方法。
        参数:
            data:新的存储数据
        """
        self.__data = data

    @property
    def next_node(self):
        """获取Node节点的next指针值。
        返回：
            next指针数据
        """
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        """Node节点next指针的修改方法。
        参数：
            next：新的下一个Node节点的引用
        """
        self.__next = next_node


class SinglyLinkedList(object):
    """单向链表"""

    def __init__(self):
        """单向链表的初始化方法"""
        self.__head = None

    def find_by_value(self, value):
        """按照数据值在单向列表中查找.
        参数:
            value:查找的数据
        返回:
            Node
        """
        node = self.__head
        while (node is not None) and (node.data != value):
            node = node.next_node
        return node

    def find_by_index(self, index):
        """按照索引值在列表中查找.
        参数:
            index:索引值
        返回:
            Node
        """
        node = self.__head
        pos = 0
        while (node is not None) and (pos != index):
            node = node.next_node
            pos += 1
        return node

    def insert_to_head(self, value):
        """在链表的头部插入一个存储value数值的Node节点.
        参数:
            value:将要存储的数据
        """
        node = Node(value)
        node.next_node = self.__head
        self.__head = node

    def insert_after(self, node, value):
        """在链表的某个指定node节点之后，插入一个存储value数据的Node节点
        参数：
            node，指定的一个Node节点
            value，将要存储在新Node节点的数据
        """
        if node is None:  # 如果指定节点为空，则直接返回
            return

        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_before(self, node, value):
        """在链表的某个指定node节点之前，插入一个存储value数据的Node节点
        参数：
            node，指定的一个Node节点
            value，将要存储在新Node节点的数据
        """
        if node is None or self.__head is Node:  # 如果指定节点为空，或者是空链表，则直接返回
            return

        if node == self.__head:
            self.insert_to_head(value)
            return
        new_node = Node(value)
        pro = self.__head
        not_found = False  # 如果在整个链表中都没有找到指定插入的Node节点，则该标记量设置为True
        while pro.next_node != node:  # 寻找指定Node之前的一个Node
            if pro.next_node is None:  # 如果已经到了链表的最后一个节点，则表明该链表中没有找到指定插入的Node节点
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:  # 找到了指定Node之前的一个node
            new_node.next_node = node
            pro.next_node = new_node

    def delete_by_node(self, node):
        """在链表中删除指定Node的节点.
        参数:
            node:指定的Node节点
        """
        if self.__head is None:  # 如果链表是空的，则什么都不做
            return

        if node == self.__head:  # 如果指定删除的Node节点是链表的头节点
            self.__head = node.next_node
            return
        not_found = False
        pro = self.__head
        while pro.next_node != node:
            if pro.next_node is None:  # 没找到
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:  # 找到了指定Node之前的一个node:pro
            pro.next_node = node.next_node

    def delete_by_value(self, value):
        """在链表中删除指定存储数据的Node节点.
        参数:
            value:指定的存储数据
        """
        if self.__head is None:  # 如果链表是空的，则什么都不做
            return

        if value == self.__head.data:  # 如果指定删除的Node节点是链表的头节点
            self.__head = self.__head.next_node
            return

        not_found = False
        pro = self.__head
        node = pro.next_node
        while node.data != value:
            if node is None:
                not_found = True
                break
            else:
                pro = node
                node = pro.next_node
        if not not_found:
            pro.next_node = node.next_node

    def delete_last_n_node(self, n):
        """删除链表中倒数第N个节点.
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点;
            原理是保持快慢指针距离为N，当快指针到末尾时，慢指针正好是倒数第N个节点
        参数:
            n:需要删除的倒数第N个序数
        """
        fast = self.__head
        slow = self.__head
        step = 0

        while step <= n:
            fast = fast.next_node
            step += 1

        while fast.next_node is not None:
            pro = slow
            fast = fast.next_node
            slow = slow.next_node
        pro.next_node = slow.next_node

    def find_mid_node(self):
        """查找链表中的中间节点.
        主体思想:
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
        返回:
            node:链表的中间节点
        """
        fast = self.__head
        slow = self.__head

        while fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node
        return slow

    def create_node(self, value):
        """创建一个存储value值的Node节点.
        参数:
            value:将要存储在Node节点中的数据
        返回:
            一个新的Node节点
        """
        return Node(value)

    def print_all(self):
        """打印当前链表所有节点数据."""
        pos = self.__head
        if pos is None:
            print('None')
            return
        while pos.next_node is not None:
            print(str(pos.data) + '--->', end='')
            pos = pos.next_node
        print(str(pos.data))

    def __iter__(self):
        """# 重写__iter__方法，方便for关键字调用打印值"""
        node = self.__head
        while node:
            yield node.data
            node = node.next_node


if __name__ == '__main__':
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_to_head(i)
    l.print_all()
    node9 = l.find_by_value(9)
    node3 = l.find_by_value(3)
    print(node9.data)
    l.insert_before(node9, 20)
    l.insert_before(node9, 16)
    l.insert_before(node3, 16)
    l.print_all()
    l.delete_by_value(16)
    l.print_all()
    l.delete_by_node(node3)
    l.print_all()
    for item in l:
        print(item)
