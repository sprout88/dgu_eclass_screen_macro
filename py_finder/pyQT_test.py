import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import os


class MyApp(QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('web.png'))
      self.setGeometry(300, 300, 300, 200)
      self.show()
    
  def initUI(self):
      btn = QPushButton('Quit', self)
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)

      self.setWindowTitle('Quit Button')
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())