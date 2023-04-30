from Floyd_Recursive import floyd

INF = float('inf')

graph = [[0, 16, INF, 71, INF, 94, 30, INF, INF],
          [INF, 0, 43, INF, INF, INF, INF, INF, INF],
          [INF, INF, 0, INF, INF, INF, INF, INF, INF],
          [INF, INF, INF, 0, INF, 5, 75, INF, INF],
          [INF, INF, INF, INF, 0, INF, 66, 52, INF],
          [INF, INF, INF, INF, INF, 0, 29, INF, 48],
          [INF, INF, INF, INF, INF, INF, 0, 84, INF],
          [INF, INF, INF, INF, INF, INF, INF, 0, INF],
          [INF, INF, INF, INF, INF, INF, INF, INF, 0]
         ]

floyd(graph)







