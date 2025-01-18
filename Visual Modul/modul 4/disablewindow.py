from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)

        self.button = QPushButton(self)
        self.button.setText("Button")
        self.button.setGeometry(0, 50, 300, 300)

        self.setWindowTitle("Belajar PyQt5")
        
        # Cek ukuran dan posisi layar
        cwc = QDesktopWidget().availableGeometry().center()
        print(cwc)  # Contoh output: PyQt5.QtCore.QPoint(682, 363)
        
        # Memindahkan window ke tengah layar
        cw = self.frameGeometry()
        cw.moveCenter(cwc)
        self.move(cw.topLeft())
        
        # Mengatur agar window tidak bisa di-resize
        self.setFixedSize(500, 500)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
