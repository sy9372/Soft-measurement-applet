
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject
from main import *
from mlp import MLPS
from PIL import Image
import ast
import Logger as l
import time
import sys
import os
import background
import shutil

class Signal(QObject):
    text_update = pyqtSignal(str)
    def write(self, text):
        self.text_update.emit(str(text))
        QApplication.processEvents()

    def flush(self):
        pass

class mlpui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        sys.stdout = Signal()
        sys.stdout.text_update.connect(self.updatetext)

    def updatetext(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(808, 579)
        Form.setFixedSize(808, 579)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        Form.setFont(font)
        Form.setStyleSheet("background-image:url(:/picture1.png)")

        self.input_numBox = QtWidgets.QSpinBox(Form)
        self.input_numBox.setGeometry(QtCore.QRect(170, 70, 70, 21))
        self.input_numBox.setObjectName("input_numBox")

        self.output_numBox_2 = QtWidgets.QSpinBox(Form)
        self.output_numBox_2.setGeometry(QtCore.QRect(170, 100, 70, 21))
        self.output_numBox_2.setObjectName("output_numBox_2")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 127);\n" "")
        self.label_5.setObjectName("label_5")

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 40, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(140, 330, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 85, 0);\n" "")
        self.label_15.setObjectName("label_15")

        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(570, 200, 61, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 170, 127);\n" "color: rgb(255, 85, 0);")
        self.label_12.setObjectName("label_12")

        self.shujuji_Button = QtWidgets.QPushButton(Form)
        self.shujuji_Button.setGeometry(QtCore.QRect(40, 250, 241, 23))
        self.shujuji_Button.setText("")
        self.shujuji_Button.setObjectName("shujuji_Button")

        self.iter_lineEdit = QtWidgets.QLineEdit(Form)
        self.iter_lineEdit.setGeometry(QtCore.QRect(170, 130, 71, 21))
        self.iter_lineEdit.setObjectName("iter_lineEdit")

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 360, 321, 192))
        self.textBrowser.setObjectName("textBrowser")

        self.picture = QtWidgets.QLabel(Form)
        self.picture.setGeometry(QtCore.QRect(380, 230, 427, 320))
        self.picture.setMinimumSize(QtCore.QSize(427, 320))
        self.picture.setText("")
        self.picture.setObjectName("picture")

        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 0, 127);\n" "")
        self.label_13.setObjectName("label_13")

        self.run_button = QtWidgets.QPushButton(Form)
        self.run_button.setGeometry(QtCore.QRect(130, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(18)
        self.run_button.setFont(font)
        self.run_button.setStyleSheet("color: rgb(255, 0, 0);\n" "background-color: rgb(85, 170, 255);")
        self.run_button.setObjectName("run_button")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 127);\n" "")
        self.label_6.setObjectName("label_6")

        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(300, 553, 191, 25))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);\n" "background-color: rgb(193, 200, 200);")
        self.label_14.setObjectName("label_14")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(336, 5, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);\n" "background-color: rgb(200, 180, 195);")
        self.label.setObjectName("label")

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(70, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 127);\n" "")
        self.label_7.setObjectName("label_7")

        self.select_button = QtWidgets.QToolButton(Form)
        self.select_button.setGeometry(QtCore.QRect(290, 250, 71, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(14)
        self.select_button.setFont(font)
        self.select_button.setStyleSheet("color: rgb(255, 85, 0);\n" "background-color: rgb(200, 176, 189);")
        self.select_button.setObjectName("select_button")

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(140, 220, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(200, 22, 78);\n" "background-color: rgb(187, 184, 200);")
        self.label_11.setObjectName("label_11")

        self.iter_lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.iter_lineEdit_2.setGeometry(QtCore.QRect(170, 160, 71, 21))
        self.iter_lineEdit_2.setText("")
        self.iter_lineEdit_2.setObjectName("iter_lineEdit_2")

        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(490, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 127);\n" "")
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(490, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(0, 0, 127);\n" "")
        self.label_18.setObjectName("label_18")

        self.mx_lineEdit = QtWidgets.QLineEdit(Form)
        self.mx_lineEdit.setGeometry(QtCore.QRect(600, 80, 81, 20))
        self.mx_lineEdit.setObjectName("mx_lineEdit")

        self.score_lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.score_lineEdit_3.setGeometry(QtCore.QRect(600, 140, 81, 20))
        self.score_lineEdit_3.setObjectName("score_lineEdit_3")

        self.r_lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.r_lineEdit_2.setGeometry(QtCore.QRect(600, 110, 81, 20))
        self.r_lineEdit_2.setObjectName("r_lineEdit_2")

        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(470, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 127);\n" "")
        self.label_16.setObjectName("label_16")

        self.select_button.clicked.connect(self.select1)
        self.run_button.clicked.connect(self.select3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def select1(self):
        self.fileName1, self.filetype = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./")
        self.shujuji_Button.setText(self.fileName1)
        self.ljshurumoxingquanzhong = self.fileName1
        print(self.fileName1)

    def select3(self):
        name2 = os.path.basename(self.fileName1)
        name3 = name2.split('.')[0]
        t = time.strftime("-%Y%m%d-%H%M%S", time.localtime())

        def get_desk_p():
            return os.path.join(os.path.expanduser('~'), "Desktop")
        path1 = get_desk_p() + "/Model"
        if not os.path.exists(path1):
            os.makedirs(path1)

        filenames = name3 + '+mlp' + t
        l.sys.stdout = l.Logger(path1+f'./{filenames}.txt')
        print(f"输入个数：{self.input_numBox.value()}")
        print(f"输出个数：{self.output_numBox_2.value()}")
        print(f"迭代次数：{self.iter_lineEdit.text()}")
        print(f"隐层层数及数量：{self.iter_lineEdit_2.text()}")
        list1 = ast.literal_eval(self.iter_lineEdit_2.text())
        a, b, score = MLPS(self.fileName1, list1, int(self.iter_lineEdit.text()))
        self.mx_lineEdit.setText(str(a))
        self.r_lineEdit_2.setText(str(b))
        self.score_lineEdit_3.setText(str(int(score)))
        img = Image.open("picture/mlp_figure.png")
        img.resize((427, 320))
        self.picture.setPixmap(QtGui.QPixmap("picture/mlp_figure.png"))
        self.picture.setScaledContents(True)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MLP"))
        self.label_5.setText(_translate("Form", "  输入个数："))
        self.label_15.setText(_translate("Form", "训练结果"))
        self.label_12.setText(_translate("Form", "拟合曲线"))
        self.label_13.setText(_translate("Form", "隐层层数及数量："))
        self.run_button.setText(_translate("Form", "开始"))
        self.label_6.setText(_translate("Form", "  输出个数："))
        self.label_14.setText(_translate("Form", "    ©华东理工大学版权所有"))
        self.label.setText(_translate("Form", "  MLP算法"))
        self.label_7.setText(_translate("Form", "迭代次数："))
        self.select_button.setText(_translate("Form", "选择文件"))
        self.label_11.setText(_translate("Form", "数据集"))
        self.label_17.setText(_translate("Form", "     R方："))
        self.label_18.setText(_translate("Form", "  模型得分："))
        self.label_16.setText(_translate("Form", "  最大相对误差："))

if __name__ == "__main__":
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = mlpui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())




