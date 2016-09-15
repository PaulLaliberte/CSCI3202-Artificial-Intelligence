"""Graph Class.
   Two classes, Vertex and Graph. Uses dict in dicts to represent graph.
   Version: Python 2.7.x
"""


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.cost = float('inf')
        self.visited = False
        self.previous = None

    def addNode(self, node, weight=0):
        self.adjacent[node] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getId(self):
        return self.id

    def getWeight(self, node):
        return self.adjacent[node]

    def setCost(self, cost):
        self.cost = cost

    def getCost(self):
        return self.cost

    def setPrevious(self, previous):
        self.previous = previous

    def setVisited(self):
        self.visited = True




class Graph:

    def __init__(self):
        self.vertexDictionary = {}

    def __iter__(self):
        return iter(self.vertexDictionary.values())

    def addVertex(self, node):
        newV = Vertex(node)
        self.vertexDictionary[node] = newV
        return newV

    def getVertex(self, node):
        if node in self.vertexDictionary:
            return self.vertexDictionary[node]
        else:
            return None

    def addEdge(self, v1, v2, weight = 0):
        if v1 not in self.vertexDictionary:
            self.addVertex(v1)
        if v2 not in self.vertexDictionary:
            self.addVertex(v2)

        self.vertexDictionary[v1].addNode(self.vertexDictionary[v2], weight)


    def getVerticies(self):
        return self.vertexDictionary.keys()

    def setPrevious(self, curr):
        self.setPrevious = curr

    def getPrevious(self, curr):
        return self.previous

      
   
