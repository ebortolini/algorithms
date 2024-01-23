'''
Based on: https://algs4.cs.princeton.edu/21elementary/Shell.java.html
'''
from typing import List, TypeVar, Callable

Item = TypeVar("Item")

class ShellSort:
    def sort(self, items:List[Item], compare:Callable[[Item, Item], int]) -> None:
        n = len(items)
        h = 1
        while h < n//3:
            h = 3*h+1
        
        while h >= 1:
            for i in range(h, n):
                for j in range(i, h-1, -h):
                    if self._less(items[j], items[j-h], compare):
                        self._swap(items, j, j-h)
            h = h//3

    def _less(self, a: Item, b: Item, compare:Callable[[Item, Item], int]) -> bool:
        return False if compare(a, b) >=0 else True
    
    def _swap(self, items:List[Item], i:int, j:int):
        items[i], items[j] = items[j], items[i]