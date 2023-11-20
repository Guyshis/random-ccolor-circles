import io

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>886</width>
    <height>753</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>310</x>
     <y>20</y>
     <width>221</width>
     <height>131</height>
    </rect>
   </property>
   <property name="text">
    <string>PushButton</string>
   </property>
  </widget>
  <widget class="QWidget" name="centralwidget" native="true">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>230</y>
     <width>641</width>
     <height>231</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.pushButton.setFixedSize(100, 100)
        self.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        canvas = QPixmap(850, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        x, y = [randint(10, 750) for i in range(2)]
        w = randint(10, 100)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, w)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
