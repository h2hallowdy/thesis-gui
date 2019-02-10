# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\setup files\NVIDIA\GUI\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
import glob
from PyQt5 import QtCore, QtGui, QtWidgets


def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 410)

        #Initialize global
        self.imageDir = ''
        self.imageList= []
        self.outDir = ''
        self.xmlDir = ''
        self.cur = 0
        self.total = 0
        self.category = 0
        self.imagepath = ''
        self.imagename = ''
        self.labelfilename = ''
        self.xmlfilename = ''
        self.tkimg = None
        self.numbers = False
        self.boxcount = 0

        #Initialize main windows
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.imgDir = QtWidgets.QLineEdit(self.centralwidget)
        self.imgDir.setGeometry(QtCore.QRect(70, 10, 481, 20))
        self.imgDir.setObjectName("imgDir")
        self.loadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadBtn.setGeometry(QtCore.QRect(570, 10, 131, 23))
        self.loadBtn.setObjectName("loadBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.listBBox = QtWidgets.QListView(self.centralwidget)
        self.listBBox.setGeometry(QtCore.QRect(570, 70, 131, 192))
        self.listBBox.setObjectName("listBBox")
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(570, 270, 131, 23))
        self.delBtn.setObjectName("delBtn")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(570, 300, 131, 23))
        self.clearBtn.setObjectName("clearBtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_3.setObjectName("label_3")
        self.prevBtn = QtWidgets.QPushButton(self.centralwidget)
        self.prevBtn.setGeometry(QtCore.QRect(160, 340, 75, 23))
        self.prevBtn.setObjectName("prevBtn")
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setGeometry(QtCore.QRect(260, 340, 75, 23))
        self.nextBtn.setObjectName("nextBtn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 340, 47, 13))
        self.label_4.setObjectName("label_4")
        self.currValue = QtWidgets.QLabel(self.centralwidget)
        self.currValue.setGeometry(QtCore.QRect(430, 340, 47, 13))
        self.currValue.setText("")
        self.currValue.setObjectName("currValue")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 340, 16, 16))
        self.label_5.setObjectName("label_5")
        self.totalValue = QtWidgets.QLabel(self.centralwidget)
        self.totalValue.setGeometry(QtCore.QRect(510, 340, 47, 13))
        self.totalValue.setText("")
        self.totalValue.setObjectName("totalValue")
        self.imgFrame = QtWidgets.QLabel(self.centralwidget)
        self.imgFrame.setGeometry(QtCore.QRect(70, 40, 481, 281))
        self.imgFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.imgFrame.setText("")
        self.imgFrame.setObjectName("imgFrame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Initialize callback
        self.loadBtn.clicked.connect(self.loadDir)
        self.prevBtn.clicked.connect(self.prevImage)
        self.nextBtn.clicked.connect(self.nextImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ImageDir"))
        self.loadBtn.setText(_translate("MainWindow", "Load"))
        self.label_2.setText(_translate("MainWindow", "Bounding Boxes"))
        self.delBtn.setText(_translate("MainWindow", "Delete"))
        self.clearBtn.setText(_translate("MainWindow", "Clear All"))
        self.label_3.setText(_translate("MainWindow", "Image"))
        self.prevBtn.setText(_translate("MainWindow", "<< Prev"))
        self.nextBtn.setText(_translate("MainWindow", "Next >>"))
        self.label_4.setText(_translate("MainWindow", "Progress"))
        self.label_5.setText(_translate("MainWindow", "/"))

    def loadDir(self):
        s = self.imgDir.text()
        self.category = int(s)
        self.imageDir = os.path.join(r'./Images', '%03d' %(self.category))
        # dirs = os.listdir(self.imageDir)
        # for file in dirs:
        #     print(file)
        extensions = ("*.jpg", "*.jpeg", "*.JPG", "*.JPEG")
        for extension in extensions:
            self.imageList.extend(glob.glob(os.path.join(self.imageDir, extension)))
            self.imageList = Remove(self.imageList)
        if len(self.imageList) == 0:
            print('No .JPEG images found in the specified dir!')
            return
        # for debugging
        # print('We have found', '%d' %(len(self.imageList)), 'images') 
        # for image in self.imageList:
        #     print(image)

        # default to the 1st image in the collection
        self.cur = 1
        self.total = len(self.imageList)

        # set up output dir
        self.outDir = os.path.join(r'./Labels', '%03d' %(self.category))
        self.xmlDir = os.path.join(r'./AnnotationsXML', '%03d' %(self.category))
        if not os.path.exists(self.outDir):
            os.mkdir(self.outDir)
        if not os.path.exists(self.xmlDir):
            os.mkdir(self.xmlDir)
        
        self.loadImage()
    
    # Load Image
    def loadImage(self):
        self.imagepath = self.imageList[self.cur - 1]
        pixmap = QtGui.QPixmap(self.imagepath) # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.imgFrame.width(), self.imgFrame.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.imgFrame.setPixmap(pixmap) # Set the pixmap onto the label
        self.imgFrame.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
        # Current / Total
        self.currValue.setText(str(self.cur))
        self.totalValue.setText(str(self.total))

    # Prev button
    def prevImage(self):
        # self.saveImage()
        if self.cur > 1:
            self.cur -= 1
            self.loadImage()

    # Next Button
    def nextImage(self):
        # self.saveImage()
        if self.cur < self.total:
            self.cur += 1
            self.loadImage()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
