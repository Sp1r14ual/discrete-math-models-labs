import pytest
import copy
from main import solve

def run_test(N, M, A, B, expected):
    A_copy = copy.deepcopy(A)
    B_copy = copy.deepcopy(B)
    
    result = solve(N, M, A_copy, B_copy)
    assert result.strip() == expected.strip()

def test_1():
    # 2x + 3y = 5 (1 free variable)
    run_test(1, 2, [[2, 3]], [5], "1\n3 -5\n-2 5")

def test_2():
    # Plane intersection: x + y + z = 1, 2x + 3y + 4z = 2
    run_test(2, 3, [[1, 1, 1], [2, 3, 4]], [1, 2], "1\n1 1\n-2 0\n1 0")

def test_3():
    # Parallel lines - No solution: x + y = 1, 2x + 2y = 3
    run_test(2, 2, [[1, 1], [2, 2]], [1, 3], "NO SOLUTIONS")

def test_4():
    # Dependent equations: x + y = 2, 2x + 2y = 4
    run_test(2, 2, [[1, 1], [2, 2]], [2, 4], "1\n-1 2\n1 0")

def test_5():
    # No integer solutions: 2x + 4y = 3
    run_test(1, 2, [[2, 4]], [3], "NO SOLUTIONS")

def test_6():
    # 6x + 15y = 9
    run_test(1, 2, [[6, 15]], [9], "1\n5 -6\n-2 3")

def test_7():
    # Unique solution: x = 5, y = 7
    run_test(2, 2, [[1, 0], [0, 1]], [5, 7], "0\n5\n7")
