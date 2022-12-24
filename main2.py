import sys
import os
import pandas as pd
from pandas.api.types import CategoricalDtype
from advance_search import Ui_Dialog
from Stacked_DesignUI import *
#from advanced_search import *
#from scrapping_interface4 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtGui import (QColor)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.uic import loadUi
from searchingAlgorithm import KMPStringSearching
#from PySide2.QtGui import (QColor)
from sortingAlgorithms import(InsertionSort,InsertionSortDesc,SelectionSort,SelectionSortDec,MergeSort,MergeSortDesc,BubbleSort,BubbleSortDesc,HybridMergeSort,HybridMergeSortDesc,RandomizedQuickSort,RandomizedQuickSortDesc,QuickSort,CountingSort,CountingSortDesc,RadixSort,RadixSortDesc,bucketSort,bucketSortDesc,pigeonHoleSort,pigeonHoleSortDecs,PostmanSorting,PostmanSortingDesc,CockTailSorting,CockTailSortingDesc)
#from Custom_Widgets.Widgets import *
import WebScraping as scrap 

class Movie:
    def __init__(self,MovieName,Certificate,Duration,Genre,Rating,Years,Director,Actors,Gross,Votes):
        self.MovieName=MovieName
        self.Certificate=Certificate
        self.Duration=Duration
        self.Genre=Genre
        self.Rating=Rating
        self.Years=Years
        self.Director=Director
        self.Actors=Actors
        self.Gross=Gross
        self.Votes=Votes
class MainWindow(QMainWindow):
    

    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.timeTaken=0
        self.headerCol=0
        
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
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.CardCompletion.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.CardTotalScrapped.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.CardTimeScrapped.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_9.setGraphicsEffect(self.shadow)
        
        #self.ui.menuBtn.mousePressEvent()
        self.ui.cmbSortedBy.activated.connect(lambda:self.sortDataTable(self.ui.cmbAlgorithms.currentIndex(),self.df))
        self.ui.lineEdit.textEdited.connect(lambda: self.SearchTop(self.ui.lineEdit.text()))
        self.ui.menuBtn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.accountBtn.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.btnFilters.clicked.connect(lambda: self.SildeFilters())
        #self.ui.btnScrapping.clicked.connect(lambda: self.GoToScrappingPage())
        self.ui.btnAdvanced_Search.clicked.connect(lambda: self.OpenAdvanced_Search())
        self.ui.btnScrapping.clicked.connect(lambda: self.closeHome())
        self.ui.btnHome.clicked.connect(lambda: self.closeScrapping())
        self.ui.btnStart.clicked.connect(lambda: self.WebScraping(self.timeTaken,True))
        self.ui.btnExportcsv.clicked.connect(lambda: self.exportCsv())
        
        
        self.dictSorting={
            1:InsertionSort,
            2:SelectionSort,
            3:MergeSort,
            4:BubbleSort,
            5:HybridMergeSort,
            6:RandomizedQuickSort,
            7:QuickSort,
            8:CountingSort,
            9:RadixSort,
            10:bucketSort,
            11:pigeonHoleSort,
            12:PostmanSorting,
            13:CockTailSorting,
        }
        self.dictAttrs={
            0:'MovieName',
            1:'Certificate',
            2:'Duration',
            3:'Genre',
            4:'Rating',
            5:'Years',
            6:'Director',
            7:'Actors',
            8:'Gross',
            9:'Votes',
        }
        self.ui.btnImportcsv.clicked.connect(lambda:self.importCsv())
        self.ui.tableWidget.horizontalHeader().sectionClicked.connect(lambda: self.getColumn())
        self.ui.cmbAlgorithms.activated.connect(lambda:self.sortDataTable(self.ui.cmbAlgorithms.currentIndex(),self.df))
        
        
        self.show()
    
    def WebScraping(self,totalTime,running):
        driver = scrap.webdriver.Chrome(executable_path='chromedriver.exe') 
        
        start_time=scrap.time.time()
        file=open(file="link.txt",mode='r')
        link=file.readline()
        
        #link="/search/title/?country_of_origin=IN&after=WzE5ODQ2NDYsInR0MDI1NjQzOSIsNzU0MDFd&ref_=adv_nxt"
        i=1
        while(i==1):
            self.ui.btnPause.clicked.connect(lambda: bool(running=False))
            
            driver.get("https://www.imdb.com/"+link) 
            file=open(file="link.txt",mode='w')
            file.write(link)
            content = driver.page_source 
            soup = scrap.BeautifulSoup(content)  
            linkNext=soup.find('a',attrs={'class':'lister-page-next next-page'})
            link=linkNext['href']
            Data=soup.find_all('div',attrs={'class':'lister-item mode-advanced'})
            for check in Data:
                name=check.h3.a.text
                scrap.movieNameA.append(name) 
                year=check.find('span',attrs={'class':'lister-item-year'}).text.strip()
                a=""
                for iter in year:
                    if iter.isdigit():
                        a=a+iter
                scrap.yearA.append(a[:4]) 
                certificate=check.find('span',attrs={'class':'certificate'})
                if certificate is not None:
                    scrap.certificateA.append(certificate.text.strip())
                else:
                    scrap.certificateA.append("None")   
                durationfull=check.find('span',attrs={'class':'runtime'})
                if durationfull is not None:
                    duration=(durationfull.text.strip()).split()[0] #get minutes
                    scrap.durationA.append(duration)
                else:
                    scrap.durationA.append("")
                genre=check.find('span',attrs={'class':'genre'})
                if genre is not None:
                    scrap.genreA.append(genre.text.strip())
                else:
                    scrap.genreA.append("None")
                rating=check.find('div',attrs={'class':'inline-block ratings-imdb-rating'})
                if rating is not None:  
                    scrap.ratingA.append(rating.text.strip())
                else:
                    scrap.ratingA.append("")
                #votes=check.find('span',attrs={'name':'nv'}).text.strip()
                #votesA.append(votes)
                paras=check.find('p', attrs={'class':''}).text.strip()
                directorActor=""
                director=""
                actor=""        
                if(paras!=""):
                    if '|' in paras:
                        directorActor=paras.split('|')
                        director=directorActor[0].split(':')[1].strip()
                        a=directorActor[1].split(':')[1].strip()
                        actor=''.join(a.splitlines())
                    else:
                        director=""
                        if  len(paras.split(':'))>1:
                            a=paras.split(':')[1].strip()
                            actor=''.join(a.splitlines())
                        else:
                            actor=""
                    scrap.directorA.append(director)
                    scrap.actorA.append(actor)
                else:
                    scrap.directorA.append("")
                    scrap.actorA.append("")
                
                Values=check.find_all('span',attrs={'name':'nv'})
                if(len(Values)>0):
                    votes=Values[0]
                    scrap.votesA.append(votes.text)
                    if(len(Values)==1):
                        scrap.grossA.append("")
                    else:
                        Gross=Values[1]
                        scrap.grossA.append(Gross.text) 
                else:
                    scrap.votesA.append("")
                    scrap.grossA.append("")
                
                #print(name,year[1:5],duration,genre,rating,director+" :"+actor)
                
            da={'Movie Names':scrap.movieNameA,'Certificate':scrap.certificateA,'Duration':scrap.durationA,'Genre':scrap.genreA,'Rating':scrap.ratingA,'Years':scrap.yearA,'Director':scrap.directorA,'Actors':scrap.actorA,'Gross':scrap.grossA,'Votes':scrap.votesA}
            self.df=pd.DataFrame.from_dict(da)
            self.loadDataTable(self.df)
            end_time=scrap.time.time()-start_time
            totalTime +=end_time
            i=0
            
            
   
    def SearchTop(self,text):
        ObjArray=self.reading_list(self.df)
        temp=[]
        if(text=="" or text==" "):
            self.loadDataTable(self.df)
        else:
            for i in ObjArray:
                
                a=KMPStringSearching(i.MovieName,text)
                if(a==True):
                    
                    temp.append(i)
            show=self.reading_ObjectList(temp)
            self.ui.tableWidget.clear()
            self.loadSearchData(show)
        
    def importCsv(self):
        self.df=pd.read_csv(r'data.csv')
        self.loadDataTable(self.df)
    def exportCsv(self):
        self.df.to_csv('exportData.csv',index=False)
    def getColumn(self):
        self.headerCol=self.ui.tableWidget.currentColumn()
    
    def closeHome(self):
        self.ui.mainBody.setCurrentIndex(1)
    def closeScrapping(self):
        self.ui.mainBody.setCurrentIndex(0)
    def OpenAdvanced_Search(self):
        dia=QtWidgets.QDialog()
        dia.ui=Ui_Dialog()
        dia.ui.setupUi(dia)
        dia.exec()
       
       
       
       
    def closeAdvaced_Search(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        
        

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
    def loadDataTable(self,df):
        rowCount=df.shape[0]
        colCount=df.shape[1]
        DataTable=self.ui.tableWidget
        headers = list(df)
        DataTable.setHorizontalHeaderLabels(headers) 
        DataTable.setRowCount(rowCount)
        DataTable.setColumnCount(colCount)       
        dfArray = df.values
        self.dfToTable(dfArray)
    def loadSearchData(self,arr):
        DataTable=self.ui.tableWidget
        try:
            DataTable.setRowCount(len(arr))
        except:
            DataTable.setRowCount(0)
        try:
            DataTable.setColumnCount(len(arr[1]))
        except:
            DataTable.setColumnCount(0)
            
        self.dfToTable(arr)
    def dfToTable(self,dfArray):
            rowCount=len(dfArray)
            colCount=10
            
            for x in range(rowCount):
                for y in range(colCount):
                    self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(dfArray[x][y])))    
    def sortDataTable(self,sortFunc,df):
        
        Arr=self.reading_list(df)
        A=self.dictSorting[sortFunc](Arr,self.dictAttrs[self.headerCol],0,len(Arr)-1)
        B=self.reading_ObjectList(Arr)
        if(B!=None):
            self.dfToTable(B)
        else:
            self.dfToTable(Arr)
            
    def reading_list(self,df)->list:
        return list(map(lambda x:Movie(MovieName=x[0],Certificate=x[1],Duration=x[2],Genre=x[3],Rating=x[4],Years=x[5],Director=x[6],Actors=x[7],Gross=x[8],Votes=x[9]),df.values.tolist()))
    
                    
                    
    
    def reading_ObjectList(self,A):
        l=len(A)
        arr = [[0 for i in range(10)] for j in range(l)]
        for i in range(l):
            arr[i][0]=A[i].MovieName
            arr[i][1]=A[i].Certificate
            arr[i][2]=A[i].Duration
            arr[i][3]=A[i].Genre
            arr[i][4]=A[i].Rating
            arr[i][5]=A[i].Years
            arr[i][6]=A[i].Director
            arr[i][7]=A[i].Actors 
            arr[i][8]=A[i].Gross 
            arr[i][9]=A[i].Votes 
        return arr    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())