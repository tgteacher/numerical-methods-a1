from a1 import *
from test_utils import *
from numpy import array

def test_tridiag_solver():
    check_linalg()
    solution = array([2.89871795, 2.59487179, 2.48076923, 2.32820513, 1.83205128])
    epsilon = 10E-7
    assert(sum(abs(tridiag_solver_n(5) - solution))<epsilon)
