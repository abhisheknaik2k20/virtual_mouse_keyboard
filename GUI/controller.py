import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Python_Mini_Proj.GUI.signuppage import Ui_Signup
from Python_Mini_Proj.GUI.redirect import Ui_RedirectWindow
from Python_Mini_Proj.GUI.homescreen import Ui_HomeScreen

class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Signup()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_redirect_page)

    def open_redirect_page(self):
        print("Opening redirect page...")
        self.redirect_window = RedirectWindow()
        self.redirect_window.show()
        self.close()

class RedirectWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RedirectWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_home_screen)

    def open_home_screen(self):
        print("Opening home screen...")
        self.home_window = HomeScreen()
        self.home_window.show()
        self.close()

class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomeScreen()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    signup_window = SignupWindow()
    signup_window.show()
    sys.exit(app.exec_())
