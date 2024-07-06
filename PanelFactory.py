from PySide6 import QtWidgets

import Panel
import MazePanel
import SearchPanel

def BuildPanelFromInformation(information):
    '''This function is a factory function for handling the instantiation of panels. It is intended to create
       different panel objects based on the information passed into it.'''
    
    if str(information).endswith('.json'):
        return MazePanel.MazePanel(information)
    elif str(information).startswith('SearchFiles'):
        return SearchPanel.SearchPanel(information)
    else:
        return Panel.Panel(str(information), str(information))

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout()

    mazeInformation = 'C:\\Projects\\UniFiles\\UniFiles\\Intro to Programming\\MiniProject\\MazeObjects\\EmptyMaze.json'
    MazePanel = BuildPanelFromInformation(mazeInformation)

    layout.addWidget(MazePanel)

    searchInformation = 'SearchFiles.AStar'
    searchPanel = BuildPanelFromInformation(searchInformation)

    layout.addWidget(searchPanel)

    layout.update()

    window.setLayout(layout)
    window.show()

    app.exec()