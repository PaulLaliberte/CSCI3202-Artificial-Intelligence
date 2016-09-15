import heapq

def dijkstra(graph, start, end):
    start.setCost(0)

    queue = [(v.getCost(),v) for v in graph]
    heapq.heapify(queue)

    while len(queue):
        unvisited = heapq.heappop(queue)
        curr = unvisited[1]
        curr.setVisited()

        for next in curr.adjacent:
            if next.visited:
                continue
            newCost = curr.getCost() + curr.getWeight(next)

            if newCost < next.getCost():
                next.setCost(newCost)
                next.setPrevious(curr)

        while len(queue):
            heapq.heappop(queue)

        queue = [(v.getCost(), v) for v in graph if not v.visited]
        heapq.heapify(queue)
