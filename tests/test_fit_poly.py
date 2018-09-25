import pytest
from a1 import *
from numpy import *
from test_utils import *

def test_fit_poly_2():
    check_linalg()
    points = [(0, -1), (1, -2), (2, -9)]
    coeffs = fit_poly_2(points)
    solution = empty(3)
    solution[0] = -1
    solution[1] = 2
    solution[2] = -3
    assert allclose(solution, coeffs)

def test_fit_poly():
    check_linalg()
    points = [(0, 2), (1, 6), (2, 24), (3, 62)]
    coeffs = fit_poly(points)
    solution = empty(4)
    solution[0] = 2
    solution[1] = -1
    solution[2] = 4
    solution[3] = 1
    assert allclose(solution, coeffs)

def test_fit_poly_raises():
    check_linalg()
    points = [(0, -1), (1, -2), (0, -1)]
    with pytest.raises(AssertionError):
        coeffs = fit_poly_2(points)


def eval_poly(coeffs, x):
    s = 0
    for i in range(len(coeffs)):
        s += coeffs[i] * x**i
    return s

def test_fit_poly_n():
    check_linalg()
    # pick a random number between 2 and 20
    from random import randint
    n = randint(2, 6)
    # pick n+1 random coefficients between -10 and 10
    solution = empty(n+1)
    for i in range(n+1):
        solution[i] = randint(-10, 10)
    # define points
    points = []
    for i in range(n+1):
        points.append((i, eval_poly(solution, i)))
    coeffs = fit_poly(points)
    assert allclose(solution, coeffs)

