# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from PyQt5.QtCore import QObject, pyqtSignal
from Python_Mini_Proj.GUI.homescreen2 import Ui_HomeScreen


class Ui_RedirectWindow(QObject):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow  # Store MainWindow as an attribute
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1084, 818)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 60, 821, 691))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(390, 110, 361, 421))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:40px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 411, 531))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 122, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(430, 150, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 240, 291, 51))
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,255,56);\n"
"padding-left:10px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 310, 291, 51))
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,255,56);\n"
"padding-left:10px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  # Set echo mode to Password
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.clicked.connect(self.login)
        self.pushButton.setGeometry(QtCore.QRect(490, 390, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    background-color: rgba(90, 0, 10, 255);\n"
"    color: rgba(255, 255, 255, 200);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(65, 78, 92, 255); \n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: rgba(105, 118, 132, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(480, 460, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(227, 8, 48, 0.8);")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(60, 50, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(70, 150, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(255,255,255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(80, 250, 231, 231))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(100)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255,255,255);")
        self.label_7.setObjectName("label_7")
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect( blurRadius=25, xOffset=0, yOffset=0 ))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.pushButton.setText(_translate("MainWindow", "Verify"))
        self.label_4.setText(_translate("MainWindow", "Don\'t Have an Account?"))
        self.label_5.setText(_translate("MainWindow", "Hello There!"))
        self.label_6.setText(_translate("MainWindow", "Login or Create Account \n"
"to use the\n"
"HandGesture Detector"))
        self.label_7.setText(_translate("MainWindow", "👋"))

    def label_clicked(self, event):
       print('predded on Login')

    def login(self):
        # Check if the text fields are empty
        if self.lineEdit.text().strip() == "" or self.lineEdit_2.text().strip() == "":
            # Display an alert if any of the fields are empty
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please enter both email and password")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        # MySQL Connectivity
        try:
            # Establish Connection
            connection = mysql.connector.connect(
                host="localhost",  # Replace 'your_host' with the actual hostname
                user="root",  # Replace 'your_username' with the actual username
                password="HelloWorld@1234",  # Replace 'your_password' with the actual password
                database="handgesture"
            )

            cursor = connection.cursor()

            query = "SELECT * FROM details WHERE email = %s AND password = %s"
            email = self.lineEdit.text()
            password = self.lineEdit_2.text()
            cursor.execute(query, (email, password))

            # Sample Verification
            if cursor.fetchone() is not None:
                print("Login Successful")
                self.redirect_to_new_page()

            else:
                # Display an alert
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Invalid email or Password")
                msg.setWindowTitle("Error")
                msg.exec_()
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
        except mysql.connector.Error as error:
            print("Failed to connect to MySQL: {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def redirect_to_new_page(self):
        self.window = Ui_HomeScreen()  # Create an instance of Ui_HomeScreen2
        self.window.show()  # Show the Ui_HomeScreen2 window
        self.MainWindow.close()
#import sys
#app = QtWidgets.QApplication(sys.argv)
#RedirectWindow = QtWidgets.QMainWindow()
#ui = Ui_RedirectWindow()
#ui.setupUi(RedirectWindow)
#ui.pushButton.clicked.connect(ui.login)
#RedirectWindow.show()
#sys.exit(app.exec_())
