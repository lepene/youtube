from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QListView


class F1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube")
        main_layout = QVBoxLayout(self)
        icons_layout = QHBoxLayout()

        for i in range(10):
            btn = QPushButton(f"{str(i)}")
            icons_layout.addWidget(btn)
        main_layout.addLayout(icons_layout)


app = QApplication()
f1 = F1()
f1.show()
app.exec()
