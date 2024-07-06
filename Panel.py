from PySide6 import QtWidgets

class Panel(QtWidgets.QPushButton):
    '''This class represents a panel which can be clicked on to carry out the function connected with it.
       The panel can essenitally be thought of as a giant button, that holds information about what it carries
       out. This panel has limited formatting but is meant to be a parent for more interesting panel classes.'''
    def __init__(self, text, parent = None):
        super().__init__(parent)

        self.setMinimumSize(200, 350)
        self.setMaximumSize(200, 350)
        self.text = text
        self.connectedFunction = self.empty
        self.pressed.connect(self.onPress)

        self.layout = QtWidgets.QVBoxLayout()

        

    def empty(self):
        '''An empty function used as a placeholder before a function is connected to the panel.'''
        pass

    def ConnectFunction(self, function):
        '''connects a function to the panel, so that when the panel is clicked on the function is called'''
        self.connectedFunction = function
        
    def onPress(self):
        '''this function is called whenever the button contained within the panel is pressed. 
           It calls the function connected to this panel passing the function the panel's text property'''
        self.connectedFunction(self.text)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout()
    def testFunction(text):
        print(text)


    testPanel = Panel('TEST', 'test')
    testPanel.ConnectFunction(testFunction)
    layout.addWidget(testPanel)
    window.setLayout(layout)

    window.show()
    app.exec()