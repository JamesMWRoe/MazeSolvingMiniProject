from PySide6 import QtWidgets, QtCore
import Panel
import importlib

class SearchPanel(Panel.Panel):
    def __init__(self, searchModule, parent = None):
        super().__init__(searchModule, parent)

        search = importlib.import_module(searchModule)

        self.nameLabel = self.SetupNameLabel(search.name)

        self.layout = self.SetupLayout()

    def SetupNameLabel(self, name):
        nameLabel = QtWidgets.QLabel(self)
        nameLabel.setWordWrap(True)
        nameLabel.setText('Name: ' + name)
        nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        return nameLabel
    
    def SetupLayout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.nameLabel)

        return layout

if __name__ == '__main__':
    applicaton = QtWidgets.QApplication()

    searchInformation = 'SearchFiles.AStar'
    searchPanel = SearchPanel(searchInformation)

    def testFunction(text):
        print(text)
    
    searchPanel.ConnectFunction(testFunction)
    searchPanel.show()

    applicaton.exec()
