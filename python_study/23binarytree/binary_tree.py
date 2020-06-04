""" 二叉树的前序遍历，中序遍历，后序遍历，对于二叉查找树来说，中序遍历就是按顺序打印"""

from typing import TypeVar, Generic, Generator, Optional

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, value: T):
        self.val = value
        self.left = None
        self.right = None


def pre_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield root.val
        yield from pre_order(root.left)
        yield from pre_order(root.right)


def in_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from in_order(root.left)
        yield root.val
        yield from in_order(root.right)


def post_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from in_order(root.left)
        yield from in_order(root.right)
        yield root.val


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

    print(list(pre_order(a)))
    print(list(in_order(a)))
    print(list(post_order(a)))


    singer = TreeNode("Taylor Swift")

    genre_country = TreeNode("Country")
    genre_pop = TreeNode("Pop")

    album_fearless = TreeNode("Fearless")
    album_red = TreeNode("Red")
    album_1989 = TreeNode("1989")
    album_reputation = TreeNode("Reputation")

    song_ls = TreeNode("Love Story")
    song_wh = TreeNode("White Horse")
    song_wanegbt = TreeNode("We Are Never Ever Getting Back Together")
    song_ikywt = TreeNode("I Knew You Were Trouble")
    song_sio = TreeNode("Shake It Off")
    song_bb = TreeNode("Bad Blood")
    song_lwymmd = TreeNode("Look What You Made Me Do")
    song_g = TreeNode("Gorgeous")

    singer.left, singer.right = genre_country, genre_pop
    genre_country.left, genre_country.right = album_fearless, album_red
    genre_pop.left, genre_pop.right = album_1989, album_reputation
    album_fearless.left, album_fearless.right = song_ls, song_wh
    album_red.left, album_red.right = song_wanegbt, song_ikywt
    album_1989.left, album_1989.right = song_sio, song_bb
    album_reputation.left, album_reputation.right = song_lwymmd, song_g

    print(list(pre_order(singer)))
    print(list(in_order(singer)))
    print(list(post_order(singer)))
