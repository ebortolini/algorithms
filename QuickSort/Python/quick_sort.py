'''
Based on: https://algs4.cs.princeton.edu/23quicksort/Quick.java.html
'''
from typing import List, TypeVar
import random

Item = TypeVar("Item", int, str)

class QuickSort():
    @staticmethod
    def sort(items: List[Item]):
        random.shuffle(items)
        QuickSort._sort(items, 0, len(items) -1)

    @staticmethod
    def _partition(items: List[Item], lo:int, hi:int) -> int:
        i = lo
        j = hi + 1
        v = items[lo]

        while True:
            i+=1
            while items[i] < v:
                if i == hi: break
                i += 1
        
            j-=1
            while v < items[j]:
                if j == lo: break
                j -=1
                
            
            if i >= j: break

            items[i], items[j] = items[j], items[i]

        items[lo], items[j] = items[j], items[lo]
        return j

    @staticmethod
    def _sort(items: List[Item], lo:int, hi:int):
        if hi<=lo: return
        j = QuickSort._partition(items, lo, hi)
        QuickSort._sort(items, lo, j - 1)
        QuickSort._sort(items, j + 1, hi)
