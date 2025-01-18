from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        btn1 = QPushButton("Btn 1")
        btn2 = QPushButton("Btn 2")
        btn3 = QPushButton("Btn 3")
        btn4 = QPushButton("Btn 4")

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)

        self.setLayout(layout)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()