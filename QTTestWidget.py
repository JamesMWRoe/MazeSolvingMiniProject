from PySide6 import QtWidgets, QtGui
import importlib

class TestWidget:
    def __init__(self):
        self.widget = QtWidgets.QWidget()
        imageLable = QtWidgets.QLabel(self.widget)
        imageLable.setPixmap(QtGui.QPixmap('MazeImages/MazeIconPlaceholder.jpg').scaled(150, 150))
        nameLabel = QtWidgets.QLabel(self.widget)
        nameLabel.setText('Name: Maze Icon Test')
        descriptionLabel = QtWidgets.QLabel(self.widget)
        descriptionLabel.setText('An image of a maze \n icon found online for\n the purposes of testing \nthe text in label widgets')
        self.widget.show()
        button = QtWidgets.QPushButton('Test')
        button.pressed.connect(self.testFunc)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(imageLable)
        layout.addWidget(nameLabel)
        layout.addWidget(descriptionLabel)
        layout.addWidget(button)

        self.widget.setLayout(layout)
    
    def testFunc(self):
        importedModule = importlib.import_module('SearchFiles.AStar')
        print(importedModule.name)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    testWidget = TestWidget()
    app.exec()
