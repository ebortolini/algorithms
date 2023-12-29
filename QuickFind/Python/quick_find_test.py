from quick_find import QuickFindUF

def test_5_and_2_should_not_be_connected():
    qf = QuickFindUF(10)
    assert False == qf.connected(5, 2)

def test_5_and_2_should_be_connected():
    qf = QuickFindUF(10)
    qf.union(5,2)
    assert True == qf.connected(5, 2)

def test_change_connections():
    qf = QuickFindUF(10)
    assert False == qf.connected(5, 2)
    
    qf.union(5,2)
    assert True == qf.connected(5, 2)
    
    qf.union(0, 9)
    assert True == qf.connected(0, 9)
    assert True == qf.connected(9, 0)

    qf.union(2,9)
    assert True == qf.connected(2, 9)
    assert True == qf.connected(5, 2)
    assert True == qf.connected(0, 2)
    assert True == qf.connected(0, 5)
    assert True == qf.connected(9, 5)
