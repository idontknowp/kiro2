# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

from collections import defaultdict


# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

        # A utility function to find set of an element i

    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

        # A function that does union of two sets of x and y

    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

            # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):

        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1:  Sort all the edges in non-decreasing
        # order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [];
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

            # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                # Else discard the edge

        # # print the contents of result[] to display the built MST
        # print("Following are the edges in the constructed MST")
        # for u, v, weight in result:
        #     # print str(u) + " -- " + str(v) + " == " + str(weight)
        #     print("%d -- %d == %d" % (u, v, weight))

        return result


class Graph2:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0
        self.tour = []

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

        # This function removes edge u-v from graph
    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

                # A DFS based function to count reachable vertices from v

    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)
        return count

        # The function to check if edge u-v can be considered as next edge in

    # Euler Tour
    def isValidNextEdge(self, u, v):
        # The edge u-v is valid in one of the following two cases:

        #  1) If v is the only adjacent vertex of u
        if len(self.graph[u]) == 1:
            return True
        else:
            ''' 
             2) If there are multiple adjacents, then u-v is not a bridge 
                 Do following steps to check if u-v is a bridge 

            2.a) count of vertices reachable from u'''
            visited = [False] * (self.V)
            count1 = self.DFSCount(u, visited)

            '''2.b) Remove edge (u, v) and after removing the edge, count 
                vertices reachable from u'''
            self.rmvEdge(u, v)
            visited = [False] * (self.V)
            count2 = self.DFSCount(u, visited)

            # 2.c) Add the edge back to the graph
            self.addEdge(u, v)

            # 2.d) If count1 is greater, then edge (u, v) is a bridge
            return False if count1 > count2 else True

    # Print Euler tour starting from vertex u
    def printEulerUtil(self, u):
        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v):
                self.rmvEdge(u, v)
                self.tour.append([u, v])
                self.printEulerUtil(v)


    '''The main function that print Eulerian Trail. It first finds an odd 
   degree vertex (if there is any) and then calls printEulerUtil() 
   to print the path '''

    def printEulerTour(self):
        # Find a vertex with odd degree
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        # Print tour starting from odd vertex
        self.printEulerUtil(u)

