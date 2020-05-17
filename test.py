from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QDial
app = QApplication([])
mainWidget = QWidget()



layout = QVBoxLayout()



label = QLabel("Ceci est un QLabel")
button = QPushButton("Ceci est un QPushButton")
dial = QDial()


layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(dial)


mainWidget.setLayout(layout)


mainWidget.setWindowTitle("Ma premiere interface en Qt")
mainWidget.show()
app.exec_()
