#Performance tests for Floyd Warshall algorithm
"""
    This tests the performance of the recurisve algorithm
"""

import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

#Importing the recursive and iterative algorithms
from Algorithms.Floyd_Recursive import floyd



#Importing the test cases
from Test_cases import (control_input, test_A, test_B, test_C)

#Importing the testing package
import cProfile

#Following are the performance tests

# Testing of control case (a 4x4 matrix)
print("Performance Tests of Control Inputs")
cProfile.run("floyd(control_input)")


# Testing of test case A (a 7x7 matrix)
print("Performance Tests of test_A")
cProfile.run("floyd(test_A)")


#Testing of test case B (a 9x9 matrix)
print("Performance Tests of test_B")
cProfile.run("floyd(test_B)")


# Testing of test case C (a 10x10 matrix)
print("Performance tests of test_C")
cProfile.run("floyd(test_C)")
