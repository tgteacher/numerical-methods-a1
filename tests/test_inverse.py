from a1 import *
from numpy import *
from test_utils import *

def test_inverse():
    check_linalg()
    a = array([[6, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    inva = matrix_invert(a)
    from numpy.linalg import inv
    a = array([[6, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    solution = inv(a)
    epsilon = 10E-3
    assert(abs(inva - solution).max()<epsilon)
