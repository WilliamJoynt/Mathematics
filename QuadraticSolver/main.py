"""
This is a programme that will solve quadratic equations.

Quadratic equations look like this: 

    Ax^2 + Bx + C

This is the formula:

    (-B +- √((B^2)-4(A*C))) / 2*A
"""
import math

#####################################
# Helper functions for this programme

def solve(A: int, B: int, C: int):
    if (pow(B, 2) - 4*(A*C)) < 0:
        print("Invalid quadratic")
        root1 = None
        root2 = None
    else:
        root1 = ((-1 * B) + math.sqrt(pow(B, 2) - 4*(A*C))) / (2 * A)
        root2 = ((-1 * B) - math.sqrt(pow(B, 2) - 4*(A*C))) / (2 * A)
    
    return root1, root2

###################################
# The main programme starts here

print("Input A,B,C from the equation Ax^2 + Bx + C")

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

root1, root2 = solve(A, B, C)

print(root1, root2)