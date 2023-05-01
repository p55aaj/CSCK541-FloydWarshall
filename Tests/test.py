"""
Unit Test file for the recursive function
"""

#Importing the Floyd algorithm from another folder
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


# Importing the unittest package
import unittest

# Importing the Recursive algortihm
from Algorithms.Floyd_Recursive import floyd

# Importing the various test cases and expected results
from Test_cases import (control_input, control_expected_output,
                        test_A, expected_A,
                        test_B, expected_B,
                        test_C, expected_C)

class floydTests(unittest.TestCase):
    """
    Testing the various cases. If there is an error, an output is dispalyed showing that there is an error in the output of the recursive code
    """


    def test_control(self):
        self.assertEqual(floyd(control_input), control_expected_output,
        "Output is not what was expected")

    def test_testA(self):
        self.assertEqual(floyd(test_A), expected_A,
        "Output is not what was expected")
    
    def test_testB(self):
        self.assertEqual(floyd(test_B), expected_B,
        "Output is not what was expected")

    def test_testC(self):
        self.assertEqual(floyd(test_C), expected_C,
        "Output is not what was expected")

if __name__ == '__main__':
    unittest.main()

