# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'islem.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IslemPanel(object):
    def setupUi(self, IslemPanel):
        IslemPanel.setObjectName("IslemPanel")
        IslemPanel.resize(345, 255)
        self.centralwidget = QtWidgets.QWidget(IslemPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.islem_Label = QtWidgets.QLabel(self.centralwidget)
        self.islem_Label.setGeometry(QtCore.QRect(10, 10, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setUnderline(True)
        self.islem_Label.setFont(font)
        self.islem_Label.setObjectName("islem_Label")
        self.islem_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.islem_textBrowser.setGeometry(QtCore.QRect(10, 50, 311, 151))
        self.islem_textBrowser.setObjectName("islem_textBrowser")
        IslemPanel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IslemPanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 21))
        self.menubar.setObjectName("menubar")
        IslemPanel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IslemPanel)
        self.statusbar.setObjectName("statusbar")
        IslemPanel.setStatusBar(self.statusbar)

        self.retranslateUi(IslemPanel)
        QtCore.QMetaObject.connectSlotsByName(IslemPanel)

    def retranslateUi(self, IslemPanel):
        _translate = QtCore.QCoreApplication.translate
        IslemPanel.setWindowTitle(_translate("IslemPanel", "MainWindow"))
        self.islem_Label.setText(_translate("IslemPanel", "LABEL DENEME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IslemPanel = QtWidgets.QMainWindow()
    ui = Ui_IslemPanel()
    ui.setupUi(IslemPanel)
    IslemPanel.show()
    sys.exit(app.exec_())