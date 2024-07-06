from PySide6 import QtWidgets, QtGui
import PanelFactory

class SelectionWindow:
    '''This class constructs a window that holds a series of panels for selecting one of a collection of 
       objects. As an example, it can be used to choose a single maze for a selection of mazes.'''
    def __init__(self, informationDictionary, function):
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Maze Search")
        
        self.function = function
        self.panelList = []
        self.layout = QtWidgets.QHBoxLayout()
        self.SetupLayout(informationDictionary)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(self.window)
        self.scrollArea.setMinimumHeight(390)
        self.scrollArea.setMaximumHeight(390)
    
    def SetupLayout(self, informationDictionary):
        '''sets the layout of the window'''
        self.SetupPanels(informationDictionary)
        self.window.setLayout(self.layout)
    
    def SetupPanels(self, informationDictionary):
        '''A method that creates a panel for each key value pair within the information Dictionary, 
           the key is passed to the panel for it to use. it then connects the function property to 
           each of these panels and finally adds these panels to the layout.'''
        
        for name in informationDictionary:
            information = informationDictionary[name]
            print (information)
            print(type(information))
            panel = PanelFactory.BuildPanelFromInformation(information)
            panel.ConnectFunction(self.function)
            self.panelList.append(panel)
            self.layout.addWidget(panel)
            
    
    def SetupReturnPanel(self, returnFunction, windowToReturnTo):
        '''UNDER CONSTRUCTION.  Can be called to create a singular panel that calls the function returnFunction
           with the parameter windowToReturnTo. The intention of this panel is to allow users of the app to return
           to previous windows to change their decisions.'''
        returnPanel = PanelFactory.Panel('return', windowToReturnTo)
        returnPanel.ConnectFunction(returnFunction)
        self.panelList.insert(0, returnPanel)
        self.layout.addWidget(returnPanel)

    def Show(self):
        self.scrollArea.show()

    def Hide(self):
        self.scrollArea.hide()


    
if __name__ == '__main__':
    app = QtWidgets.QApplication()

    testDictionary = {"test1": 1, "test2": 2, "test3": "C:\\Projects\\UniFiles\\UniFiles\\Intro to Programming\\MiniProject\\MazeObjects\\EmptyMaze.json"}
    def TestFunction(arg):
        print(arg)
    
    testWindow = SelectionWindow(testDictionary, TestFunction)
    testWindow.scrollArea.show()

    app.exec()