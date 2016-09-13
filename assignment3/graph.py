"""Graph Class.
   Two classes, Vertex and Graph. Uses dict in dicts to represent graph.
   Version: Python 2.7.x
"""

class Vertex:

    def __init__(self,vertex):
        self.vertex=vertex
        self.adjacent = {}

    def __str__(self):
        vtx = str(self.vertex)
        adj = str([i.vertex for i in self.adjacent])
        return vtx + ' adjacent vertex: ' + adj

    def addConnection(self,vertex,weight=0):
        self.adjacent[vertex] = weight

    def getConnection(self):
        return self.adjacent.keys()

    def getVertex(self):
        return self.vertex

    def getWeight(self,vertex):
        return self.adjacent[vertex]



class Graph:
    
    def __init__(self):
        self.vertexDictionary = {}

    def __iter__(self):
        return iter(self.vertexDictionary.values())

    def addVertex(self,vertex):
        if vertex not in self.vertexDictionary:
            newVertex = Vertex(vertex)
            self.vertexDictionary[vertex] = newVertex
            return newVertex


    def addEdge(self,vertex1,vertex2,weight=0):
        if vertex1 not in self.vertexDictionary:
            self.addVertex(vertex1)
        if vertex2 not in self.vertexDictionary:
            self.addVertex(vertex2)

        self.vertexDictionary[vertex1].addConnection(self.vertexDictionary[vertex2], weight)






        
   
