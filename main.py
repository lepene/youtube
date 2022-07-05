from youtube_gui import F1
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication()
    win1 = F1()
    win1.show()
    app.exec()

