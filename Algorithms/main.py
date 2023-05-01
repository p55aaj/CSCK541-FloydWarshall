#Main Script to call the recursive Floyd Warshall Algorithm

from Floyd_Recursive import floyd


#Define infinity. The value is used for vertices not connected to each other
INF = float('inf')

#Define the graph to be called (represented as a matrix)
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
        ]

floyd(graph)







