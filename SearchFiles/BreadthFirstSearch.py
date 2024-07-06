import SearchPathStepline
import Queue

name = "Breadth First Search"

def search(maze):
    '''Implements the Breadth first search algorithm. This code is modified from the code given in ICE-4101
       Introduction to programming assignment 4. The modifications aren't major but effectively take the paths
       that were previously just printed and adds them to a stepline which can be used later on.'''
    pathTimeline = SearchPathStepline.SearchPathStepline()
    step = -1
    queue = Queue.Queue()
    startNode = maze.getStartNode()
    endNode = maze.getEndNode()
    firstPath = [startNode]

    queue.enqueue(firstPath)

    while queue.IsEmpty() == False:

        path = queue.dequeue()

        pathTimeline.addStep(path)
        step += 1
        lastNode = path[-1]

        if lastNode == endNode:
            pathTimeline.addValidPath(path)
            pathTimeline.printPathAtStep(step)
            continue
        for linkNode in lastNode.getAdjacencyList():
        
            if linkNode not in path:
                new_path = []
                new_path = path + [linkNode]
                queue.enqueue(new_path)
    
    return pathTimeline