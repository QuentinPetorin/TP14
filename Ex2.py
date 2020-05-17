from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QHBoxLayout, QGridLayout, QTextEdit

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")


        self.layout = QGridLayout()
        #self.layout = QHBoxLayout()


        self.label = QLabel("Laissez un commentaire")
        self.text = QTextEdit()
        self.button1 = QPushButton("Success")
        self.button2 = QPushButton("Cancel")
       # layout.addWidget()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()


