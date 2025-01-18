from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QPushButton, QDesktopWidget
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle("Belajar PyQt5")

        # Center the main window on the screen
        cwa = self.frameGeometry()  # Get the current geometry of the main window
        cpc = QDesktopWidget().availableGeometry().center()  # Center point of the screen
        cwa.moveCenter(cpc)
        self.move(cwa.topLeft())

        self.setFixedSize(500, 500)  # Prevent resizing; maximize icon will disappear automatically
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
