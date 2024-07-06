from PySide6 import QtWidgets, QtGui, QtCore
import Maze
import sys
from SearchFiles import AStar
import json

class MazeCanvas(QtWidgets.QWidget):
    '''This class is a subclass of the QT QWidget class. It is a canvas which the maze is drawn onto and 
       is searched through. it takes a maze object and path timeline object as its parameters, which represent
       the maze it draws and the sequence of paths it uses to search through the maze'''

    def __init__(self, maze, pathTimeline):
        super().__init__()
        self.setMinimumSize(300, 300)
        self.maze = maze
        self.pathTimeline = pathTimeline
        self.padding = 10
        self.painter = QtGui.QPainter()

        self.timeFrame = 0
        self.listOfPathCoordinateNodesForTimeline = []
        self.currentPathCoordinates = None

        self.playing = False
        animationTimer = QtCore.QTimer(self)
        animationTimer.timeout.connect(self.animateSearchPlay)
        animationTimer.start(100)
        


    def paintEvent(self, event):
        height = self.size().height()
        width = self.size().width()

        self.painter.begin(self)

        self.pen = QtGui.QPen()
        self.pen.setWidth(6)
        self.pen.setCapStyle(QtCore.Qt.PenCapStyle.SquareCap)
        self.pen.setJoinStyle(QtCore.Qt.PenJoinStyle.MiterJoin)
        self.painter.setPen(self.pen)

        self.drawMaze()
        self.drawSearchPath()
        self.painter.end()
        print('height: ', height)
        print('width: ', width)


    def drawMaze(self):
        '''This method draws the maze, it does this by setting the room size and maze origin 
           and then it draws the horizontal lines of the maze, and then the vertical lines of the maze.'''
        self.setMazeRoomSizeAndMazeOrigin()
        self.drawHorizontalMazeLines()
        self.drawVerticalMazeLines()

    def drawDotsTest(self):
        '''A Test Method to check that the mazeCoordinates property stores the correct values by drawing dots
           at the coordinates stored in mazeCoordinates.'''
        self.painter.drawPoints(self.mazeCoordinates)

    def setMazeRoomSizeAndMazeOrigin(self):
        '''a method that calculates the size each maze room should be, and where the origin should be
           based on the size of the Canvas widget. and then sets the room size and origins to be those values'''
        print('function called')
        screenHeight = self.size().height()
        screenWidth = self.size().width()

        mazeHeight = self.maze.getHeight()
        mazeWidth = self.maze.getWidth()

        screenRatio = screenWidth/screenHeight
        mazeRatio = mazeWidth/mazeHeight

        mazeIsWide = mazeRatio > screenRatio

        if mazeIsWide:

            print('mazeIsWide')
            mazeCanvasWidth = screenWidth -  2*self.padding
            
            paddingY = (screenHeight - (mazeCanvasWidth/mazeRatio))/2

            mazeOriginX = self.padding
            mazeOriginY = paddingY + (mazeCanvasWidth/mazeRatio)

            roomSize = int(mazeCanvasWidth/mazeWidth)

        else:
            
            print('mazeIsTall')
            mazeCanvasHeight = screenHeight - 2*self.padding

            paddingX = (screenWidth - (mazeCanvasHeight*mazeRatio))/2
            
            mazeOriginY = screenHeight - self.padding
            mazeOriginX = paddingX

            roomSize = int(mazeCanvasHeight/mazeHeight)
        
        print('room size:', roomSize)
        self.roomSize = roomSize
        self.mazeOrigin = QtCore.QPoint(mazeOriginX, mazeOriginY)
        self.horizontalRoomSize = QtCore.QPoint(self.roomSize, 0)
        self.verticalRoomSize = QtCore.QPoint(0, self.roomSize)

        self.mazeCoordinates = QtCore.QPointList()

        for i in range(self.maze.mazeGraph.getOrder()):
            x, y = self.maze.mazeGraph.getNodeCoordinates(i)
            xCoordinate = mazeOriginX + roomSize/2 + roomSize*x
            yCoordinate = mazeOriginY - roomSize/2 - roomSize*y
            self.mazeCoordinates.append(QtCore.QPoint(xCoordinate, yCoordinate))


    def drawHorizontalMazeLines(self):
        '''This method draws the horizontal maze lines on the canvas, 
        by getting each line's mazeOrigin and then drawing that line'''

        horizontalLineRepresentation = self.maze.getHorizontalLineRepresentation()

        lineStartPoint = self.getMazeOrigin()

        for line in horizontalLineRepresentation:
            self.drawHorizontalLine(line, lineStartPoint)
            lineStartPoint = self.getNextHorizontalLineStartPoint(lineStartPoint)


    def drawVerticalMazeLines(self):
        '''This method draws the vertical maze lines on the canvas, 
        by getting each line's mazeOrigin and then drawing that line'''

        verticalLineRepresentation = self.maze.getVerticalLineRepresentation()
        
        lineStartPoint = self.getMazeOrigin()

        for line in verticalLineRepresentation:
            self.drawVerticalLine(line, lineStartPoint)
            lineStartPoint = self.getNextVerticalLineStartPoint(lineStartPoint)
            

    def getMazeOrigin(self):
        '''returns the coordinate of the bottom left pixel of the maze drawing '''

        return QtCore.QPoint(self.mazeOrigin)

    def drawHorizontalLine(self, line, lineStartPoint):
        '''draws a single horizontal line of the maze.'''

        currentPoint = lineStartPoint
        segmentIsSolid = not line.pop()
        for segment in line:
            nextPoint = currentPoint + segment*self.horizontalRoomSize

            if segmentIsSolid: self.painter.drawLine(currentPoint, nextPoint)

            segmentIsSolid = not segmentIsSolid
            currentPoint = nextPoint


    def getNextHorizontalLineStartPoint(self, currentLineStartPoint):
        '''A method which returns where the next horizontal maze line should start based
           on the start point of the current horizontal maze line'''
        
        return currentLineStartPoint - self.verticalRoomSize


    def drawVerticalLine(self, line, lineStartPoint):
        '''draws a single vertical line of the maze.'''

        currentPoint = lineStartPoint
        segmentIsSolid = not line.pop()
        for segment in line:
            nextPoint = currentPoint - segment*self.verticalRoomSize

            if segmentIsSolid: self.painter.drawLine(currentPoint, nextPoint)

            segmentIsSolid = not segmentIsSolid
            currentPoint = nextPoint
    
    def getNextVerticalLineStartPoint(self, currentLineStartPoint):
        '''A method which returns where the next vertical maze line should start based
           on the start point of the current vertical maze line'''
        
        return currentLineStartPoint + self.horizontalRoomSize
    
    def drawSearchPath(self):
        '''draws the search path at the current timeframe in the timeline. Draws the search path in blue
           unless the search path is a valid path from entrance to exit in which case it is drawn in red.'''
        path = self.pathTimeline.getPathAtStep(self.timeFrame)
        nodePath = []
        for node in path:
            nodePath.append(self.mazeCoordinates[node.getIndex()])    
        print(self.timeFrame)
        self.pen.setColor("blue")
        self.painter.setPen(self.pen)

        if path in self.pathTimeline.getValidPaths():
            self.pen.setColor("red")
            self.painter.setPen(self.pen)

        self.painter.drawPolyline(nodePath)
        

        

    def animateSearchPlay(self):
        '''a function which increments the time frame of the canvas by one whenerver it's called to allow for
           the animation to play. It only increments the time frame if the canvas has been set to play. It also
           stops the animator from playing if it has reached the end of the animation.'''
        
        if not self.playing:
            return
        
        self.timeFrame += 1
        if self.timeFrame >= self.pathTimeline.getTotalSteps():
            self.timeFrame -= 1
            self.playing = False

        print('timeframe is currently', self.timeFrame)
        self.update()

    
    def animateSearchStart(self):
        '''Starts the animator from the current timeframe. If the animator is at the end, calling
           this function starts the animation fro the beginning.'''
        self.playing = True

        if self.timeFrame == self.pathTimeline.getTotalSteps() - 1:
            self.timeFrame = 0


    def animateSearchPause(self):
        '''Pause the animation'''
        self.playing = False
    
    def animateSearchNextFrame(self):
        '''causes the animation to move onto the next frame by incrementing the timeframe by one
           and updating the canvas.'''
        self.timeFrame += 1
        if self.timeFrame >= self.pathTimeline.getTotalSteps():
            self.timeFrame = 0

        self.playing = False
        self.update()
    
    def animateSearchPreviousFrame(self):
        '''causes the animation to move onto the next frame by decrementing the timeframe by one
           and updating the canvas.'''
        self.timeFrame -= 1
        if self.timeFrame < 0:
            self.timeFrame = self.pathTimeline.getTotalSteps() - 1

        self.playing = False
        self.update()
    
    def drawValidPath(self):
        '''For Testing purposes. calling this function draws the first valid path found by the search
           algorithm'''
        path = self.pathTimeline.getFirstValidPath()
        pathList = []
        for node in path:
            pathList.append(self.mazeCoordinates[node.getName()])
        self.pen.setColor("blue")
        self.painter.setPen(self.pen)
        self.painter.drawPolyline(pathList)

        

if __name__ == '__main__':

    with open("MazeObjects/CheveningHouse.json", 'r') as mazeFile:
        mazeObject = json.load(mazeFile)

    maze = Maze.Maze(mazeObject)
    pathTimeline =  AStar.search(maze)
    app = QtWidgets.QApplication(sys.argv)
    window = MazeCanvas(maze, pathTimeline)
    window.show()

    app.exec()