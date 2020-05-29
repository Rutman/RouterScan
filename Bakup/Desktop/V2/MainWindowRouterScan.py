# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowRouterScan_bak.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_RouterScanMainWindow(object):
    def setupUi(self, RouterScanMainWindow):
        RouterScanMainWindow.setObjectName("RouterScanMainWindow")
        RouterScanMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(RouterScanMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 731, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowserTarget = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowserTarget.setObjectName("textBrowserTarget")
        self.verticalLayout.addWidget(self.textBrowserTarget)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textBrowserOutput = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowserOutput.setObjectName("textBrowserOutput")
        self.verticalLayout_2.addWidget(self.textBrowserOutput)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        RouterScanMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RouterScanMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuDevices = QtWidgets.QMenu(self.menubar)
        self.menuDevices.setObjectName("menuDevices")
        self.menuMikroTik = QtWidgets.QMenu(self.menuDevices)
        self.menuMikroTik.setObjectName("menuMikroTik")
        self.menuCVE_2018_14847 = QtWidgets.QMenu(self.menuMikroTik)
        self.menuCVE_2018_14847.setObjectName("menuCVE_2018_14847")
        self.menuUtilization = QtWidgets.QMenu(self.menuCVE_2018_14847)
        self.menuUtilization.setObjectName("menuUtilization")
        self.menuDocument = QtWidgets.QMenu(self.menubar)
        self.menuDocument.setObjectName("menuDocument")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        RouterScanMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RouterScanMainWindow)
        self.statusbar.setObjectName("statusbar")
        RouterScanMainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(RouterScanMainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionContact = QtWidgets.QAction(RouterScanMainWindow)
        self.actionContact.setObjectName("actionContact")
        self.actionAPIs = QtWidgets.QAction(RouterScanMainWindow)
        self.actionAPIs.setObjectName("actionAPIs")
        self.actionDocument = QtWidgets.QAction(RouterScanMainWindow)
        self.actionDocument.setObjectName("actionDocument")
        self.actionUsage = QtWidgets.QAction(RouterScanMainWindow)
        self.actionUsage.setObjectName("actionUsage")
        self.actionExploitCVE_2018_14847 = QtWidgets.QAction(RouterScanMainWindow)
        self.actionExploitCVE_2018_14847.setObjectName("actionExploitCVE_2018_14847")
        self.actionVPNCVE_2018_14847 = QtWidgets.QAction(RouterScanMainWindow)
        self.actionVPNCVE_2018_14847.setObjectName("actionVPNCVE_2018_14847")
        self.menuUtilization.addAction(self.actionVPNCVE_2018_14847)
        self.menuCVE_2018_14847.addAction(self.actionExploitCVE_2018_14847)
        self.menuCVE_2018_14847.addAction(self.menuUtilization.menuAction())
        self.menuMikroTik.addAction(self.menuCVE_2018_14847.menuAction())
        self.menuDevices.addAction(self.menuMikroTik.menuAction())
        self.menuDocument.addAction(self.actionDocument)
        self.menuDocument.addAction(self.actionAPIs)
        self.menuDocument.addAction(self.actionUsage)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionContact)
        self.menubar.addAction(self.menuDevices.menuAction())
        self.menubar.addAction(self.menuDocument.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(RouterScanMainWindow)
        QtCore.QMetaObject.connectSlotsByName(RouterScanMainWindow)


    def retranslateUi(self, RouterScanMainWindow):
        _translate = QtCore.QCoreApplication.translate
        RouterScanMainWindow.setWindowTitle(_translate("RouterScanMainWindow", "Router Scanner"))
        self.label.setText(_translate("RouterScanMainWindow", " Target"))
        self.label_2.setText(_translate("RouterScanMainWindow", "Output"))
        self.menuDevices.setTitle(_translate("RouterScanMainWindow", "Devices"))
        self.menuMikroTik.setTitle(_translate("RouterScanMainWindow", "MikroTik"))
        self.menuCVE_2018_14847.setTitle(_translate("RouterScanMainWindow", "CVE_2018_14847"))
        self.menuUtilization.setTitle(_translate("RouterScanMainWindow", "Utilization"))
        self.menuDocument.setTitle(_translate("RouterScanMainWindow", "Document"))
        self.menuHelp.setTitle(_translate("RouterScanMainWindow", "Help"))
        self.actionHelp.setText(_translate("RouterScanMainWindow", "Help"))
        self.actionContact.setText(_translate("RouterScanMainWindow", "Contact"))
        self.actionAPIs.setText(_translate("RouterScanMainWindow", "APIs"))
        self.actionDocument.setText(_translate("RouterScanMainWindow", "Document"))
        self.actionUsage.setText(_translate("RouterScanMainWindow", "Usage"))
        self.actionExploitCVE_2018_14847.setText(_translate("RouterScanMainWindow", "Exploit"))
        self.actionVPNCVE_2018_14847.setText(_translate("RouterScanMainWindow", "VPN"))