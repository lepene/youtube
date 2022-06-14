from PySide6.QtWidgets import QApplication, QWidget


class F1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube")


app = QApplication()
f1 = F1()
f1.show()
app.exec()
