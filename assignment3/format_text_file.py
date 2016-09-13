"""Read text file into graph.
   Create a pdf of the graph.
   Comment out graphviz if not installed.
"""
import graphviz as gv
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
#Doesn't print inorder
for v1 in g:
        for v2 in v1.getConnection():
            ve1 = v1.getVertex()
            ve2 = v2.getVertex()
            print '(%s, %s, %i)'  % ( ve1, ve2, v1.getWeight(v2))
"""


#Print Graph in a pdf file, graphviz needed
g1 = gv.Graph(format='pdf')

for v1 in g:
        for v2 in v1.getConnection():
            g1.node(v1.getVertex())
            g1.node(v2.getVertex())
            g1.edge(v1.getVertex(),v2.getVertex(), label=str(v1.getWeight(v2)))


filename = g1.render(filename='graphPDF/g1')


