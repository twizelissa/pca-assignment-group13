# AlumathGroup13 - Advanced Linear Algebra Matrix Operations

[![PyPI version](https://badge.fury.io/py/alumathgroup13.svg)](https://badge.fury.io/py/alumathgroup13)
[![Python versions](https://img.shields.io/pypi/pyversions/alumathgroup13.svg)](https://pypi.org/project/alumathgroup13/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A pure Python library for advanced linear algebra operations, specifically designed for matrix multiplication with support for different matrix dimensions. **No external libraries required** - uses only Python built-in functions.

## 🚀 Features

- **Matrix Multiplication**: Efficient multiplication of matrices with different dimensions
- **Pure Python**: No external dependencies - uses only Python built-in functions
- **Input Validation**: Comprehensive validation to ensure matrices can be multiplied
- **Error Handling**: Clear error messages for invalid operations
- **Lightweight**: Zero external dependencies
- **Educational**: Perfect for learning matrix operations without library abstractions

## 📦 Installation

### From PyPI (Recommended)
```bash
pip install group13-matrix-operations-2025==1.0.0
```

### From Source
```bash
git clone https://github.com/yourusername/alumathgroup13.git
cd alumathgroup13
pip install -e .
```

## 🎯 Quick Start

```python
from alumathgroup13 import matrix_multiply

# Basic matrix multiplication
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply(A, B)
print(result)  # Output: [[19, 22], [43, 50]]
```

## 📚 Usage Examples

### Example 1: Basic 2x2 Matrix Multiplication
```python
from alumathgroup13 import matrix_multiply

A = [[1, 2], 
     [3, 4]]
B = [[5, 6], 
     [7, 8]]

result = matrix_multiply(A, B)
print("A × B =", result)
# Output: A × B = [[19, 22], [43, 50]]
```

### Example 2: Different Dimensions (1×3 × 3×1)
```python
from alumathgroup13 import matrix_multiply

# 1x3 matrix multiplied by 3x1 matrix
A = [[1, 2, 3]]
B = [[4], 
     [5], 
     [6]]

result = matrix_multiply(A, B)
print("A × B =", result)
# Output: A × B = [[32]]
```

### Example 3: Rectangular Matrices (3×2 × 2×3)
```python
from alumathgroup13 import matrix_multiply

# 3x2 matrix multiplied by 2x3 matrix
A = [[1, 2], 
     [3, 4], 
     [5, 6]]
B = [[7, 8, 9], 
     [10, 11, 12]]

result = matrix_multiply(A, B)
print("A × B =", result)
# Output: A × B = [[27, 30, 33], [61, 68, 75], [95, 106, 117]]
```

### Example 4: Large Matrix Multiplication
```python
from alumathgroup13 import matrix_multiply

# Create larger matrices using pure Python
rows_A, cols_A = 100, 50
rows_B, cols_B = 50, 75

# Generate random matrices using pure Python
import random
A = [[random.randint(1, 10) for _ in range(cols_A)] for _ in range(rows_A)]
B = [[random.randint(1, 10) for _ in range(cols_B)] for _ in range(rows_B)]

result = matrix_multiply(A, B)
print(f"Multiplied {rows_A}×{cols_A} with {rows_B}×{cols_B} matrix")
print(f"Result shape: {len(result)}×{len(result[0])}")
```

### Example 5: Matrix Multiplication with Validation
```python
from alumathgroup13 import matrix_multiply, validate_matrices

# Example with validation
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

try:
    # Validate first
    rows_A, cols_A, rows_B, cols_B = validate_matrices(A, B)
    print(f"Matrix A: {rows_A}×{cols_A}")
    print(f"Matrix B: {rows_B}×{cols_B}")
    
    # Perform multiplication
    result = matrix_multiply(A, B)
    print(f"Result: {len(result)}×{len(result[0])} matrix")
    print("Result:", result)
    
except ValueError as e:
    print(f"Error: {e}")
```

## 🔧 API Reference

### `matrix_multiply(A, B)`

Multiply two matrices using standard matrix multiplication algorithm implemented in pure Python.

**Parameters:**
- `A` (list of lists): First matrix (m×n)
- `B` (list of lists): Second matrix (n×p)

**Returns:**
- `list`: Resulting matrix (m×p) as list of lists

**Raises:**
- `ValueError`: If matrices cannot be multiplied (incompatible dimensions)
- `ValueError`: If input is not a list of lists

**Algorithm Complexity:** O(m × n × p) where A is m×n and B is n×p

### `validate_matrices(A, B)`

Validate that matrices can be multiplied and return their dimensions.

**Parameters:**
- `A` (list of lists): First matrix
- `B` (list of lists): Second matrix

**Returns:**
- `tuple`: (rows_A, cols_A, rows_B, cols_B)

**Raises:**
- `ValueError`: If matrices are invalid or incompatible

### `matrix_info(matrix)`

Get information about a matrix.

**Parameters:**
- `matrix` (list of lists): Input matrix

**Returns:**
- `dict`: Matrix information including dimensions and properties

## ⚠️ Important Notes

### Input Requirements
- **Only list of lists accepted**: `[[1, 2], [3, 4]]` ✅
- **No NumPy arrays**: This library uses pure Python only
- **No external dependencies**: Works with Python standard library only

### Valid Input Examples
```python
# ✅ Valid inputs
A = [[1, 2], [3, 4]]
B = [[5, 6, 7], [8, 9, 10]]
C = [[1]]  # Single element matrix

# ❌ Invalid inputs (will raise ValueError)
D = [1, 2, 3]  # Not a matrix (missing nested lists)
E = []  # Empty matrix
F = [[1, 2], [3]]  # Inconsistent row lengths
```

## 🧪 Testing

### Basic Test
```python
# Create test file: test_basic.py
from alumathgroup13 import matrix_multiply

def test_basic():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = matrix_multiply(A, B)
    expected = [[19, 22], [43, 50]]
    assert result == expected
    print("✅ Basic test passed")

def test_dimensions():
    A = [[1, 2, 3]]
    B = [[4], [5], [6]]
    result = matrix_multiply(A, B)
    expected = [[32]]
    assert result == expected
    print("✅ Dimension test passed")

def test_error_handling():
    try:
        matrix_multiply([[1, 2]], [[3], [4], [5]])
        assert False, "Should have raised error"
    except ValueError:
        print("✅ Error handling test passed")

if __name__ == "__main__":
    test_basic()
    test_dimensions()
    test_error_handling()
    print("🎉 All tests passed!")
```

### Run Tests
```bash
python test_basic.py
```

## 🏗️ Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/alumathgroup13.git
cd alumathgroup13
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .
```

## 📋 Requirements

- **Python 3.7+**
- **No external dependencies** - uses only Python built-in functions
- **No NumPy, SciPy, or other libraries required**

## 🎓 Educational Value

This library is perfect for:
- **Learning matrix multiplication algorithms**
- **Understanding pure Python implementations**
- **Academic assignments requiring no external libraries**
- **Teaching linear algebra concepts**

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Ensure your code uses only pure Python (no external libraries)
4. Add tests for new functionality
5. Run the test suite
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

**Group 13**
- Member 1: [GitHub Profile](https://github.com/twizelissa)
- Member 2: [GitHub Profile](https://github.com/aubert-gloire)
- Member 3: [GitHub Profile](https://github.com/Uwingabir)
- Member 3: [GitHub Profile](https://github.com/Umwanankabandi-liliane)


## 🙏 Acknowledgments

- Built as part of Advanced Linear Algebra (PCA) coursework
- Implemented using pure Python to meet assignment requirements
- Thanks to our instructors and peers for feedback

## 📞 Support

For support, email twizelissa@gmail.com or create an issue on GitHub.


---

**Built with 💻 Pure Python | No External Dependencies | Group 13**