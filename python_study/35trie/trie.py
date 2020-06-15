"""
 trie树
"""


class TrieNode:
    def __init__(self, data: str):
        self._data = data
        self._children = [None] * 26
        self._is_ending_char = False


class Trie:
    def __init__(self):
        self._root = TrieNode("/")

    def insert(self, text: str):
        node = self._root
        for index, char in map(lambda x: (ord(x) - ord("a"), x), text):
            # print(index, char)
            if not node._children[index]:
                node._children[index] = TrieNode(text)
            node = node._children[index]
        node._is_ending_char = True

    def find(self, pattern: str):
        node = self._root
        for index in map(lambda x: ord(x) - ord("a"), pattern):
            # print(index)
            if not node._children[index]: return False
            node = node._children[index]
        return node._is_ending_char


if __name__ == '__main__':

    strs = ["how", "hi", "her", "hello", "so", "see"]
    trie = Trie()
    for s in strs:
        trie.insert(s)

    for s in strs:
        print(trie.find(s))
