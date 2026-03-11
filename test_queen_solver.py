import pytest
from src.queen_solver import solve_n_queens


def test_n_1():
    """测试n=1时的解"""
    solutions = solve_n_queens(1)
    assert solutions == [["Q"]]


def test_n_4():
    """测试n=4时的解数量"""
    solutions = solve_n_queens(4)
    assert len(solutions) == 2


def test_n_8():
    """测试n=8时的解数量"""
    solutions = solve_n_queens(8)
    assert len(solutions) == 92


def test_n_0():
    """测试n=0时的异常"""
    with pytest.raises(ValueError, match="n必须大于等于1"):
        solve_n_queens(0)