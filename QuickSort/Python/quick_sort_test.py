from typing import List, Type
from quick_sort import QuickSort

def test_should_order_unordered_array_of_len_3():
    unordered_array : List[int] = [1,2,0]
    expected_array : List[int] = [0,1,2]

    QuickSort.sort(unordered_array)

    assert unordered_array == expected_array

def test_should_order_unordered_array_of_len_10():
    unordered_array : List[int] = [100,0,1893,70,2,985232,-1,35,101,-9058]
    expected_array : List[int] = [-9058, -1, 0, 2, 35, 70, 100, 101, 1893, 985232]

    QuickSort.sort(unordered_array)

    assert unordered_array == expected_array

def test_should_not_change_ordered_array():
    ordered_array : List[int] = [-9058, -1, 0, 2, 35, 70, 100, 101, 1893, 985232]
    expected_array : List[int] = [-9058, -1, 0, 2, 35, 70, 100, 101, 1893, 985232]

    QuickSort.sort(ordered_array)

    assert ordered_array == expected_array

def test_should_work_for_1_element_array():
    ordered_array : List[int] = [1]
    expected_array : List[int] = [1]

    QuickSort.sort(ordered_array)

    assert ordered_array == expected_array

def test_should_work_for_empty_array():
    ordered_array : List[int] = []
    expected_array : List[int] = []

    QuickSort.sort(ordered_array)

    assert ordered_array == expected_array

def test_should_work_for_strings():
    ordered_array : List[str] = ['A', 'G', 'B'] #["B", "G", "A"]
    expected_array : List[str] = ["A", "B", "G"]

    QuickSort.sort(ordered_array)

    assert ordered_array == expected_array

def test_should_sort_reversed_array():
    ordered_array : List[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    QuickSort.sort(ordered_array)

    assert ordered_array == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
