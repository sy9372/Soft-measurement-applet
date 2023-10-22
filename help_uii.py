
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QIcon
from PyQt5.QtCore import QSize
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent
import sys
import os

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)
logo_path = get_resource_path(os.path.join('resources', 'helps.jpeg'))

class helpui(QWidget):
    def __init__(self):
        super(helpui, self).__init__()
        self.setWindowTitle('帮助文档')
        self.resize(780, 800)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.topFiller = QWidget()
        self.topFiller.setFixedSize(760, 47287)
        self.label3 = QLabel(self.topFiller)
        self.label3.setFixedSize(760, 47287)
        self.label3.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(logo_path)
        scaredPixmap = pixmap.scaled(QSize(760, 47287), aspectRatioMode=Qt.IgnoreAspectRatio)
        self.label3.setScaledContents(True)
        self.label3.setPixmap(scaredPixmap)

        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)
        self.hSb = self.scroll.verticalScrollBar()

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label3)
        self.topFiller.setLayout(vbox1)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.topFiller)
        self.scroll.setLayout(vbox2)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.setLayout(self.vbox)

    def wheelEvent(self, event):
        angle = event.angleDelta()
        y = angle.y()
        self.hSb.setValue(self.hSb.value() - y)

if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    win = helpui()
    win.show()
    sys.exit(app.exec_())
