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

    def addConnection(self,weight=0):
        pass

    def getConnection(self):
        return self.adjacent.keys()

    def getVertex(self):
        return self.vertex

    def getWeight(self,connection):
        pass



class Graph:
    
    def __init__(self):
        self.vertexDictionary = {}
        self.verticesCount = 0

    def __iter__(self):
        return iter(self.vertexDictionary.values())

    def addVertex(self,vertex):
        pass

    def addEdge(self,vertex1,vertex2,weight=0):
        pass



        
   
