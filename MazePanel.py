from PySide6 import QtWidgets, QtGui, QtCore
import json
import Panel


class MazePanel(Panel.Panel):
    def __init__(self, mazeFileLocation, parent = None):

        with open(mazeFileLocation, 'r') as mazeFile:
            mazeInformation = json.load(mazeFile)

        super().__init__(mazeFileLocation, parent)
        
        
        self.imageLabel = self.SetupImageLabel(mazeInformation["imageLocation"])
        self.nameLabel = self.SetupNameLabel(mazeInformation["name"])
        self.descriptionLabel = self.SetupDescriptionLabel(mazeInformation["description"])
        
        self.layout = self.SetupLayout()

    
    def SetupImageLabel(self, imageLocation):
        imageLabel = QtWidgets.QLabel(self)
        imageLabel.setPixmap(QtGui.QPixmap(imageLocation).scaled(150, 150))
        imageLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        return imageLabel
    
    def SetupNameLabel(self, name):
        nameLabel = QtWidgets.QLabel(self)
        nameLabel.setWordWrap(True)
        nameLabel.setText('Name: ' + name)
        nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        return nameLabel

    def SetupDescriptionLabel(self, description):
        descriptionLabel = QtWidgets.QLabel(self)
        descriptionLabel.setWordWrap(True)
        descriptionLabel.setText('Description: ' + description)
        descriptionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        return descriptionLabel
    
    def SetupLayout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.imageLabel)
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.descriptionLabel)

        return layout

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    def testFunction(text):
        print(text)

    testPanel = MazePanel('MazeObjects/EmptyMaze.json')
    testPanel.ConnectFunction(testFunction)

    testPanel.show()
    app.exec()