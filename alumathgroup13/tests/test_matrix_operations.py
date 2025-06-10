import pytest
from alumathgroup13 import matrix_multiply, validate_matrices

def test_basic_matrix_multiplication():
    """Test basic 2x2 matrix multiplication"""
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    result = matrix_multiply(A, B)
    assert result == expected

def test_different_dimensions():
    """Test multiplication with different dimensions"""
    A = [[1, 2, 3]]  # 1x3
    B = [[4], [5], [6]]  # 3x1
    expected = [[32]]  # 1x1
    result = matrix_multiply(A, B)
    assert result == expected

def test_rectangular_matrices():
    """Test multiplication of rectangular matrices"""
    A = [[1, 2], [3, 4], [5, 6]]  # 3x2
    B = [[7, 8, 9], [10, 11, 12]]  # 2x3
    expected = [[27, 30, 33], [61, 68, 75], [95, 106, 117]]  # 3x3
    result = matrix_multiply(A, B)
    assert result == expected

def test_invalid_dimensions():
    """Test that invalid dimensions raise ValueError"""
    A = [[1, 2]]  # 1x2
    B = [[3], [4], [5]]  # 3x1
    with pytest.raises(ValueError):
        matrix_multiply(A, B)

def test_empty_matrices():
    """Test that empty matrices raise ValueError"""
    A = []
    B = [[1, 2]]
    with pytest.raises(ValueError):
        matrix_multiply(A, B)