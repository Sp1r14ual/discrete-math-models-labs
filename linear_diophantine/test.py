import pytest
import copy
from main import solve

def run_test(N, M, A, B, expected):
    A_copy = copy.deepcopy(A)
    B_copy = copy.deepcopy(B)
    
    result = solve(N, M, A_copy, B_copy)
    assert result.strip() == expected.strip()

# Tests from manual (equations)
def test_eq_1():
    # x = 1 => x - 1 = 0
    run_test(1, 1, [[1]], [-1], "0\n1")

def test_eq_2():
    # x + y = 1 => x + y - 1 = 0
    run_test(1, 2, [[1, 1]], [-1], "1\n-1 1\n1 0")

def test_eq_3():
    # 3x = 5 => 3x - 5 = 0
    run_test(1, 1, [[3]], [-5], "NO SOLUTIONS")

def test_eq_4():
    # 2x + 3y = 5 => 2x + 3y - 5 = 0
    run_test(1, 2, [[2, 3]], [-5], "1\n3 -5\n-2 5")

def test_eq_5():
    # 2x + 2y = 5 => 2x + 2y - 5 = 0
    run_test(1, 2, [[2, 2]], [-5], "NO SOLUTIONS")

def test_eq_6():
    # 4x + 8y = 16 => 4x + 8y - 16 = 0
    run_test(1, 2, [[4, 8]], [-16], "1\n-2 4\n1 0")

# Tests from manual (systems)
def test_sys_1():
    # x=1, y=2, z=3 => x-1=0, y-2=0, z-3=0
    run_test(3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]], [-1, -2, -3], "0\n1\n2\n3")

def test_sys_2():
    # x+z=1, y=2, x+z=3
    run_test(3, 3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]], [-1, -2, -3], "NO SOLUTIONS")

def test_sys_3():
    # x+z=1, y=2, 2x+2z=2
    run_test(3, 3, [[1, 0, 1], [0, 1, 0], [2, 0, 2]], [-1, -2, -2], "1\n-1 1\n0 2\n1 0")

def test_sys_4():
    # x+z=1, y=2
    run_test(2, 3, [[1, 0, 1], [0, 1, 0]], [-1, -2], "1\n-1 1\n0 2\n1 0")

def test_sys_5():
    # x+z=1, y-z=2
    run_test(2, 3, [[1, 0, 1], [0, 1, -1]], [-1, -2], "1\n-1 1\n1 2\n1 0")

def test_sys_6():
    # x+y+z=1, 2x+2y+2z=4
    run_test(2, 3, [[1, 1, 1], [2, 2, 2]], [-1, -4], "NO SOLUTIONS")
