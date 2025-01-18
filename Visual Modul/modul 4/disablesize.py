from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QPushButton, QDesktopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Label1", self)
        self.label.move(20, 20)
        self.button = QPushButton("Button1", self)
        self.button.move(20, 50)
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Belajar PyQt5")

        # Center the main window on the screen
        cwa = self.frameGeometry()  # Get the current geometry of the main window
        cpc = QDesktopWidget().availableGeometry().center()  # Center point of the screen
        cwa.moveCenter(cpc)
        self.move(cwa.topLeft())

        self.setFixedSize(500, 500)  # Prevent resizing; maximize icon will disappear automatically

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
