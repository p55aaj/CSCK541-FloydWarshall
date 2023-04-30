#Performance for Iterative Floyd Warshall Algorithm

"""
Testing the performance of the iterative solutiuon provided by GeeksforGeeks
for comparison with the recursive function that has been created.

Due to code limitations, the number of vertices has to be manually changed in the Floyd_Iterative.py
document before the test for each test case is run.
"""

import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Algorithms.Floyd_Iterative import floydWarshall

from Tests.Test_cases import (control_input, test_A,
                                test_B, test_C)


import cProfile


#test for a 4x4 matrix
#cProfile.run("floydWarshall(control_input)")

#test for the 7x7 matrix
#cProfile.run("floydWarshall(test_A)")

#test for the 9x9 matrix
#cProfile.run("floydWarshall(test_B)")

#test for the 10x10 matrix
print("test C")
cProfile.run("floydWarshall(test_C)")