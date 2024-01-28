'''
Based on:
    https://algs4.cs.princeton.edu/22mergesort/Merge.java.html
'''

from typing import Callable, Generic, List, TypeVar, cast


T = TypeVar("T")

class MergeSort(Generic[T]):
    def __init__(self, compare:Callable[[T, T], int]) -> None:
        super().__init__()
        self.compare = compare

    def _less(self, a: T, b: T) -> bool:
        return False if self.compare(a, b) >=0 else True
    
    def _merge(self, a: List[T], aux:List[T], low:int, mid:int, high:int):
        for k in range(low, high+1):
            aux[k] = a[k]

        i = low
        j = mid+1

        for k in range(low, high+1):
            if i > mid:
                a[k] = aux[j] #we already passed all elements from the left side, so just get the righ until is finished
                j = j+1
            elif j > high:
                a[k] = aux[i] #Same as the previous but in the righ side
                i = i + 1
            elif self._less(aux[j], aux[i]):
                a[k] = aux[j]
                j= j+1
            else:
                a[k] = aux[i]
                i = i+1

    def _sort(self, a: List[T], aux:List[T], low:int, high:int):
        if high <= low:
            return
        mid = low + (high - low) // 2
        self._sort(a, aux, low, mid)
        self._sort(a, aux, mid +1, high)
        self._merge(a, aux, low, mid, high)

    def sort(self, a: List[T]):
        aux: List = [None] * len(a)
        self._sort(a, aux, 0, len(a)-1)