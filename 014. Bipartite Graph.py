'''
Problem 1:
Check whether a given graph is Bipartite or not
'''

import collections
class Graph(object):
 
    def __init__(self, n, pairs):
        self.graph = collections.defaultdict(list)
        for pair in pairs:
            self.graph[pair[0]].append(pair[1])
            self.graph[pair[1]].append(pair[0])
        self.n = n
 

    def isBipartite(self, src):
        colors = [-1] * self.n
        colors[src] = 1
        q = collections.deque([src])
        while len(q):
            cur = q.popleft()
            if self.graph.has_key(cur):
                for nei in self.graph[cur]:
                    if self.graph.has_key(nei) and cur in self.graph[nei]: # Note
                        self.graph[nei].remove(cur)
                    if colors[nei] == colors[cur]:
                        return False
                    colors[nei] = 1-colors[cur]
                    q.append(nei)
        return True


g = Graph(4, [[0,1],[0,3],[1,2],[2,3]])
print "Yes" if g.isBipartite(0) else "No"
 

 

'''
Problem 2: 
Given an undirected graph and a number m, determine if the graph can be colored with at most m colors 
such that no two adjacent vertices of the graph are colored with same color. 
Here coloring of a graph means assignment of colors to all vertices.
Backtracking: http://www.geeksforgeeks.org/backttracking-set-5-m-coloring-problem/
'''

import collections
class Graph(object):
 
    def __init__(self, n, pairs):
        self.graph = collections.defaultdict(list)
        for pair in pairs:
            self.graph[pair[0]].append(pair[1])
            self.graph[pair[1]].append(pair[0])
        self.n = n


    def canColored(self, m):

        def paintHouse(house):
            def isSafe(house, c):
                for n in self.graph[house]:
                    if colors[n] == c:
                        return False
                return True

            if house == self.n:
                return True
            for c in range(m):
                if isSafe(house, c):
                    colors[house] = c
                    if paintHouse(house+1):
                        return True
                    colors[house] = -1
            return False

        colors = [-1] * self.n
        return paintHouse(0)


        

g = Graph(4, [[0,1],[0,2],[0,3],[1,2],[2,3]])
print "Yes" if g.canColored(3) else "No"








import collections
class Graph(object):
 
    def __init__(self, n, pairs):
        self.graph = collections.defaultdict(list)
        for pair in pairs:
            self.graph[pair[0]].append(pair[1])
            self.graph[pair[1]].append(pair[0])
        self.n = n
 

    def canColored(self, m):
        colors = [-1] * self.n
        colors[0] = 0
        q = collections.deque([0])
        while len(q):
            cur = q.popleft()
            if self.graph.has_key(cur):
                for nei in self.graph[cur]:
                    if self.graph.has_key(nei) and cur in self.graph[nei]: # Note
                        self.graph[nei].remove(cur)
                    # try to paint each neighbour 
                    # if it has not been painted
                    if colors[nei] == -1:
                        avaiColor = set([i for i in range(m)])
                        avaiColor.remove(colors[cur])
                        for n in self.graph[nei]:
                            if colors[n] != -1:
                                avaiColor.remove(colors[n])
                        if len(avaiColor) > 0:
                            colors[nei] = avaiColor.pop()
                            q.append(nei)
                        else:
                            return False
        return True


g = Graph(4, [[0,1],[0,2],[0,3],[1,2],[2,3]])
print "Yes" if g.canColored(3) else "No"
 
