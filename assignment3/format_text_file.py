"""Read text file into graph.
   Create a pdf of the graph.
   Comment out graphviz if not installed.
"""
#import graphviz as gv
from dijkstra import *
from a_star import *
from shortest import *
from graph import *
from sys import argv

g = Graph()
a = Graph()


with open('assignment3.txt') as f:
    for line in f:
        array = []
        cs = "[']\r\n,"
        for char in cs:
            line = line.replace(char,"")

        for i in line:
            array.append(i)


        if len(array) is 0:
            break
        else:
            g.addVertex(array[0])
            g.addVertex(array[1])
            a.addVertex(array[0])
            a.addVertex(array[1])

        


with open('assignment3.txt') as h:
    for line in h:
        array = []
        cs = "[']\r\n,"
        for char in cs:
            line = line.replace(char,"")

        for i in line:
            array.append(i)

        if len(array) is 0:
            break
        else:
            g.addEdge(array[0], array[1], int(array[2]))
            a.addEdge(array[0], array[1], int(array[2]))


array = []
newArray = []

with open('assignment3.txt') as i:
    for line in i:
        cs = "[']\r\n,"
        for char in cs:
            line = line.replace(char,"")
        array.append(line)
    m = 0
    for i in array:
        m = m + 1
        if i is '':
            newArray.append(array[m:len(array)-1])
    """
    for p in newarray:
        for q in p:
            for r in q:
                if r is 'A':
                    print q
    """

print "dijkstra number of evaluated nodes: %i" % dijkstra(g, g.getVertex('S'), g.getVertex('F'))
#getHeuristic('A', newArray)

print "a* number of evaluated nodes: %i" % a_Star(a, a.getVertex('S'), a.getVertex('F'), newArray)





goal = g.getVertex('F')

shortestPath = [goal.getId()]
shortest(goal, shortestPath)
print shortestPath[::-1]

goal = a.getVertex('F')

shortestPath = [goal.getId()]
shortest(goal, shortestPath)
print shortestPath[::-1]




"""
#Print Graph in a pdf file, graphviz needed
#Need to comment line in graph.py -> see graph.py
g1 = gv.Graph(format='pdf')

for v1 in g:
        for v2 in v1.getConnections():
            g1.node(v1.getId())
            g1.node(v2.getId())
            g1.edge(v1.getId(),v2.getId(), label=str(v1.getWeight(v2)))


filename = g1.render(filename='graphPDF/g1')
"""

