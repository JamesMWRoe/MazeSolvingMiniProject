from PySide6 import QtWidgets
import Maze
import Canvas
from SearchFiles import AStar
import json

class MazeWindow:
    '''This class constructs a window which contains a canvas on which a maze is drawn and a search algorthm
       is animated searching through said maze, as well as a series of buttons which can be used to playthrough
       this animation.'''
    
    def __init__(self, maze, pathTimeline):
        self.playButton = QtWidgets.QPushButton('play')
        self.pauseButton = QtWidgets.QPushButton('pause')
        self.nextFrameButton = QtWidgets.QPushButton('next frame')
        self.previousFrameButton = QtWidgets.QPushButton('previous frame')


        buttonLayout = QtWidgets.QHBoxLayout()

        buttonLayout.addWidget(self.previousFrameButton)
        buttonLayout.addWidget(self.playButton)
        buttonLayout.addWidget(self.pauseButton)
        buttonLayout.addWidget(self.nextFrameButton)

        self.widget = QtWidgets.QWidget()
        self.mazeCanvas = Canvas.MazeCanvas(maze, pathTimeline)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.mazeCanvas)
        self.layout.addLayout(buttonLayout)
        self.widget.setLayout(self.layout)
        self.widget.show()
        self.playButton.pressed.connect(self.mazeCanvas.animateSearchStart)
        self.pauseButton.pressed.connect(self.mazeCanvas.animateSearchPause)
        self.nextFrameButton.pressed.connect(self.mazeCanvas.animateSearchNextFrame)
        self.previousFrameButton.pressed.connect(self.mazeCanvas.animateSearchPreviousFrame)

    def Show(self):
        self.widget.show()
        
    def Hide(self):
        self.widget.hide()


if __name__ == '__main__':

    with open('MazeObjects/HamptonCourt.json', 'r') as mazeFile:
        mazeInfo = json.load(mazeFile)

    testMaze = Maze.Maze(mazeInfo)
    testSearch =  AStar.search(testMaze)
    app = QtWidgets.QApplication()
    testWidget = MazeWindow(testMaze, testSearch)
    testWidget.Show()
    app.exec()

