from merge_sort import MergeSort
from typing import Callable
compare_func:Callable[[int, int], int] = lambda a, b: -1 if a < b else 1 if a > b else 0 


def test_should_order_unordered_array_of_len_3():
    merge_sort = MergeSort(compare=compare_func)

    unordered_array = [1,2,0]
    expected_array = [0,1,2]

    merge_sort.sort(unordered_array)

    assert unordered_array == expected_array

def test_should_order_unordered_array_of_len_10():
    merge_sort = MergeSort(compare=compare_func)

    unordered_array = [100,0,1893,70,2,985232,-1,35,101,-9058]
    expected_array = [-9058, -1, 0, 2, 35, 70, 100, 101, 1893, 985232]

    merge_sort.sort(unordered_array)

    assert unordered_array == expected_array

def test_should_not_change_ordered_array():
    merge_sort = MergeSort(compare=compare_func)

    ordered_array = [-9058, -1, 0, 2, 35, 70, 100, 101, 1893, 985232]
    expected_array = [-9058, -1, 0, 2, 35, 70, 100, 101, 1893, 985232]

    merge_sort.sort(ordered_array)

    assert ordered_array == expected_array

def test_should_work_for_1_element_array():
    merge_sort = MergeSort(compare=compare_func)

    ordered_array = [1]
    expected_array = [1]

    merge_sort.sort(ordered_array)

    assert ordered_array == expected_array

def test_should_work_for_empty_array():
    merge_sort = MergeSort(compare=compare_func)

    ordered_array = []
    expected_array = []

    merge_sort.sort(ordered_array)

    assert ordered_array == expected_array