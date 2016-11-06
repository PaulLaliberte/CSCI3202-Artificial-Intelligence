"""Use of a heap for dij."""


import heapq


def dijkstra(graph, start, end):
    start.setCost(0)
    solved = [start.getId()]

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

            newCost = curr.getCost() + curr.getWeight(n)

            if newCost < n.getCost():
                n.setCost(newCost)
                n.setPrevious(curr)
                if curr.getId() not in solved:
                    solved.append(curr.getId())



        while len(queue):
            heapq.heappop(queue)

        for vertex in graph:
            if not vertex.visited:
                queue.append((vertex.getCost(), vertex))
        heapq.heapify(queue)
    if end.visited:
        solved.append(end.getId())
    return solved

