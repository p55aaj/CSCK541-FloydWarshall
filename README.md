# CSCK541-FloydWarshall

This is a directory that contains a recurisve function of the Floyd-Warshall algorithm. 

# How do I run the programme?

In main.py, enter the graph that you wish to test, an example is below:

```
# Main Script to call the recursive Floyd Warshall Algorithm

from Floyd_Recursive import floyd


# Define infinity. The value is used for vertices not connected to each other
INF = float('inf')

# Define the graph to be called (represented as a matrix)
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
        ]

floyd(graph)
```

# Testing
The test cases and tests are in the "Tests" subfolder. To run the unit tests, run the test.py file. 

```
python Tests/test.py
```

To run the performance tests for the recursive function, run the performance_tests_recursive.py file.
```
python Tests/performance_tests_recursive.py
```
