class Digraph(object):
    """有向图，二维数组，每一行数组，代表a[i]中指向的元素"""

    def __init__(self, vertex_num):
        self.v_num = vertex_num
        self.adj_tbl = []
        for i in range(self.v_num + 1):
            self.adj_tbl.append([])

    def add_edge(self, frm_index, to_index):
        if frm_index > self.v_num or to_index > self.v_num:
            return False
        self.adj_tbl[frm_index].append(to_index)

    def __len__(self):
        return self.v_num

    def __getitem__(self, index):
        if index > self.v_num:
            raise IndexError(" No Such Vertex")
        return self.adj_tbl[index]

    def __repr__(self):
        return str(self.adj_tbl)

    def __str__(self):
        return str(self.adj_tbl)


class UndigGraph:
    """无向图，二维数组，a[i]数组中存储的是有边关系的元素"""

    def __init__(self, vertex_num):
        self.v_num = vertex_num
        self.adj_tbl = []
        for i in range(self.v_num + 1):
            self.adj_tbl.append([])

    def add_edge(self, frm_index, to_index):
        if frm_index > self.v_num or to_index > self.v_num:
            return
        self.adj_tbl[frm_index].append(to_index)
        self.adj_tbl[to_index].append(frm_index)

    def __len__(self):
        return self.v_num

    def __getitem__(self, index):
        if index > self.v_num:
            raise IndexError(" No Such Vertex")
        return self.adj_tbl[index]

    def __repr__(self):
        return str(self.adj_tbl)

    def __str__(self):
        return str(self.adj_tbl)


if __name__ == '__main__':
    dg = Digraph(10)
    print(dg)
    dg.add_edge(1, 9)
    dg.add_edge(1, 3)
    dg.add_edge(3, 4)
    dg.add_edge(4, 3)
    print(dg)

    ug = UndigGraph(10)
    print(ug)
    ug.add_edge(1, 9)
    ug.add_edge(1, 3)
    ug.add_edge(3, 4)
    ug.add_edge(4, 3)
    print(ug)
