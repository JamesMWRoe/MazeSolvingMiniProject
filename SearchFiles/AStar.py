import SearchPathStepline

name = 'A* Search'

def search(maze):
    '''Implements the A* Search algorithm as found on: https://brilliant.org/wiki/a-star-search/
       The basic idea of this algorithm is to implement Dijkstra's but with an estimator, called a
       heuristic, to help weight which node to choose next. The heuristic chosen in this case was
       the manhattan distance which is the distance between the current node and the end node
       in the x direction plus that in the y direction.'''
    pathTimeline = SearchPathStepline.SearchPathStepline()

    endNodeHasBeenFound = False

    mazeGraph = maze.getGraph()
    graphOrder = mazeGraph.getOrder()
    startNode = maze.getStartNode()
    endNode = maze.getEndNode()

    previousNodeArray = [None] * graphOrder 

    gArray = [graphOrder+1] * graphOrder
    gArray[startNode.getIndex()] = 0

    hArray = []
    for i in range(mazeGraph.getOrder()):
        currentNode = mazeGraph.getNode(i)
        xCoordinate, yCoordinate = currentNode.getCoordinates()
        endXCoordinate, endYCoodinate = endNode.getCoordinates()
        manhattanDistance = abs(xCoordinate - endXCoordinate) + abs(yCoordinate - endYCoodinate)
        hArray.append(manhattanDistance)

    openList = [(startNode)]
    
    closedList = []

    while not endNodeHasBeenFound:

        lowestFValueNode = openList[0]
        for node in openList:
            nodeFValue = gArray[node.getIndex()] + hArray[node.getIndex()]
            lowestFValue = gArray[lowestFValueNode.getIndex()] + hArray[lowestFValueNode.getIndex()]
            if nodeFValue < lowestFValue:
                lowestFValueNode = node
        currentNode = openList.pop(openList.index(lowestFValueNode)) #pop value with lowest f

        path = []
        currentNodeIndex = currentNode.getIndex()

        while currentNodeIndex is not None:
            path.append(mazeGraph.getNode(currentNodeIndex))
            currentNodeIndex = previousNodeArray[currentNodeIndex]

        pathTimeline.addStep(path)

        if currentNode == endNode:
                endNodeHasBeenFound = True
        
        for node in currentNode.getAdjacencyList():
            temporaryGValue = gArray[currentNode.getIndex()] + 1
            if temporaryGValue < gArray[node.getIndex()]:
                gArray[node.getIndex()] = temporaryGValue
                previousNodeArray[node.getIndex()] = currentNode.getIndex()
                if node not in openList and node not in closedList:
                    openList.append(node)
        
        closedList.append(currentNode)
    
    shortestPath = []
    currentNodeIndex = endNode.getIndex()
    while currentNodeIndex is not None:
        shortestPath.append(mazeGraph.getNode(currentNodeIndex))
        currentNodeIndex = previousNodeArray[currentNodeIndex]
    
    pathTimeline.addStep(shortestPath)
    pathTimeline.addValidPath(shortestPath)

    print(pathTimeline.printPathAtStep(-1))

    return pathTimeline