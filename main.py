import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Yellow Circles')
        self.setGeometry(100, 100, 800, 600)

        self.button = QPushButton('Add Circle', self)
        self.button.clicked.connect(self.add_circle)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))  # Yellow color
        for circle in self.circles:
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = CircleWidget()
    mainWin.show()
    sys.exit(app.exec_())
