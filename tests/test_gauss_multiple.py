from numpy import *
from a1 import *
from test_utils import *

def test_gauss_multiple():
    check_linalg()
    a = array([[6, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    b = array([[-14, 22], [36, -18], [6, 7]], dtype=float_)
    solution = gauss_multiple(a, b) # result is now in b or solution
    na = array([[6, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    nb = array([[-14, 22], [36, -18], [6, 7]], dtype=float_)
    from numpy.linalg import solve
    nsolution = solve(na, nb)
    epsilon = 10E-15
    assert(((not (solution is None)) and sum(abs(nsolution - solution)) < epsilon) or (sum(abs(nsolution - b)) < epsilon))

def test_gauss_multiple_pivot():
    check_linalg()
    a = array([[0, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    b = array([[-14, 22], [36, -18], [6, 7]], dtype=float_)
    solution = gauss_multiple_pivot(a, b) # result is now in b or solution
    na = array([[0, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    nb = array([[-14, 22], [36, -18], [6, 7]], dtype=float_)
    from numpy.linalg import solve
    nsolution = solve(na, nb)
    epsilon = 10E-15
    assert(((not (solution is None)) and sum(abs(nsolution - solution)) < epsilon) or (sum(abs(nsolution - b)) < epsilon))
