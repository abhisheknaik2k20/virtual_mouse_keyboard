from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QTimer
import subprocess

class Ui_HomeScreen(QtWidgets.QMainWindow):
    flag = 0
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("background:transparent;")
        self.draggable = False
        self.offset = QPoint()
        self.setupUi()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_subprocess_status)
        self.timer.start(1000)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            x = event.globalX() - self.offset.x()
            y = event.globalY() - self.offset.y()
            self.move(x, y)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint()
        else:
            super().mouseReleaseEvent(event)

    def setupUi(self):
        self.setObjectName("HomeScreen")
        self.resize(190, 573)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame = QtWidgets.QWidget(self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(30, 0, 301, 521))
        self.Frame.setStyleSheet("background-color:rgba(18, 210, 145, 0.8);\n"
                                  "border-radius:100px;")
        self.Frame.setObjectName("Frame")
        self.pushButton = QtWidgets.QPushButton(self.Frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 121, 131))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:50px;\n"
                                       "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 180, 121, 131))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius:50px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 320, 121, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius:50px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 190, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        # Connect button signals
        self.pushButton.clicked.connect(self.handgesture_detection)
        self.pushButton_2.clicked.connect(self.virtual_mode)
        self.pushButton_3.clicked.connect(self.presentation_mode)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("HomeScreen", "MainWindow"))
        self.pushButton.setText(_translate("HomeScreen", "🖱️"))
        self.pushButton_2.setText(_translate("HomeScreen", "⌨️"))
        self.pushButton_3.setText(_translate("HomeScreen", "Hand\n""Gestures"))
    def handgesture_detection(self):
        self.terminate_subprocess()
        script_path = "D:\python\Python_Mini_Proj\VMouse.py"
        self.handgesture_process = subprocess.Popen(["python", script_path])

    def virtual_mode(self):
        Ui_HomeScreen.flag=0
        self.terminate_subprocess()
        script_path = "D:\python\Python_Mini_Proj\VKeybard.py"
        self.virtual_process = subprocess.Popen(["python", script_path])
        return_code = self.virtual_process.poll()
        if return_code is None:
            print("Virtual Mode started successfully")
        else:
            print("Virtual Mode failed to start")
    def presentation_mode(self):
        self.terminate_subprocess()
        script_path = "D:\python\Python_Mini_Proj\hand_gesture_detection.py"
        self.presentation_prcoess= subprocess.Popen(["python", script_path])

    def terminate_subprocess(self):
        if hasattr(self, 'handgesture_process'):
            self.handgesture_process.terminate()
        if hasattr(self, 'virtual_process'):
            self.virtual_process.terminate()
        if hasattr(self, 'presentation_prcoess'):
            self.virtual_process.terminate()


    def check_subprocess_status(self):
        if hasattr(self, 'handgesture_process'):
            return_code = self.handgesture_process.poll()
            if return_code is not None:
                print(f"Handgesture subprocess terminated with return code: {return_code}")
                if return_code != 0:
                    print("Handgesture subprocess terminated unexpectedly")

        if hasattr(self, 'virtual_process'):
            return_code = self.virtual_process.poll()
            if return_code is not None:
                if Ui_HomeScreen.flag==0:
                    Ui_HomeScreen.flag+=1
                    script_path = "D:\python\Python_Mini_Proj\VMouse.py"
                    self.handgesture_process = subprocess.Popen(["python", script_path])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = Ui_HomeScreen()
    home.show()
    sys.exit(app.exec_())