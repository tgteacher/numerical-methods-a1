from numpy import *


'''
   PART 1: Warm-up
'''


def example_func():
    '''
      Important: READ THIS CAREFULLY. 
      Task: This function is an example, you don't have to modify it.
      Example: Nothing to report here, really.
      Test: This function is is tested in tests/test_example.py
            This test just gives you a bonus, yay!
      Hint: The functions below have to be implemented in Python, without
            using any function from numpy's linear algebra module. In each function, a
            docstring formatted as the present one explains what the 
            function must do (Task), gives an example of output 
            (Example), explains how it will be evaluated (Test), and 
            may give you some hints (Hint).
    '''
    return 'It works!'


def square(a):
    '''
      Task: This function tests if a matrix is square. It returns True 
            if a represents a square matrix.
      Parameters: a is a numpy array.
      Example: square(array([[1, 2], [3, 4]])) must return True.
      Test: This function is is tested in tests/test_square.py
      Hint: Use numpy's shape function.
    '''

    ## YOUR CODE GOES HERE
    raise Exception("Function not implemented")


'''
  Part 2: Resolution of linear systems for polynomial interpolation
'''


def fit_poly_2(points):
    '''
      Task: This function finds a polynomial P of degree 2 that passes 
            through the 3 points contained in list 'points'. It returns a numpy
            array containing the coefficient of a polynomial P: array([a0, a1, a2]),
            where P(x) = a0 + a1*x + a2*x**2. Every (x, y) in 'points' must 
            verify y = a0 + a1*x + a2*x**2.
      Parameters: points is a Python list of 3 pairs representing 2D points.
      Example: fit_poly_2([(0, -1), (1, -2), (2, -9)]) must return array([-1, 2, 3])
      Test: This function is is tested by function test_fit_poly_2 in tests/test_fit_poly.py
      Hint: This should be done by solving a linear system.
    '''

    ## YOUR CODE GOES HERE
    raise Exception("Function not implemented")


def fit_poly(points):
    '''
      Task: This function is a generalization of the previous one. It 
            finds a polynomial P of degree n that passes 
            through the n+1 points contained in list 'points'. It 
            returns a numpy array containing the coefficient of a 
            polynomial P: array([a0, a1, ..., an]), where P(x) = a0 + 
            a1*x + a2*x**2 + ... + an*x**n. Every (x, y) in 'points' 
            must verify y = P(x).
      Parameters: points is a Python list of pairs representing 2D points.
      Examples: fit_poly([(0, -1), (1, -2), (2, -9)]) must return 
                array([-1, 2, 3]) (as in the previous function) fit_poly([(0, 2), 
                (1, 6), (2, 24), (3, 62)]) must return array([2, -1, 4, 1])
      Test: This function is is tested by the following functions in tests/test_fit_poly.py:
            - test_fit_poly tests a basic fit
            - test_fit_poly_raises tests that the function raises an 
              AssertionError when the polynomial cannot be fit (for 
              instance, 3 points are aligned).
            - test_fit_poly_n tests the fit on a random polynomial of degre <= 6.
      Hint: This should be done by solving a linear system.
    '''

    ## YOUR CODE GOES HERE
    raise Exception("Function not implemented")


'''
  Part 3: Tridiagonal systems
'''

def tridiag_solver_n(n):
    '''
      Task: This function returns the solution of the following tridiagonal equations:
            4x[1] - x[2] = 9
            -x[i-1] + 4x[i] - x[i+1] = 5, i=2,....n-1
            -x[n-1] + 4x[n] = 5
            The system of equations is the same
            as in problem 2.2.9 in the Textbook, except that here n is a 
            parameter of the function. All correct answers will be accepted,
            but you are strongly encouraged to exploit the tridiagonal nature
            of the system.
      Parameters: n is an integer representing the dimension of the system.
      Examples: tridiag_solver_n(2) must return array([41/15, 29/15])
      Test: This function is is tested by the function in tests/test_tridiag_solver.py.
    '''

    ## YOUR CODE GOES HERE
    raise Exception("Function not implemented")


'''
  Part 4: Gauss Elimination for more than 1 equation
'''

def gauss_multiple(a, b):
    '''
      Task: This function returns the solution of the system written as
            AX=B, where A is an n x n square matrix, and X and B are n x m matrices.
            It is equivalent to solving m systems of the form Ax=b, where
            x and b are column vectors. You have to extend the implementation
            of Gauss elimination presented in the course to work with m constant
            vectors instead of only 1. This is problem 2.1.14 in the textbook.
            It is up to you to decide if your function will modify a and b (the
            tests should work in both cases).
      Parameters: a is a numpy array representing a square matrix. b is a numpy
            array representing a matrix with as many lines as in a.
      Test: This function is is tested by the function test_gauss_multiple in tests/test_gauss_multiple.py.
      Hint: Start from the implementation shown in the course!
    '''

    ## YOUR CODE GOES HERE
    raise Exception("Function not implemented")


def gauss_multiple_pivot(a, b):
    '''
      Task: This function returns the same result as the previous one,
            except that it uses scaled row pivoting.
      Parameters: a is a numpy array representing a square matrix. b is a numpy
            array representing a matrix with as many lines as in a.
      Test: This function is is tested by the function 
            test_gauss_multiple_pivot in tests/test_gauss_multiple.py.
    '''

    ## YOUR CODE GOES HERE
    raise Exception("Function not implemented")


def matrix_invert(a):
    '''
      Task: This function returns the inverse of the square matrix a passed 
            as a paramter. 
      Parameters: a is a numpy array representing a non-singular square matrix.
      Test: This function is is tested by function test_inverse in tests/test_inverse.py
      Hint: Remember that the inverse of A is the solution of n linear systems of n 
            equations.
    '''

    ## YOUR CODE GOES HERE
    raise Exception("Function not implemented")
