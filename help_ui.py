from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPalette, QIcon
from PyQt5.QtCore import QSize, QObject, QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os


def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)
logo_path = get_resource_path(os.path.join('resources', 'helps.png'))



class helpui(QWidget):


    def __init__(self):
        super(helpui, self).__init__()
        self.setWindowTitle('帮助文档')

        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(760, 30100)  #######设置滚动条的尺寸
        self.label3 = QLabel(self.topFiller)
        self.label3.setAlignment(Qt.AlignCenter)  # 设置文本标签居中显示
        self.label3.setScaledContents(True)

        pixmap = QPixmap(logo_path)
        # Qt.KeepAspectRatio设置为等比例缩放
        # Qt.IgnoreAspectRatio为不按比例缩放
        scaredPixmap = pixmap.scaled(QSize(760, 30100), aspectRatioMode=Qt.IgnoreAspectRatio)
        self.label3.setScaledContents(True)
        self.label3.setPixmap(scaredPixmap)

        ##创建一个滚动条
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
    # win.setWindowIcon(QIcon('interface/icon.ico'))
    win.show()
    sys.exit(app.exec_())
