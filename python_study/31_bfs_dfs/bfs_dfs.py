"""广度优先和深度优先搜索"""

from typing import List, Optional, Generator, IO
from collections import deque


class Graph:
    """无向图"""

    def __init__(self, num_vertices):
        self.v_num = num_vertices
        self.adj_tbl = []
        for i in range(self.v_num + 1):
            self.adj_tbl.append([])

    def add_edge(self, from_index, to_index):
        if from_index > self.v_num or to_index > self.v_num:
            return False
        self.adj_tbl[from_index].append(to_index)
        self.adj_tbl[to_index].append(from_index)

    def __repr__(self):
        return str(self.adj_tbl)

    def _generate_path(self, s: int, t: int, prev: List[Optional[int]]):
        # prev 的形式prev: [None, 0, 1, 0, 1, 2, 4, 5]，从最后一个5开始推，5 <--pre[5]=2 <--pre[2]=1 <--pre[1]=0,
        # 利用下标index，记录了查找的路径
        if prev[t] or s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s: int, t: int):
        """ 广度优先搜索,类似于二叉树的层次遍历，利用queue的先进先出特性来实现"""
        if s == t: return

        visited = [False] * self.v_num
        visited[s] = True
        q = deque()
        q.append(s)
        prev = [None] * self.v_num

        while q:
            v = q.popleft()
            for neighbour in self.adj_tbl[v]:
                # 必须是没有被访问过的
                if not visited[neighbour]:
                    # v 是neighbor的上一层节点
                    prev[neighbour] = v
                    # 找到了最后一层
                    if neighbour == t:
                        print("find it path:", "->".join(self._generate_path(s, t, prev)))
                        # return
                    visited[neighbour] = True
                    q.append(neighbour)
            print("v:", v, "path:", "->".join(self._generate_path(s, v, prev)))
        print("visited:", visited)
        print("prev:", prev)

    def dfs(self, s: int, t: int):
        """深度优先搜索"""
        found = False
        visited = [False] * self.v_num
        prev = [None] * self.v_num

        def _dfs(from_vertex: int):
            nonlocal found
            if found: return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbour in self.adj_tbl[from_vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)

        _dfs(s)
        print("find it path:", "->".join(self._generate_path(s, t, prev)))
        print("visited:", visited)
        print("prev:", prev)


if __name__ == '__main__':
    graph = Graph(8)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    print(graph)
    # graph.bfs(0, 7)

    graph.dfs(0,7)