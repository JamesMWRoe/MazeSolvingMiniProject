import SearchPathStepline
import Stack

name = "Depth First Search"

def search(maze):
    '''Implements the Depth first search algorithm. This code is modified from the code created for ICE-4101
       Introduction to programming assignment 4, by modifying the code given in that assignment for breadth 
       first search.'''
    pathTimeline = SearchPathStepline.SearchPathStepline()
    step = -1
    stack = Stack.Stack() # make an empty stack first
    firstPath = [maze.getStartNode()]

    stack.push(firstPath) # add the start node onto the queue
        
    while stack.isEmpty() == False:
        path = stack.pop()

        pathTimeline.addStep(path)
        step += 1
        lastNode = path[-1]
            
        if lastNode == maze.getEndNode():
            pathTimeline.addValidPath(path)
            pathTimeline.printPathAtStep(step)
            continue
        for linkNode in lastNode.getAdjacencyList():
            if linkNode not in path:
                new_path = []
                new_path = path + [linkNode]
                stack.push(new_path)
        
    return pathTimeline