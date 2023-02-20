from collections import defaultdict

class Graph:
    def __init__(self):
        self.gDict = {}
        
    def addVertex(self, vertex):
        if vertex not in self.gDict.keys():
            self.gDict[vertex] = []
            return True
        return False
    
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.gDict.keys() and vertex2 in self.gDict.keys():
            self.gDict[vertex1].append(vertex2)
            self.gDict[vertex2].append(vertex1)
            return True
        return False
    
    def printGraph(self):
        for vertex in self.gDict:
            print(vertex, ":", self.gDict[vertex])
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.gDict.keys() and vertex2 in self.gDict.keys():
            try:
                self.gDict[vertex1].remove(vertex2)
                self.gDict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def removeVertex(self, vertex):
        if vertex in self.gDict.keys():
            for other_vertex in self.gDict[vertex]:
                self.gDict[other_vertex].remove(vertex)
            del self.gDict[vertex]
            return True
        return False
 
class Graph1:
    def __init__(self, numberOfVertex):
        self.graph = defaultdict(list)
        self.numberOfVertex = numberOfVertex
        
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
        
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjVertex in self.gDict[popVertex]:
                if adjVertex not in visited:
                    stack.append(adjVertex)
                     
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjVertex in self.gDict[deVertex]:
                if adjVertex not in visited:
                    queue.append(adjVertex)
                    
    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)
        
    def topologicalSort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        print(stack)
    
            
graph = Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("A", "D")
graph.addEdge("B", "C")
graph.addEdge("C", "D")
graph.printGraph()
graph.removeVertex("D")
print("-------------")
graph.dfs("A")