def test_filter():
    lst = [11,22,23,24,25,26,27,28,29,8,7,6,5,4,3,2,1]
    assert  list(filter( lambda x: x%2 == 0, lst ))  == [22,24,26,28,8,6,4,2]
    assert list(filter(lambda x: x > 10, lst)) == [11,22,23,24,25,26,27,28,29]

def test_map():
    lst = [1,2,3,4,5]
    lst2=[0,2,0,2,0]
    assert list(map(lambda x: x*10, lst)) == [10,20,30,40,50]
    assert list( map( lambda x,y: x*y,lst,lst2)  ) == [0,4,0,8,0]

def test_sorted():
    lst = [1,3,2,4,7,5,8,6,9]
    assert sorted( lst ) == [1,2,3,4,5,6,7,8,9]
    assert sorted(lst,reverse=True) == [9,8,7,6,5,4,3,2,1]
    assert sorted(lst, key=lambda x: x*(-1) ) == [9, 8, 7, 6, 5, 4, 3, 2, 1]

import math
def test_pi():
    assert str(math.pi)[:9] == '3.1415926'

def test_sqrt():
    assert math.sqrt(9)  == 3

def test_pow():
    assert math.pow(2,3) == 8

def test_hypot():
    assert int(math.hypot(  5,1 )) == 5