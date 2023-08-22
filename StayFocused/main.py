import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from home import Home
from pomo_focus import PomoFocus

#######
#Style
NAV_BAR_BUTTON_STYLE = '''background-color: white;
padding: 15px;
font-size: 20px;
border-top-left-radius: 30px;
text-align: left'''
#######



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("styles/main.ui", self)

        # Pages instances
        self.home = Home(self)
        self.pomo_focus = PomoFocus(self) 


        # signals related
        self.buttons = [
                        self.homeButton,
                        self.pomoFocusButton,
                        self.libraryButton,
                        self.reportsButton,
                        self.settingsButton
                    ]
        
        for button in self.buttons:
            button.clicked.connect(self.nav_bar_buttons)



        

    def nav_bar_buttons(self):
        sender = self.sender()
        if sender == self.buttons[0]: self.pagesStackedWidget.setCurrentIndex(0)
        if sender == self.buttons[1]: self.pagesStackedWidget.setCurrentIndex(1)
        if sender == self.buttons[2]: self.pagesStackedWidget.setCurrentIndex(2)
        if sender == self.buttons[3]: self.pagesStackedWidget.setCurrentIndex(3)

        # Style Button
        for button in self.buttons:
            if button is sender:
                button.setStyleSheet(NAV_BAR_BUTTON_STYLE)
            else:
                button.setStyleSheet("")


app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("Stay Focused")
window.show()
sys.exit(app.exec_())