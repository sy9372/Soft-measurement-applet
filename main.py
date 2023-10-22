
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import background
import sys

class mainui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(820, 562)
        Form.setFixedSize(820, 562)
        Form.setStyleSheet("background-image:url(:/picture1.png)")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 10, 341, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);\n" "background-color: rgb(200, 180, 195);")
        self.label.setObjectName("label")

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(320, 530, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n""background-color: rgb(193, 200, 200);")
        self.label_7.setObjectName("label_7")

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 80, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(355, 160, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(67)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 127);\n""")
        self.label_6.setObjectName("label_6")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 250, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(85, 0, 0);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 250, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(85, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 250, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(85, 0, 0);\n""")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 250, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(85, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(724, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(85, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 320, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(85, 0, 0);")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 320, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(85, 0, 0);")
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 320, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(85, 0, 0);")
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(630, 320, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 170, 127);\n""color: rgb(85, 0, 0);")
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_4.raise_()
        self.label.raise_()
        self.label_7.raise_()
        self.line.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.retranslateUi(Form)

        self.pushButton.clicked.connect(self.mlpzhuan)
        self.pushButton_2.clicked.connect(self.gbdtzhuan)
        self.pushButton_3.clicked.connect(self.knnzhuan)
        self.pushButton_4.clicked.connect(self.rfzhuan)
        self.pushButton_5.clicked.connect(self.helpzhuan)
        self.pushButton_6.clicked.connect(self.adbzhuan)
        self.pushButton_7.clicked.connect(self.bagzhuan)
        self.pushButton_8.clicked.connect(self.hgbrzhuan)
        self.pushButton_9.clicked.connect(self.etzhuan)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据驱动模型开发软件"))
        self.label.setText(_translate("Form", "  数据驱动模型开发软件"))
        self.label_7.setText(_translate("Form", "    ©华东理工大学版权所有"))
        self.label_6.setText(_translate("Form", "算法选择"))
        self.pushButton.setText(_translate("Form", "MLP算法"))
        self.pushButton_2.setText(_translate("Form", "GBDT算法"))
        self.pushButton_3.setText(_translate("Form", "KNN算法"))
        self.pushButton_4.setText(_translate("Form", "RF算法"))
        self.pushButton_5.setText(_translate("Form", "帮助文档"))
        self.pushButton_6.setText(_translate("Form", "AdaBoost算法"))
        self.pushButton_7.setText(_translate("Form", "Bagging算法"))
        self.pushButton_8.setText(_translate("Form", "HGBR算法"))
        self.pushButton_9.setText(_translate("Form", "ET算法"))

    def mlpzhuan (self):
        import mlp_ui
        self.one = mlp_ui.mlpui()
        self.one.show()

    def gbdtzhuan (self):
        import gbdt_uii
        self.two = gbdt_uii.gbdtui()
        self.two.show()

    def knnzhuan (self):
        import knn_ui
        self.three = knn_ui.knnui()
        self.three.show()

    def rfzhuan (self):
        import rf_ui
        self.four = rf_ui.rfui()
        self.four.show()

    def helpzhuan(self):
        import help_uii
        self.five = help_uii.helpui()
        self.five.show()

    def adbzhuan(self):
        import adb_ui
        self.six = adb_ui.adbui()
        self.six.show()

    def bagzhuan(self):
        import bag_ui
        self.seven = bag_ui.bagui()
        self.seven.show()

    def hgbrzhuan(self):
        import hgbr_ui
        self.eight = hgbr_ui.hgbrui()
        self.eight.show()

    def etzhuan(self):
        import et_ui
        self.nine = et_ui.etui()
        self.nine.show()



if __name__ == "__main__":
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = mainui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
