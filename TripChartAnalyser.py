# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TripChartAnalyser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(280, 80, 61, 16))
        self.label.setObjectName("label")
        self.comboBox_TT_step1 = QtWidgets.QComboBox(self.tab)
        self.comboBox_TT_step1.setGeometry(QtCore.QRect(410, 80, 101, 22))
        self.comboBox_TT_step1.setObjectName("comboBox_TT_step1")
        self.comboBox_TT_step1.addItem("")
        self.comboBox_TT_step1.addItem("")
        self.comboBox_TT_step1.addItem("")
        self.pushButton_step1 = QtWidgets.QPushButton(self.tab)
        self.pushButton_step1.setGeometry(QtCore.QRect(340, 190, 101, 31))
        self.pushButton_step1.setObjectName("pushButton_step1")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(280, 130, 61, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_totalDuties_step1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_totalDuties_step1.setGeometry(QtCore.QRect(410, 130, 101, 20))
        self.lineEdit_totalDuties_step1.setObjectName("lineEdit_totalDuties_step1")
        self.label_alert_step1 = QtWidgets.QLabel(self.tab)
        self.label_alert_step1.setGeometry(QtCore.QRect(300, 270, 191, 16))
        self.label_alert_step1.setObjectName("label_alert_step1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(280, 130, 61, 16))
        self.label_10.setObjectName("label_10")
        self.comboBox_TT_step2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_TT_step2.setGeometry(QtCore.QRect(410, 80, 101, 22))
        self.comboBox_TT_step2.setObjectName("comboBox_TT_step2")
        self.comboBox_TT_step2.addItem("")
        self.comboBox_TT_step2.addItem("")
        self.comboBox_TT_step2.addItem("")
        self.pushButton_step2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_step2.setGeometry(QtCore.QRect(300, 190, 181, 31))
        self.pushButton_step2.setObjectName("pushButton_step2")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(280, 80, 61, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_totalDuties_step2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_totalDuties_step2.setGeometry(QtCore.QRect(410, 130, 101, 20))
        self.lineEdit_totalDuties_step2.setObjectName("lineEdit_totalDuties_step2")
        self.label_alert_step2 = QtWidgets.QLabel(self.tab_2)
        self.label_alert_step2.setGeometry(QtCore.QRect(300, 270, 191, 16))
        self.label_alert_step2.setObjectName("label_alert_step2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.comboBox_TT_step3 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_TT_step3.setGeometry(QtCore.QRect(410, 80, 101, 22))
        self.comboBox_TT_step3.setObjectName("comboBox_TT_step3")
        self.comboBox_TT_step3.addItem("")
        self.comboBox_TT_step3.addItem("")
        self.comboBox_TT_step3.addItem("")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(280, 80, 61, 16))
        self.label_13.setObjectName("label_13")
        self.pushButton_step3 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_step3.setGeometry(QtCore.QRect(330, 140, 101, 31))
        self.pushButton_step3.setObjectName("pushButton_step3")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_14 = QtWidgets.QLabel(self.tab_6)
        self.label_14.setGeometry(QtCore.QRect(280, 80, 61, 16))
        self.label_14.setObjectName("label_14")
        self.pushButton_step4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_step4.setGeometry(QtCore.QRect(330, 140, 131, 31))
        self.pushButton_step4.setObjectName("pushButton_step4")
        self.comboBox_TT_step4 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_TT_step4.setGeometry(QtCore.QRect(410, 80, 101, 22))
        self.comboBox_TT_step4.setObjectName("comboBox_TT_step4")
        self.comboBox_TT_step4.addItem("")
        self.comboBox_TT_step4.addItem("")
        self.comboBox_TT_step4.addItem("")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.comboBox_TT_step5 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_TT_step5.setGeometry(QtCore.QRect(410, 80, 91, 22))
        self.comboBox_TT_step5.setObjectName("comboBox_TT_step5")
        self.comboBox_TT_step5.addItem("")
        self.comboBox_TT_step5.addItem("")
        self.comboBox_TT_step5.addItem("")
        self.pushButton_step5 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_step5.setGeometry(QtCore.QRect(330, 190, 131, 31))
        self.pushButton_step5.setObjectName("pushButton_step5")
        self.label_15 = QtWidgets.QLabel(self.tab_7)
        self.label_15.setGeometry(QtCore.QRect(280, 80, 61, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_7)
        self.label_16.setGeometry(QtCore.QRect(280, 130, 61, 16))
        self.label_16.setObjectName("label_16")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_7)
        self.dateEdit.setGeometry(QtCore.QRect(410, 130, 91, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2019, 6, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.label_17 = QtWidgets.QLabel(self.tab_7)
        self.label_17.setGeometry(QtCore.QRect(560, 510, 201, 20))
        self.label_17.setObjectName("label_17")
        self.tabWidget.addTab(self.tab_7, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connecting buttons
        self.pushButton_step1.clicked.connect(self.step1)
        self.pushButton_step2.clicked.connect(self.step2)
        self.pushButton_step3.clicked.connect(self.step3)
        self.pushButton_step4.clicked.connect(self.step4)
        self.pushButton_step5.clicked.connect(self.step5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TripChartAnalyser"))
        self.label.setText(_translate("MainWindow", "Time Table"))
        self.comboBox_TT_step1.setItemText(0, _translate("MainWindow", "WEEK"))
        self.comboBox_TT_step1.setItemText(1, _translate("MainWindow", "SAT"))
        self.comboBox_TT_step1.setItemText(2, _translate("MainWindow", "SUN"))
        self.pushButton_step1.setText(_translate("MainWindow", "Fetch Trips Data"))
        self.label_2.setText(_translate("MainWindow", "Total Duties"))
        self.label_alert_step1.setText(_translate("MainWindow", "?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Step 1"))
        self.label_10.setText(_translate("MainWindow", "Total Duties"))
        self.comboBox_TT_step2.setItemText(0, _translate("MainWindow", "WEEK"))
        self.comboBox_TT_step2.setItemText(1, _translate("MainWindow", "SAT"))
        self.comboBox_TT_step2.setItemText(2, _translate("MainWindow", "SUN"))
        self.pushButton_step2.setText(_translate("MainWindow", "Fetch Borading Deborading Points"))
        self.label_11.setText(_translate("MainWindow", "Time Table"))
        self.label_alert_step2.setText(_translate("MainWindow", "?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Step 2"))
        self.comboBox_TT_step3.setItemText(0, _translate("MainWindow", "WEEK"))
        self.comboBox_TT_step3.setItemText(1, _translate("MainWindow", "SAT"))
        self.comboBox_TT_step3.setItemText(2, _translate("MainWindow", "SUN"))
        self.label_13.setText(_translate("MainWindow", "Time Table"))
        self.pushButton_step3.setText(_translate("MainWindow", "Calculate Km"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Step 3"))
        self.label_14.setText(_translate("MainWindow", "Time Table"))
        self.pushButton_step4.setText(_translate("MainWindow", "Do Correction in Km Data"))
        self.comboBox_TT_step4.setItemText(0, _translate("MainWindow", "WEEK"))
        self.comboBox_TT_step4.setItemText(1, _translate("MainWindow", "SAT"))
        self.comboBox_TT_step4.setItemText(2, _translate("MainWindow", "SUN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Step 4"))
        self.comboBox_TT_step5.setItemText(0, _translate("MainWindow", "WEEK"))
        self.comboBox_TT_step5.setItemText(1, _translate("MainWindow", "SAT"))
        self.comboBox_TT_step5.setItemText(2, _translate("MainWindow", "SUN"))
        self.pushButton_step5.setText(_translate("MainWindow", "Generate DutyData"))
        self.label_15.setText(_translate("MainWindow", "Time Table"))
        self.label_16.setText(_translate("MainWindow", "WEF date"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.label_17.setText(_translate("MainWindow", "Developer: satishkushwah50@gmail.com"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Step 5"))

    #defing button functions
    def step1(self):
        #self.label_alert_step1.setText('Please wait data is being processed...')
        if self.comboBox_TT_step1.currentText()=='WEEK':
            choice=1
        elif self.comboBox_TT_step1.currentText()=='SAT':
            choice=2
        else: choice=3
        totalduties=int(self.lineEdit_totalDuties_step1.text())
        import ExcelTripchartReader_v4_5_including_arrival_departure
        ExcelTripchartReader_v4_5_including_arrival_departure.myfunction(choice,totalduties)
        QMessageBox.about(self,'Completed successfully',"Move to next step")

    def step2(self):
        #self.label_alert_step1.setText('Please wait data is being processed...')
        if self.comboBox_TT_step2.currentText()=='WEEK':
            choice=1
        elif self.comboBox_TT_step2.currentText()=='SAT':
            choice=2
        else: choice=3
        totalduties=int(self.lineEdit_totalDuties_step2.text())
        import ExcelTripchartReader_v4_5
        ExcelTripchartReader_v4_5.myfunction(choice,totalduties)
        QMessageBox.about(self,'Completed successfully',"Move to next step")

    def step3(self):
        if self.comboBox_TT_step3.currentText()=='WEEK':
            choice=1
        elif self.comboBox_TT_step3.currentText()=='SAT':
            choice=2
        else: choice=3
        import DutyKmCalculator_v2_2_with_SDG
        DutyKmCalculator_v2_2_with_SDG.myfunction(choice)
        QMessageBox.about(self,'Completed successfully',"Move to next step")

    def step4(self):
        if self.comboBox_TT_step4.currentText()=='WEEK':
            choice=1
        elif self.comboBox_TT_step4.currentText()=='SAT':
            choice=2
        else: choice=3
        import SidingKmDeductor_v1_1
        SidingKmDeductor_v1_1.myfunction(choice)
        QMessageBox.about(self,'Completed successfully',"Move to next step")

    def step5(self):
        if self.comboBox_TT_step5.currentText()=='WEEK':
            choice=1
        elif self.comboBox_TT_step5.currentText()=='SAT':
            choice=2
        else: choice=3
        wef=self.dateEdit.text().replace('/','.')
        import DutyDataAIO_v1_21
        DutyDataAIO_v1_21.myfunction(choice,wef)
        QMessageBox.about(self,'Completed successfully',"DutyData generated successfully")
        import os
        os.startfile(os.path.dirname(__file__)+"/Generated_DutyData/")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

