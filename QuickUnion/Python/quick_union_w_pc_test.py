from quick_union import WeightedQuickUnionPathCompressionUF

def test_5_and_2_should_not_be_connected():
    qu = WeightedQuickUnionPathCompressionUF(10)
    assert False == qu.connected(5,2)

def test_5_and_2_should_be_connected():
    qu = WeightedQuickUnionPathCompressionUF(10)
    qu.union(5,2)
    assert True == qu.connected(5,2)

def test_multiple_connections():
    qu = WeightedQuickUnionPathCompressionUF(10)
    qu.union(4,3)
    assert True == qu.connected(4,3)

    qu.union(3,8)
    assert True == qu.connected(3,8)
    assert True == qu.connected(4,8)

    qu.union(5,6)
    assert True == qu.connected(5, 6)

    qu.union(9,4)
    assert True == qu.connected(9, 4)
    assert True == qu.connected(9, 3)
    assert True == qu.connected(9, 8)

    qu.union(2,1)
    assert True == qu.connected(2, 1)
    assert True == qu.connected(1, 2)

    assert False == qu.connected(4,5)

    qu.union(5,0)
    assert True == qu.connected(5, 0)
    assert True == qu.connected(0, 0)

    qu.union(7,2)
    assert True == qu.connected(2, 7)

    qu.union(6,1)
    assert True == qu.connected(6, 1)
    assert False == qu.connected(8,1)