"""
Math 560
Project 4
Fall 2020

Partner 1:
Partner 2:
Date:
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
"""
def ED(src, dest):
    # First, initialize the table.
    n = len(src)
    m = len(dest)
    dpTable = [[0 for j in range(m+1)] for i in range(n+1)]

    # Fill in the base cases (first row and first column).
    # rows
    for i in range(-1,n):
        dpTable[i+1][0] = i+1
    # columns
    for j in range(-1,m):
        dpTable[0][j+1] = j+1

    # Fill in table by iterating across each row
    for i in range(1,n+1):
        for j in range(1,m+1):
            if src[i-1] == dest[j-1]:
                dpTable[i][j] = dpTable[i-1][j-1]
            else:
                dpTable[i][j] = 1 + min(dpTable[i-1][j],dpTable[i][j-1],dpTable[i-1][j-1])

    dist = dpTable[n][m]
    # Reconstruct the solution
    # Initialize indices i, j to end of strings
    i, j = n, m
    # Adding null to beginning of strings
    src = " " + src
    dest = " " + dest
    # Initialize empty edits list
    edits = []
    # Continue searching until base case is reached where DP Table is 0
    while (dpTable[i][j] != 0):
        # If the same letter, then match
        if src[i] == dest[j]:
            edits.append(('match', src[i], i-1))
            i,j = i-1, j-1
        # Else calculate the values for insert,delete, and substitute
        # Take the minimum to determine which cell we came from in DP Table
        else:
            insert = dpTable[i][j-1]
            delete = dpTable[i-1][j]
            sub = dpTable[i-1][j-1]
            # If the minimum is equal to insert value
            # Append letter to insert and move left one column
            if min(insert,delete,sub) == insert:
                edits.append(('insert', dest[j], i))
                i,j = i,j-1
            # If minimum is equal to delete value
            # Append letter to delete and move up one row
            elif min(insert, delete, sub) == delete:
                edits.append(('delete', src[i], i-1))
                i,j = i-1,j
            else:
            # If minimum is equal to substitute value
            # Append letter to be substituted and move up one row and left one column
                edits.append(('sub', dest[j],i-1))
                i,j = i-1,j-1


    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300)
    print()
    compareRandStrings(True, 30, 300)