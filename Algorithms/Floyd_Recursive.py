#Python program for a recursive version of Floyd's algorithm

def floyd(distance):

    #determine the number of vertices (v) of the graph
    v = len(distance)
    
    
    INF = float('inf')

    def shortestPath(i, j, k):
        """
        The recursive function to find the shortest path
        between two vertices   
        """    
        

        #Calculates the direct paths and ends recursion when all nodes
        #have been tried. 
        if k < 0:
            return distance[i][j]
        

        else:
            #returns the minimum distance between two paths with differing
            # intermediate nodes 
            return min(shortestPath(i, j, k -1),
                        shortestPath(i, k, k - 1) + shortestPath(k, j, k - 1))
            
    
    
    
    
    """
    Calling of calculation of shortest path and displaying the matrix showing
    the shortest path
    """
    
    print("The shortest distances between every pair of vertices is:")
    
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distance[i][j] = shortestPath(i,j,k) 
        if k == v-1:
            print(distance)
            return distance                






            