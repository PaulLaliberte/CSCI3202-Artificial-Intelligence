"""A* Search"""

def getHeuristic(a, array):
    heuristic = 0
    for p in array:
        for q in p:
            for r in q:
                if a is r:
                    heuristic = q[2]
    print heuristic

def a_Star():
    pass
