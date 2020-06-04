""" 二叉树的前序遍历，中序遍历，后序遍历，对于二叉查找树来说，中序遍历就是按顺序打印"""
import queue


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def settag(self, tag=None):
        self.tag = tag


def treeDepth(treenode: TreeNode):
    """计算书的深度，递归计算，递归计算左右子树的深度，如果没有深度，返回0；每一层的返回值+1"""
    if treenode is None:
        return 0
    left_depth = treeDepth(treenode.left)
    rigth_depth = treeDepth(treenode.right)
    return max(left_depth, rigth_depth) + 1


def visit(treenode: TreeNode):
    print(str(treenode.val), end='\t')


def levelOrder(root: TreeNode):
    """广度优先遍历，也是层次遍历，自上而下，自左向右，使用队列数据结果实现："""
    deque = queue.Queue()
    if root is not None:
        deque.put(root)
    # 利用队列的先进先出的特性，实现层次遍历
    while not deque.empty():
        treenode = deque.get()
        visit(treenode)
        if treenode.left is not None:
            deque.put(treenode.left)
        if treenode.right is not None:
            deque.put(treenode.right)


""" 
深度优先遍历--递归遍历
"""


def recursionPreOrder(treenode: TreeNode):
    """前序遍历"""
    if treenode:
        visit(treenode)
        recursionPreOrder(treenode.left)
        recursionPreOrder(treenode.right)


def recursionInOrder(treenode: TreeNode):
    """中序遍历"""
    if treenode:
        recursionInOrder(treenode.left)
        visit(treenode)
        recursionInOrder(treenode.right)


def recursionPostOrder(treenode: TreeNode):
    """后序遍历"""
    if treenode:
        recursionPostOrder(treenode.left)
        recursionPostOrder(treenode.right)
        visit(treenode)


"""
深度优先遍历---非递归遍历,利用栈结构的先进后出的原则
"""


def PreOrderNoRescur(treenode: TreeNode):
    """使用栈数据来保存节点信息，前序遍历"""
    stack = queue.LifoQueue()
    while treenode is not None or not stack.empty():
        if treenode:
            visit(treenode)
            stack.put(treenode.right)  # right的数据压入到堆中
            treenode = treenode.left  # 先取左边的数据
        else:
            treenode = stack.get()


def InOrderNoRescur(treenode: TreeNode):
    """使用栈数据来保存节点信息，中序遍历"""
    stack = queue.LifoQueue()
    while treenode is not None or not stack.empty():
        if treenode:
            stack.put(treenode)  # 根节点和所有左子树中的左节点的数据压入到堆中
            treenode = treenode.left
        else:
            treenode = stack.get()  # 全部放入堆中后依次取出
            visit(treenode)
            treenode = treenode.right


if __name__ == '__main__':
    a = TreeNode('a')

    a1 = TreeNode('a1')
    a2 = TreeNode('a2')

    a11 = TreeNode('a11')
    a12 = TreeNode('a12')
    a21 = TreeNode('a21')
    a22 = TreeNode('a22')

    a111 = TreeNode('a111')
    a112 = TreeNode('a112')
    a121 = TreeNode('a121')
    a122 = TreeNode('a122')
    a211 = TreeNode('a211')
    a212 = TreeNode('a212')
    a221 = TreeNode('a221')
    a222 = TreeNode('a222')

    a.left, a.right = a1, a2
    a1.left, a1.right = a11, a12
    a2.left, a2.right = a21, a22
    a11.left, a11.right = a111, a112
    a12.left, a12.right = a121, a122
    a21.left, a21.right = a211, a212
    a22.left, a22.right = a221, a222

    print("tree depth:")
    print(treeDepth(a))
    print("Level order:")
    levelOrder(a)
    print("\nRecursion pre order:")
    recursionPreOrder(a)
    print("\nRecursion in order:")
    recursionInOrder(a)
    print("\nRecursion post order:")
    recursionPostOrder(a)
