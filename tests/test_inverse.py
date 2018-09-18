from a1 import *
from numpy import *

def test_inverse():
    a = array([[6, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    inva = matrix_invert(a)
    from numpy.linalg import inv
    solution = inv(a)
    epsilon = 10E-3
    assert(sum(abs(inva - solution))<epsilon)
