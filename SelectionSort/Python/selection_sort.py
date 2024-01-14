#Based on: https://algs4.cs.princeton.edu/21elementary/Selection.java.html

from typing import List, TypeVar, Callable

Item = TypeVar("Item")

class SelectionSort:
    def sort(self, items:List[Item], compare:Callable[[Item, Item], int]) -> None:
        n = len(items)
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if (self._less(items[j], items[min], compare)):
                    min = j
            self._swap(items, i, min)

    def _less(self, a: Item, b: Item, compare:Callable[[Item, Item], int]) -> bool:
        return False if compare(a, b) >=0 else True

    def _swap(self, items:List[Item], i:int, j:int):
        items[i], items[j] = items[j], items[i]