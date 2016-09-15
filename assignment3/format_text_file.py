"""Read text file into graph.
   Create a pdf of the graph.
   Comment out graphviz if not installed.
"""
import graphviz as gv
from dijkstra import *
from shortest import *
from graph import *
from sys import argv

g = Graph()

with open('assignment3.txt') as f:
    for line in f:
        array = []
        cs = "[']\r\n,"
        for char in cs:
            line = line.replace(char,"")

        for i in line:
            array.append(i)
        g.addVertex(array[0])
        g.addVertex(array[1])

with open('assignment3.txt') as h:
    for line in h:
        array = []
        cs = "[']\r\n,"
        for char in cs:
            line = line.replace(char,"")

        for i in line:
            array.append(i)

        g.addEdge(array[0], array[1], int(array[2]))


"""
g.addVertex('S')
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('P')
g.addVertex('D')
g.addVertex('G')
g.addVertex('E')
g.addVertex('H')
g.addVertex('R')
g.addVertex('J')
g.addVertex('Q')
g.addVertex('L')
g.addVertex('I')
g.addVertex('M')
g.addVertex('N')
g.addVertex('O')
g.addVertex('P')
g.addVertex('K')
g.addVertex('F')

g.addEdge('S','A',2)
g.addEdge('A','B',1)
g.addEdge('B','C',4)
g.addEdge('B','P',6)
g.addEdge('C','D',4)
g.addEdge('D','G',5)
g.addEdge('D','E',4)
g.addEdge('E','R',3)
g.addEdge('G','H',3)
g.addEdge('G','R',4)
g.addEdge('H','I',2)
g.addEdge('H','J',3)
g.addEdge('R','J',2)
g.addEdge('R','L',2)
g.addEdge('P','Q',7)
g.addEdge('Q','L',2)
g.addEdge('L','M',2)
g.addEdge('M','N',3)
g.addEdge('N','O',4)
g.addEdge('O','K',5)
g.addEdge('I','K',3)
g.addEdge('S','A',2)
g.addEdge('K','F',2)
"""



dijkstra(g, g.getVertex('S'), g.getVertex('F'))

goal = g.getVertex('F')

shortestPath = [goal.getId()]
shortest(goal, shortestPath)
print shortestPath[::-1]


"""

#Print Graph in a pdf file, graphviz needed
#Need to comment line in graph.py -> see graph.py
g1 = gv.Graph(format='pdf')

for v1 in g:
        for v2 in v1.getConnection():
            g1.node(v1.getVertex())
            g1.node(v2.getVertex())
            g1.edge(v1.getVertex(),v2.getVertex(), label=str(v1.getWeight(v2)))


filename = g1.render(filename='graphPDF/g1')

"""
