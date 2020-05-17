from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QFileIconProvider, QProgressBar, QLineEdit


class Q(QWidget):


    def __init__(self):

        QWidget.__init__(self)
        mainWidget = QWidget()
        mainWidget.setFixedSize(400,300)
        self.setWindowTitle("IHM")
        mainWidget.setWindowIcon(self.icon)

        self.icon = QFileIconProvider('https://drive.google.com/file/d/1rRc9g8vKTRm5GZGAh68T0Izv2kwM2A7l/view')

        self.layout = QVBoxLayout()

        self.label = QLabel("Label")
        self.layout.setAlignement(self.label)
        self.ProgressBar = QProgressBar()
        self.ProgressBar.setvalue(3)
        self.LineEdit = QLineEdit()
        self.button = QPushButton()
        self.button.setToolPip("Hello")



        self.layout.addwidget(self.icon)
        self.layout.addwidget(self.label)
        self.layout.addwidget(self.bar)
        self.layout.addwidget(self.LineEdit)
        self.layout.addwidget(self.button)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    win = Q()
    win.show()
    app.exec_()








