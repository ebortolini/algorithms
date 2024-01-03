from stack import Stack

def test_should_return_empty():
    stack = Stack[int]()
    assert True == stack.isEmpty()

def test_should_return_last_element_added():
    stack = Stack[int]()
    stack.push(5)
    stack.push(10)
    stack.push(1)

    assert False == stack.isEmpty()
    assert 1 == stack.pop()
    assert False == stack.isEmpty()
    assert 10 == stack.pop()
    assert False == stack.isEmpty()
    assert 5 == stack.pop()
    assert True == stack.isEmpty()