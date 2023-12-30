#Based on book/lectures from: https://algs4.cs.princeton.edu/home/

class QuickUnionUF:
    def __init__(self, size:int) -> None:
        self.ids = []
        for n in range(size):
            self.ids.append(n)
    
    def _get_root(self, id:int) -> int:
        while id != self.ids[id]:
            id = self.ids[id]
        return id
    
    def connected(self, p:int, q:int) -> bool:
        return self._get_root(p) == self._get_root(q)
    
    def union(self, p:int, q:int) -> None:
        id_p = self._get_root(p)
        id_q = self._get_root(q)
        self.ids[id_p] = id_q

#reference: https://algs4.cs.princeton.edu/15uf/WeightedQuickUnionPathCompressionUF.java.html
class WeightedQuickUnionPathCompressionUF:
    def __init__(self, size:int) -> None:
        self.parent = []
        self.size = []
        for n in range(size):
            self.parent.append(n)
            self.size.append(1)
    
    def _get_root(self, p:int) -> int:
        while self.parent[p] != p:
            p = self.parent[p]
        return p
    
    def _compress_path(self, p:int, root:int) -> None:
        while p != root:
            new_p = self.parent[p]
            self.parent[p] = root
            p = new_p
    
    def connected(self, p:int, q:int) -> bool:
        return self._get_root(p) == self._get_root(q)
    

    def union(self, p:int, q:int) -> None:
        root_p = self._get_root(p)
        self._compress_path(p, root_p)
        root_q = self._get_root(q)
        self._compress_path(q, root_q)

        if root_p == root_q:
            return
        
        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_p]+= self.size[root_q]
        else:
            self.parent[root_q] = root_p
            self.size[root_q]+= self.size[root_p]