# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(name=""):
    """Read a matrix from user input."""
    print(f"\nEnter {name}:")
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        if rows <= 0 or cols <= 0:
            print("Error: Rows and columns must be positive.")
            return None
        
        matrix = []
        for i in range(1, rows + 1):
            row = list(map(float, input(f"Enter row {i}: ").split()))
            if len(row) != cols:
                print(f"Error: Row {i} has {len(row)} elements, expected {cols}.")
                return None
            matrix.append(row)
        
        return matrix
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return None


def display_matrix(matrix, name="Matrix"):
    """Display a matrix in a neat grid format."""
    if matrix is None:
        return
    
    print(f"\n{name}:")
    for row in matrix:
        print("  ".join(f"{val:>8.2f}" if isinstance(val, float) else f"{val:>8}" for val in row))


def transpose(matrix):
    """Transpose a matrix (rows become columns)."""
    if matrix is None or len(matrix) == 0:
        return None
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed


def add_matrices(matrix1, matrix2):
    """Add two matrices of the same size."""
    if matrix1 is None or matrix2 is None:
        return None
    
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Matrices must have the same dimensions.")
        return None
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result


def multiply_matrices(matrix1, matrix2):
    """Multiply two matrices."""
    if matrix1 is None or matrix2 is None:
        return None
    
    if len(matrix1[0]) != len(matrix2):
        print("Error: Number of columns in first matrix must equal number of rows in second matrix.")
        return None
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            cell_value = 0
            for k in range(len(matrix2)):
                cell_value += matrix1[i][k] * matrix2[k][j]
            row.append(cell_value)
        result.append(row)
    
    return result


def main():
    """Main function to run matrix operations."""
    while True:
        print("\n" + "="*40)
        print("MATRIX OPERATIONS")
        print("="*40)
        print("1. Transpose a matrix")
        print("2. Add two matrices")
        print("3. Multiply two matrices")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            matrix = read_matrix("the matrix")
            transposed = transpose(matrix)
            display_matrix(matrix, "Original Matrix")
            display_matrix(transposed, "Transposed Matrix")
        
        elif choice == "2":
            matrix1 = read_matrix("the first matrix")
            matrix2 = read_matrix("the second matrix")
            result = add_matrices(matrix1, matrix2)
            display_matrix(matrix1, "Matrix 1")
            display_matrix(matrix2, "Matrix 2")
            display_matrix(result, "Sum of Matrices")
        
        elif choice == "3":
            matrix1 = read_matrix("the first matrix (A)")
            matrix2 = read_matrix("the second matrix (B)")
            result = multiply_matrices(matrix1, matrix2)
            display_matrix(matrix1, "Matrix A")
            display_matrix(matrix2, "Matrix B")
            display_matrix(result, "Product A × B")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
