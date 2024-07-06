class SearchPathStepline:
    '''A class used to represent a search algorithm's progress in traversing a graph as a series of steps.
       Each step is represented as a path of nodes within the graph. The final node in the path is the node
       currently being traversed.'''
    
    def __init__(self):
        '''initialises the stepline with 0 total steps and two empty lists. The first 'stepline' will represent
           The stepline (effectively a timeline but with discrete intervals) of paths, and the second
           'validPaths' will contain all of the paths that traverse the graph from the start to the end.'''
        self.stepline = []
        self.validPaths = []
        self.totalSteps = 0

    def addStep(self, path):
        '''adds a path to the stepline at the end, and increments the totalSteps counter by 1.'''
        self.stepline.append(path)
        self.totalSteps += 1

    def addValidPath(self, path):
        '''adds a path to the validPaths list, should be used alongside the addStep method whenever adding
        a valid path, as the valid path should be added to the stepline.'''
        self.validPaths.append(path)
    
    def getFirstValidPath(self):
        '''For testng purposes. Returns the zeroth value of validPaths (essentially the frst valid path 
           obtained by the search algorithm.'''
        return self.validPaths[0]
    
    def getValidPaths (self):
        '''returns a copy of the list of valid paths.'''
        return self.validPaths.copy()
        
    def getPathAtStep(self, step):
        '''returns the path at the given step.'''
        return self.stepline[step].copy()

    def printPathAtStep(self, step):
        '''For testing purposes. Prints to the terminal an inorder list of the indexes of the nodes within
           the path at the given step by retrieving the path at the step and creating a new list by running 
           through each node within that path and retrieving its index, and then printing this list.'''
        path = self.stepline[step]
        nodeIndexesInPath = []
        for node in path:
            nodeIndex = node.getIndex()
            nodeIndexesInPath.append(nodeIndex)
        
        #print(nodeIndexesInPath)

    def getTotalSteps(self):
        '''returns an integer equal to the total number of steps in the stepline.'''
        return self.totalSteps

if __name__ == '__main__':
    pass