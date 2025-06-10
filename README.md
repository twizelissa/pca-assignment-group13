# PCA Assignment - Group 13

## Advanced Linear Algebra (PCA) Assignment
**Course**: Advanced Linear Algebra  
**Group**: Group 13  
**Assignment**: Principal Component Analysis Implementation + PyPI Library

---

## 📚 Assignment Parts

### **Part 1: PCA Implementation**
- ✅ Implemented PCA from scratch using pure Python
- ✅ Data standardization and covariance matrix calculation
- ✅ Eigenvalue decomposition and principal component analysis
- ✅ Dynamic component selection based on explained variance
- ✅ Performance optimization for large datasets

**Location**: `notebooks/pca_implementation.ipynb`

### **Part 2: Manual Eigenvalue Calculations**
- ✅ Hand-calculated eigenvalues and eigenvectors
- ✅ Step-by-step mathematical proofs
- ✅ Importance calculations in percentage form
- ✅ Collaborative work with distinct handwriting

**Location**: `calculations/eigenvalue_calculations.pdf`

### **Part 3: PyPI Library - Matrix Operations**
- ✅ **Published Library**: `group13-matrix-operations-2025`
- ✅ **Pure Python Implementation** (no external libraries)
- ✅ **Matrix multiplication** for different dimensions
- ✅ **Error handling** and input validation

---

## 🚀 PyPI Library: group13-matrix-operations-2025

### **Installation**
```bash
pip install group13-matrix-operations-2025
```

### **Usage**
```python
from group13_matrix_operations_2025 import matrix_multiply

# Example 1: Basic 2x2 matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply(A, B)
print(result)  # [[19, 22], [43, 50]]

# Example 2: Different dimensions
A = [[1, 2, 3]]     # 1x3
B = [[4], [5], [6]]  # 3x1
result = matrix_multiply(A, B)
print(result)  # [[32]]

# Example 3: Error handling
try:
    matrix_multiply([[1, 2]], [[3], [4], [5]])  # Incompatible dimensions
except ValueError as e:
    print(f"Error: {e}")
```

### **Features**
- ✅ **Pure Python**: No external dependencies
- ✅ **Multiple Dimensions**: Handles any compatible matrix sizes
- ✅ **Error Handling**: Clear validation and error messages
- ✅ **Educational**: Perfect for learning matrix operations

### **Library Source Code**
The complete library source code is available in: `alumathgroup13/`

---

## 🧪 Testing Your Installation

### **Quick Test for Coach**
```python
# coach_test.py
from group13_matrix_operations_2025 import matrix_multiply

print("=== Group 13 Matrix Library Test ===")

# Test basic functionality
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply(A, B)

print(f"Result: {result}")
print(f"Expected: [[19, 22], [43, 50]]")
print(f"✓ Working: {result == [[19, 22], [43, 50]]}")
```

---

## 📁 Repository Structure

```
pca-assignment-group13/
├── notebooks/
│   └── pca_implementation.ipynb          # Part 1: PCA implementation
├── calculations/
│   └── eigenvalue_calculations.pdf      # Part 2: Manual calculations
├── alumathgroup13/                       # Part 3: Library source code
│   ├── alumathgroup13/
│   │   ├── __init__.py
│   │   └── matrix_operations.py
│   ├── setup.py
│   ├── README.md
│   └── requirements.txt
├── tests/
│   └── test_matrix_operations.py
└── README.md                            # This file
```

---

## 👥 Group Members & Contributions

### **Git Log Summary**
```bash
# View individual contributions
git log --oneline --graph --all

# View commits by author
git shortlog -sn
```

**Group 13 Members:**
- **Member 1**: [Name] - PCA implementation, eigenvalue calculations
- **Member 2**: [Name] - Library development, testing
- **Member 3**: [Name] - Documentation, PyPI publishing

---

## 🛠️ Development Setup

### **For PCA Notebook**
```bash
# Install Jupyter
pip install jupyter numpy matplotlib

# Run notebook
jupyter notebook notebooks/pca_implementation.ipynb
```

### **For Library Development**
```bash
# Navigate to library directory
cd alumathgroup13/

# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/
```

---

## 📦 Requirements Met

### **Assignment Requirements Check:**
- ✅ **Matrix Manipulation Library**: Complete
- ✅ **Different Dimensions**: Handles all compatible matrix sizes
- ✅ **Error Handling**: Comprehensive validation
- ✅ **No External Libraries**: Pure Python implementation
- ✅ **PyPI Publication**: Successfully published
- ✅ **Git Log**: All members have meaningful contributions
- ✅ **Documentation**: Complete README with installation instructions

---

## 🔗 Links

- **PyPI Package**: https://pypi.org/project/group13-matrix-operations-2025/1.0.0/
- **GitHub Repository**: https://github.com/yourusername/pca-assignment-group13

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with 💻 Pure Python | Group 13 | Advanced Linear Algebra Course**