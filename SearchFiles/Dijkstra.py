import SearchPathStepline
import PriorityQueue

name = "Dijkstra's Shortest Path Search"

def search(maze):
    '''Implements Dijkstras Shortest Path algorithm as explained here: https://www.programiz.com/dsa/dijkstra-algorithm
       Only makes use of the pseudocode. The basic idea of this algorithm is to find the shortest distance 
       to each node and by doing so you can find the shortest distance to the nodes neighbouring a node.'''
    pathTimeline = SearchPathStepline.SearchPathStepline()

    mazeGraph = maze.getGraph()
    graphOrder = mazeGraph.getOrder()
    startNode = maze.getStartNode()
    endNode = maze.getEndNode()

    distanceArray = [graphOrder+1] * graphOrder
    distanceArray[startNode.getIndex()] = 0

    previousNodeArray = [None] * graphOrder  

    queue = PriorityQueue.PriorityQueue()
    for nodeIndex in range(graphOrder):
        node = mazeGraph.getNode(nodeIndex)
        queue.enqueue(node, distanceArray[nodeIndex])
    
    traversedNodes = []

    while endNode not in traversedNodes:
        currentNode = queue.dequeue()
        traversedNodes.append(currentNode)

        path = []
        currentNodeIndex = currentNode.getIndex()
        while currentNodeIndex is not None:
            path.append(mazeGraph.getNode(currentNodeIndex))
            currentNodeIndex = previousNodeArray[currentNodeIndex]

        pathTimeline.addStep(path)

        for node in currentNode.getAdjacencyList():
            if node not in traversedNodes:
                temporaryDistance = distanceArray[currentNode.getIndex()] + 1
                if temporaryDistance < distanceArray[node.getIndex()]:
                    distanceArray[node.getIndex()] = temporaryDistance
                    previousNodeArray[node.getIndex()] = currentNode.getIndex()
                    queue.updatePriority(node, temporaryDistance)
    
    shortestPath = []
    currentNodeIndex = endNode.getIndex()
    while currentNodeIndex is not None:
        shortestPath.append(mazeGraph.getNode(currentNodeIndex))
        currentNodeIndex = previousNodeArray[currentNodeIndex]
    
    pathTimeline.addStep(shortestPath)
    pathTimeline.addValidPath(shortestPath)

    print(pathTimeline.printPathAtStep(-1))

    return pathTimeline