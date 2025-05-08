from typing import List
"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

# Row & column set to 0

# M * N

# Brute Force
# O(MN)
# Iterate through the 2D matrix - keep track of which rows and columns to set to 0
# Iterate again and set columns and rows to 0

def main():
    m_1 = [[1, 1, 1],[0, 1, 1],[1, 1, 1]]
    answer_1 = [[0, 1, 1], [0, 0, 0], [0, 1, 1]]
    if zero_matrix(m_1) != answer_1:
        print(f"Test 1 failed!")
    
    m_2= [
        [0], 
        [1], 
        [1]
    ]
    answer_2= [
        [0], 
        [0], 
        [0]
    ]
    if zero_matrix(m_2) != answer_2:
        print(f"Test 2 failed!")

    m_3= [[]
       
    ]
    answer_3= [[]  
    ]
    if zero_matrix(m_3) != answer_3:
        print(f"Test 3 failed!")
    
# O(m*n)
def zero_matrix(matrix: List[List[int]]):
    print(f"\nTesting for matrix:\n")
    format_matrix_print(matrix)
    rows = set()
    columns = set()
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            #print(f"At row: {row} col: {col} value: {matrix[row][col]}")
            if matrix[row][col] == 0:
                rows.add(row)
                columns.add(col)
    #print(f"Rows: {rows}")
    #print(f"Columns: {columns}")
    for row in rows:
        matrix[row] = [0] * len(matrix[0])
    
    # O(m*n)
    for col in columns:
        for i in range(0, len(matrix)):
            matrix[i][col] = 0
    print(f"\nFinal matrix:")
    format_matrix_print(matrix)
    return matrix

def format_matrix_print(matrix: List[List[int]]):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()




