from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        btn1 = QPushButton("Btn 1")
        btn2 = QPushButton("Btn 2")
        btn3 = QPushButton("Btn 3")
        btn4 = QPushButton("Btn 4")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        self.setLayout(layout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()