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