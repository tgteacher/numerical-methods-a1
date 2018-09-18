from numpy import *
from a1 import *

def test_square():
    a = array([[1, 2, 3], [1, 2, 3]])
    assert(not square(a))
    a = array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    assert(square(a))
