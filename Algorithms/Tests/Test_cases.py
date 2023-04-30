#Test cases for the Floyd algorithm

"""
There are 3 test graphs outlined, plus one control graph, to test various
outcomes. The expected outcomes are also defined.
"""

#Define INF as a very large number to represent infinity
INF = float('inf')

#Control Graph
"""
This control graph is from the GeeksforGeeks website, outlining the Floyd
algorithm using an iterative method
"""

control_input = [[0, 5, INF, 10],
                 [INF, 0, 3, INF],
                 [INF, INF, 0, 1],
                 [INF, INF, INF, 0]
                ]

control_expected_output = [[0, 5, 8, 9],
                            [INF, 0, 3, 4],
                            [INF, INF, 0, 1],
                            [INF, INF, INF, 0]
                            ]

#Test A 7x7 matrix
test_A =  [[0, INF, INF, INF, INF, INF, 15],
             [INF, 0, INF, 35, INF, INF, INF],
             [INF, INF, 0, INF, INF, 42, INF],
             [INF, INF, INF, 0, 56, INF, INF],
             [INF, INF, INF, INF, 0, 41, INF],
             [INF, INF, INF, INF, INF, 0, INF],
             [INF, INF, INF, INF, INF, INF, 0],
             ]

expected_A = [[0, INF, INF, INF, INF, INF, 15],
                [INF, 0, INF, 35, 91, 132, INF],
                [INF, INF, 0, INF, INF, 42, INF],
                [INF, INF, INF, 0, 56, 97, INF],
                [INF, INF, INF, INF, 0, 41, INF],
                [INF, INF, INF, INF, INF, 0, INF],
                [INF, INF, INF, INF, INF, INF ,0]
                ]


#Test B, 9x9 matrix
test_B = [[0, 16, INF, 71, INF, 94, 30, INF, INF],
          [INF, 0, 43, INF, INF, INF, INF, INF, INF],
          [INF, INF, 0, INF, INF, INF, INF, INF, INF],
          [INF, INF, INF, 0, INF, 5, 75, INF, INF],
          [INF, INF, INF, INF, 0, INF, 66, 52, INF],
          [INF, INF, INF, INF, INF, 0, 29, INF, 48],
          [INF, INF, INF, INF, INF, INF, 0, 84, INF],
          [INF, INF, INF, INF, INF, INF, INF, 0, INF],
          [INF, INF, INF, INF, INF, INF, INF, INF, 0]
         ]

expected_B = [[0, 16, 59, 71, INF, 76, 30, 114, 124],
              [INF, 0, 43, INF, INF, INF, INF, INF, INF],
              [INF, INF, 0, INF, INF, INF, INF, INF, INF],
              [INF, INF, INF, 0, INF, 5, 34, 118, 53],
              [INF, INF, INF, INF, 0, INF, 66, 52,INF],
              [INF, INF, INF, INF, INF, 0, 29, 113, 48],
              [INF, INF, INF, INF, INF, INF, 0, 84, INF],
              [INF, INF, INF, INF, INF, INF, INF, 0, INF],
              [INF, INF, INF, INF, INF, INF, INF, INF, 0]]


#Test C, 10x10 matrix with large numbers
test_C = [[0, INF, INF, INF, INF, 343, INF, 1435, 464, INF],
             [INF, 0, INF, INF, INF, 879, 954, 811, INF, 524],
             [INF, INF, 0, INF, 1364, 1054, INF, INF, INF, INF],
             [INF, INF, INF, 0, INF, INF, 433, INF, INF, 1053],
             [INF, INF, 1364, INF, 0, 1106, INF, INF, INF, 766],
             [343, 879, 1054, INF, 1106, 0, INF, INF, INF, INF],
             [INF, 954, INF, 433, INF, INF, 0, 837, INF, INF],
             [1435, 811, INF, INF, INF, INF, 837, 0, INF, INF],
             [464, INF, INF, INF, INF, INF, INF, INF, 0, INF],
             [INF, 524, INF, 1053, 766, INF, INF, INF, INF, 0]
            ]

expected_C = [[0, 1222, 1397, 2609, 1449, 343, 2176, 1435, 464, 1746],
              [1222, 0, 1933, 1387, 1290, 879, 954, 811, 1686, 524],
              [1397, 1933, 0, 3183, 1364, 1054, 2887, 2744, 1861, 2130],
              [2609, 1387, 3183, 0, 1819, 2266, 433, 1270, 3073, 1053],
              [1449, 1290, 1364, 1819, 0, 1106, 2244, 2101, 1913, 766],
              [343, 879, 1054, 2266, 1106, 0, 1833, 1690, 807, 1403],
              [2176, 954,2887, 433, 2244, 1833, 0, 837, 2640, 1478],
              [1435, 811, 2744, 1270, 2101, 1690, 837, 0, 1899, 1335],
              [464, 1686, 1861, 3073, 1913, 807, 2640, 1899, 0, 2210],
              [1746, 524, 2130, 1053, 766, 1403, 1478, 1335, 2210, 0]
             ]


