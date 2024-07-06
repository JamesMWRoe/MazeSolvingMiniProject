from PySide6 import QtWidgets
import sys
import SelectionWindow
import os
import json
import Maze
import MazeWindow
import importlib


class Main:
    '''The main class from which the application runs.'''
    def __init__(self):
        self.mainWindow = None
        self.maze = None
        self.pathTimeline = None

        self.app = QtWidgets.QApplication(sys.argv)

        self.mazeDictionary = self.CreateMazeDictionaryFromJSonFiles()
        self.searchDictionary = self.CreateSearchDictionaryFromPythonFiles()
        self.windowDictionary = self.CreateWindowDictionary()

        #self.windowDictionary["search"].SetupReturnPanel(self.SelectMainWindow, self.windowDictionary["maze"])
        self.SelectMainWindow(self.windowDictionary["maze"])
        
        self.Main()
    
    def Main(self):
        '''executes the application '''

        self.app.exec()
    
    def CreateMazeDictionaryFromJSonFiles(self):
        '''Creates a dictionary containing key value pairs where the key is the name of a maze,
            and the value is a string containing the location of a json file which itself contains
            the information about this maze.'''

        currentDirectory = os.getcwd()
        mazeFileDirectory = currentDirectory + '\\MazeObjects'
        mazeFileList = os.listdir(mazeFileDirectory)

        mazeDictionary = {}

        for jsonFile in mazeFileList:
            fileLocation = mazeFileDirectory + '\\' + jsonFile
            with open(fileLocation, 'r') as file:
                fileData = json.load(file)
                mazeDictionary[fileData["name"]] = fileLocation
        
        return mazeDictionary
    
    def CreateSearchDictionaryFromPythonFiles(self):
        '''Creates a dictionary containing key value pairs where the key is the name of a search algorithm,
           and the value is a reference to a module containing the implementation of the search algorithm'''
        
        currentDirectory = os.getcwd()
        searchFileDirectory = currentDirectory + '\\SearchFiles'
        searchFileList = os.listdir(searchFileDirectory)

        searchDictionary = {}
        print(searchFileList)

        for file in searchFileList:
            if file[0] == '_':
                continue
            
            splitFile = file.split('.')

            if splitFile[1] == 'py':
                pythonModuleName = 'SearchFiles.' + splitFile[0]
                pythonModule = importlib.import_module(pythonModuleName)
                searchDictionary[pythonModule.name] = pythonModuleName

        return searchDictionary
    
    def CreateWindowDictionary(self):
        '''Creates a dictionary which stores the different windows that are opened and closed within the app'''

        windowDictionary = {}

        windowDictionary["maze"] = SelectionWindow.SelectionWindow(self.mazeDictionary, self.SelectMaze)
        windowDictionary["search"] = SelectionWindow.SelectionWindow(self.searchDictionary, self.SelectSearch)

        return windowDictionary
    
    def SelectMainWindow(self, newWindow):
        '''Takes as a paramater a window and hides the previously showing window, and then shows the newly
           selected window.'''
        
        if self.mainWindow != None:
            self.mainWindow.Hide()

        self.mainWindow = newWindow
        self.mainWindow.Show()


    def SelectMaze(self, maze):
        '''This method generates a maze and sets it to this class's maze,
           and then sets the main window to be the search selection window.'''
        
        with open(maze, 'r') as mazeFile:
            mazeData = json.load(mazeFile)

        self.maze = Maze.Maze(mazeData)

        self.SelectMainWindow(self.windowDictionary["search"])

    def SelectSearch(self, search):
        '''This method generates a timeline of the paths that were traversed by the given search method,
           to find the path from the start to the end of the maze, it then calls the drawOnCanvas method'''
        
        print(search)
        searchModule = importlib.import_module(search)
        self.pathTimeline = searchModule.search(self.maze)
        self.DrawCanvas()
    
    def DrawCanvas(self):
        '''This method generates a window which contains the drawing of the maze,
           and sets it to be the main window'''
        
        mazeWindow = MazeWindow.MazeWindow(self.maze, self.pathTimeline)
        self.SelectMainWindow(mazeWindow)

if __name__ == '__main__':
    app = Main()