import unittest


from Floyd_Recursive import floyd

from Test_cases import (control_input, control_expected_output,
                        test_A, expected_A,
                        test_B, expected_B,
                        test_C, expected_C)

class floydTests(unittest.TestCase):
    
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

