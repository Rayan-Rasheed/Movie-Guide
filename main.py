import sys
import os
from advance_search import Ui_Dialog
from ui_interface4 import *
#from advanced_search import *
#from scrapping_interface4 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtGui import (QColor)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.uic import loadUi
#from PySide2.QtGui import (QColor)

#from Custom_Widgets.Widgets import *
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))

        self.ui.Card1.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card2.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card3.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card4.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.frame_3.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.label_7.setGraphicsEffect(self.shadow)

        #self.ui.menuBtn.mousePressEvent()
        self.ui.menuBtn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.accountBtn.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.btnFilters.clicked.connect(lambda: self.SildeFilters())
        self.ui.btnScrapping.clicked.connect(lambda: self.GoToScrappingPage())
        self.ui.btnAdvanced_Search.clicked.connect(lambda: self.OpenAdvanced_Search())
        self.show()
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
    def OpenAdvanced_Search(self):
        dia=QtWidgets.QDialog()
        dia.ui=Ui_Dialog()
        dia.ui.setupUi(dia)
        dia.exec()
        #dia.show()

        #msg=QMessageBox()
        #msg.setWindowTitle("Search")
        
        #x=msg.exec()
        #self.window = QtWidgets.QMainWindow()
        #self.ui=Ui_otherWindow()
        #self.ui.setupUi(self.window)
        #self.ui.btnClose.clicked.connect(lambda: self.closeAdvaced_Search())
        #self.window.show()
    def closeAdvaced_Search(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        
        #self.show()
    def GoToScrappingPage(self):
        Scrappage=Scrapping()
        widget=QtWidgets.QStackedWidget()
        widget.addWidget(Scrappage)
        widget.show()

    def slideLeftMenu(self):
        width=self.ui.frame_8.width()
        if(width==0):
            newWidth=200
            self.ui.menuBtn.setIcon(QtGui.QIcon(u":/blackicons/Graphics/featherBlack/chevron-left.svg"))
        else:
            newWidth=0
            self.ui.menuBtn.setIcon(QtGui.QIcon(u":/blackicons/Graphics/featherBlack/align-left.svg"))
        self.animation = QPropertyAnimation(self.ui.frame_8, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def SlideRightMenu(self):
        width=self.ui.frame_12.width()
        if(width==0):
            newWidth=200
        else:
            newWidth=0
        self.animation = QPropertyAnimation(self.ui.frame_12, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    def SildeFilters(self):
        height=self.ui.frameFilters.height()
        if(height==0):
            newHeight=120
        else:
            newHeight=0
        self.animation=QPropertyAnimation(self.ui.frameFilters, b"maximumHeight")
        self.animation.setDuration(300)
        self.animation.setStartValue(height)
        self.animation.setEndValue(newHeight)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


class Scrapping(QMainWindow):
    def __init__(self):
        super(Scrapping, self).__init__()
        loadUi("Scrapping.ui",self)
        #QMainWindow.__init__(self)
        #self.ui=Ui_MainWindow()
        #self.ui.setupUi(self)
        #self.btnHome.clicked.connect(lambda: self.OpenDesignPage())
    
    def OpenDesignPage(self):
        pass

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())