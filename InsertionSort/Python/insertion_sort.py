'''
Based on:
    https://algs4.cs.princeton.edu/21elementary/Insertion.java.html
    https://algs4.cs.princeton.edu/21elementary/InsertionX.java.html
'''
from typing import List, TypeVar, Callable
from abc import ABC, abstractmethod

Item = TypeVar("Item")

class InsertionSortBase(ABC):
    @abstractmethod
    def sort(self, items:List[Item], compare:Callable[[Item, Item], int]) -> None:
        pass

    def _less(self, a: Item, b: Item, compare:Callable[[Item, Item], int]) -> bool:
        return False if compare(a, b) >=0 else True
    
    def _swap(self, items:List[Item], i:int, j:int):
        items[i], items[j] = items[j], items[i]

class InsertionSort(InsertionSortBase):
    def sort(self, items:List[Item], compare:Callable[[Item, Item], int]) -> None:
        n = len(items)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if self._less(items[j], items[j-1], compare):
                    self._swap(items, j, j-1)
    
class InsertionSortWithSentinel(InsertionSortBase):
    def sort(self, items: List[Item], compare: Callable[[Item, Item], int]) -> None:
        exchanged = False
        n = len(items)
        for i in range(n-1, 0, -1):
            if self._less(items[i], items[i-1], compare):
                self._swap(items, i, i-1)
                exchanged = True 

        if not exchanged:
           return

        for i in range(2, n):
            j = i
            v = items[i]
            while self._less(v, items[j-1], compare):
                items[j] = items[j-1]
                j = j -1
            items[j] = v