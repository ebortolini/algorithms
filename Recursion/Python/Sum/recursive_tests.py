from recursive_sum import recursive_sum

def test_sum():
    assert recursive_sum([1,2]) == sum([1,2])
    assert recursive_sum(None) == 0
    assert recursive_sum([]) == 0
    assert recursive_sum([5]) == sum([5])
    assert recursive_sum([1,8,3,20]) == sum([1,8,3,20])
    assert recursive_sum([10,2,3,55]) == sum([10,2,3,55])