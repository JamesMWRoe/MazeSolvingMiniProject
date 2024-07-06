import Graph
import json

class Maze:
    def __init__(self, mazeData):
        '''Initialises the Maze Object. It takes an object which has the data to represent a maze, 
           and sorts this information to be easily readable for other modules.
           The major information it obtains is the location of the entrance and exit of the maze,
           as well as the informaton that represents the walls of the maze.'''

        self.lineRepresentation = {}
        self.lineRepresentation["horizontal"] = mazeData["mazeHorizontal"]
        self.lineRepresentation["vertical"] = mazeData["mazeVertical"]

        self.height = len(self.lineRepresentation["horizontal"]) - 1
        self.width = len(self.lineRepresentation["vertical"]) - 1
        self.size = self.width * self.height

        self.mazeGraph = Graph.Graph(self.size)

        self.graphSetup()

        self.startNode = self.mazeGraph.getNode(mazeData["start node"])
        self.endNode = self.mazeGraph.getNode(mazeData["end node"])

    def graphSetup(self):
        '''generates a graph of nodes associated with the maze. It does this by creating a graph that has an 
           order equal to the number of rooms of the maze and then finding where there is white space 
           between rooms using the horizontal and vertical line representations. Wherever there is white
           space between rooms, an edge is added between the nodes associated with these rooms. It also 
           sets the coordinates of these nodes where the bottom left most room has coordinate (0,0), and
           the top right room has coordinate (width of maze - 1, height of maze - 1)'''
        
        horizontalLines = self.getHorizontalLineRepresentation()
        horizontalLines.pop()
        horizontalLines.pop(0)
        currentVertex = 0

        for line in horizontalLines:
            blockIsWall = not line.pop()
            
            for block in line:
                if not blockIsWall:
                    for i in range(block):
                        
                        nextVertex = currentVertex + self.width
                        self.mazeGraph.addEdge(currentVertex, nextVertex)
                        currentVertex += 1
                else:
                    currentVertex += block
                
                blockIsWall = not blockIsWall
        
        verticalLines =  self.getVerticalLineRepresentation()
        verticalLines.pop()
        verticalLines.pop(0)
        currentLine = 0

        for line in verticalLines:
            blockIsWall = not line.pop()
            currentVertex = currentLine

            for block in line:
                if not blockIsWall:
                    for i in range(block):
                        nextVertex = currentVertex + 1
                        self.mazeGraph.addEdge(currentVertex, nextVertex)
                        currentVertex += self.width
                else:
                    currentVertex += block * self.width
                
                blockIsWall = not blockIsWall
            currentLine += 1

        x = 0
        y = 0
        for i in range(self.size):
            self.mazeGraph.setNodeCoordinates(i, (x, y))
            if x >= self.getWidth()-1:
                x = 0
                y += 1
            
            else:
                x += 1

    def getStartNode(self):
        '''returns the node of the start/entrance of the maze'''
        return self.startNode
    
    def getEndNode(self):
        '''returns the node of the end/exit of the maze'''
        return self.endNode

    def getGraph(self):
        '''returns the graph associated with the maze. Each node of this graph represents a room of the maze, 
           and the edges between these nodes represent that these rooms can be traversed between ie. they're
           next to each other and have no wall between them'''
        return self.mazeGraph

    def getHorizontalLineRepresentation(self):
        '''returns a list of lists that represent the maze's horizontal lines. Each list is a list of integers,
           each integer represents alternatingly a block of wall, or a block of empty space, from left to 
           right, with the integer being that wall/white-space's length in rooms. The final integer is a 0 
           or 1 representing whether (for 0) the first integer represent a wall or (for 1) white-space.'''
        
        lineRepresentation = []

        for line in self.lineRepresentation["horizontal"]:
            lineRepresentation.append(line.copy())
            
        return lineRepresentation

    
    def getVerticalLineRepresentation(self):
        '''returns a list of lists that represent the maze's vertical lines. Each list is a list of integers,
           each integer represents alternatingly a block of wall, or a block of empty space, from bottom to 
           top, with the integer being that wall/white-space's length in rooms. The final integer is a 0 
           or 1 representing whether (for 0) the first integer represent a wall or (for 1) white-space.'''
        
        lineRepresentation = []

        for line in self.lineRepresentation["vertical"]:
            lineRepresentation.append(line.copy())

        return lineRepresentation
    
    def getHeight(self):
        '''returns an integer equal to the height of the maze in number of rooms'''
        return self.height
    
    def getWidth(self):
        '''returns an integer equal to the width of the maze in number of rooms'''
        return self.width

    
    

if __name__ == '__main__':
    with open('MazeObjects/SmallMaze.json', 'r') as mazeFile:
        mazeData = json.load(mazeFile)

    testMaze = Maze(mazeData)
    graph = testMaze.mazeGraph
    for i in range(graph.getOrder()):
        print(i, ':', graph.getNodeAdjacencyListAsIndexes(i))