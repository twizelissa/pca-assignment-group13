"""
Matrix operations module for AlumathGroup13
Provides matrix multiplication for different dimensions
"""

def validate_matrices(A, B):
    """
    Validate that matrices can be multiplied
    
    Args:
        A: First matrix (list of lists or numpy array)
        B: Second matrix (list of lists or numpy array)
    
    Returns:
        tuple: (rows_A, cols_A, rows_B, cols_B)
    
    Raises:
        ValueError: If matrices cannot be multiplied
    """
    # Convert to list of lists if needed
    if hasattr(A, 'tolist'):
        A = A.tolist()
    if hasattr(B, 'tolist'):
        B = B.tolist()
    
    # Check if matrices are valid
    if not A or not B:
        raise ValueError("Matrices cannot be empty")
    
    rows_A = len(A)
    cols_A = len(A[0]) if A else 0
    rows_B = len(B)
    cols_B = len(B[0]) if B else 0
    
    # Validate dimensions
    if cols_A != rows_B:
        raise ValueError(f"Cannot multiply matrices: {rows_A}x{cols_A} and {rows_B}x{cols_B}. "
                        f"Number of columns in first matrix ({cols_A}) must equal "
                        f"number of rows in second matrix ({rows_B})")
    
    return rows_A, cols_A, rows_B, cols_B

def matrix_multiply(A, B):
    """
    Multiply two matrices using standard matrix multiplication
    
    Args:
        A: First matrix (list of lists or numpy array)
        B: Second matrix (list of lists or numpy array)
    
    Returns:
        list: Resulting matrix as list of lists
    
    Examples:
        >>> A = [[1, 2], [3, 4]]
        >>> B = [[5, 6], [7, 8]]
        >>> result = matrix_multiply(A, B)
        >>> print(result)
        [[19, 22], [43, 50]]
        
        >>> A = [[1, 2, 3]]
        >>> B = [[4], [5], [6]]
        >>> result = matrix_multiply(A, B)
        >>> print(result)
        [[32]]
    """
    # Validate matrices
    rows_A, cols_A, rows_B, cols_B = validate_matrices(A, B)
    
    # Convert to list of lists if needed
    if hasattr(A, 'tolist'):
        A = A.tolist()
    if hasattr(B, 'tolist'):
        B = B.tolist()
    
    # Initialize result matrix
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def matrix_info(matrix):
    """
    Get information about a matrix
    
    Args:
        matrix: Input matrix (list of lists or numpy array)
    
    Returns:
        dict: Matrix information including dimensions and properties
    """
    if hasattr(matrix, 'tolist'):
        matrix = matrix.tolist()
    
    if not matrix:
        return {"rows": 0, "cols": 0, "is_square": False, "is_empty": True}
    
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    is_square = rows == cols
    
    return {
        "rows": rows,
        "cols": cols,
        "is_square": is_square,
        "is_empty": False,
        "shape": f"{rows}x{cols}"
    }