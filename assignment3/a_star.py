"""A* Search"""

import heapq

def getHeuristic(a, array):
    heuristic = 0
    for p in array:
        for q in p:
            for r in q:
                if a is r:
                    heuristic = q[2:]
    return heuristic

def a_Star(graph, start, goal, hArray):
    start.setCost(0)
    evaluatedCounter = 0

    queue = []
    for vertex in graph:
        queue.append((vertex.getCost(), vertex))
    heapq.heapify(queue)

    while len(queue):
        unvisited = heapq.heappop(queue)
        curr = unvisited[1]
        curr.setVisited()

        for n in curr.adjacent:
            if not n.visited:
                pass

            newCost = curr.getCost() + curr.getWeight(n) + int(getHeuristic(curr.getId(), hArray))

            if newCost < n.getCost():
                n.setCost(newCost)
                n.setPrevious(curr)

        while len(queue):
            heapq.heappop(queue)

        for vertex in graph:
            if not vertex.visited:
                queue.append((vertex.getCost(), vertex))
        heapq.heapify(queue)
        evaluatedCounter = evaluatedCounter + 1
    return evaluatedCounter

   
            

    
