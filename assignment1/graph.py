class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, value):
        #check if value already exists
        if value in self.vertices:
            print("Vertex already exists")
        else:
            self.vertices[value] = []

    def addEdge(self, value1, value2):
        #check for vertex
        if value1 not in self.vertices or value2 not in self.vertices:
            print("One or more vertices not found.")
        else:
            #connect both
            self.vertices[value1].append(value2)
            self.vertices[value2].append(value1)


    def findVertex(self, value):
        foundValue = False
        if value in self.vertices:
            foundValue = True
        
        #print adjacent
        edges = []
        if foundValue == True:
            for i in self.vertices[value]:
                edges.append(i)
            print(edges)
        else:
            print("Not found.")











#Tests



print("-------------------------------------------")
print("Graph Test")
print("Add 10 vertecies, make 20 edges, print edges of five vertecies")
print("")

g = Graph()
g.addVertex(1)
g.addVertex(11)
g.addVertex(12)
g.addVertex(13)
g.addVertex(14)
g.addVertex(15)
g.addVertex(16)
g.addVertex(17)
g.addVertex(18)
g.addVertex(19)
g.addVertex(100)

g.addEdge(1,12)
g.addEdge(1,13)
g.addEdge(11,14)
g.addEdge(15,11)
g.addEdge(16,100)
g.addEdge(15,17)
g.addEdge(15,12)
g.addEdge(12,13)
g.addEdge(12,14)
g.addEdge(12,16)
g.addEdge(12,17)
g.addEdge(1,100)
g.addEdge(12,100)
g.addEdge(15,100)
g.addEdge(19,12)
g.addEdge(13,100)
g.addEdge(14,100)
g.addEdge(100,19)
g.addEdge(19,18)
g.addEdge(19,17)

g.findVertex(1)
g.findVertex(12)
g.findVertex(13)
g.findVertex(14)
g.findVertex(100)
