#Based on book/lectures from: https://algs4.cs.princeton.edu/home/

class QuickFindUF:
    def __init__(self, size:int) -> None:
        self.ids = []
        for n in range(size):
            self.ids.append(n)

    def connected(self, p:int, q:int) -> bool:
        return self.ids[p] == self.ids[q]
    
    def union(self, p:int, q:int) -> None:
        p_id = self.ids[p]
        q_id = self.ids[q]
        for i in range(len(self.ids)):
            if self.ids[i] == p_id:
                self.ids[i] = q_id


