# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(60, 0, 131, 31))
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_status = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_status.setGeometry(QtCore.QRect(70, 240, 91, 20))
        self.lbl_status.setText("")
        self.lbl_status.setObjectName("lbl_status")
        self.line_edit_id = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_edit_id.setGeometry(QtCore.QRect(70, 40, 113, 20))
        self.line_edit_id.setText("")
        self.line_edit_id.setObjectName("line_edit_id")
        self.btn_submit_vote = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_submit_vote.setGeometry(QtCore.QRect(90, 160, 75, 23))
        self.btn_submit_vote.setObjectName("btn_submit_vote")
        self.lbl_id = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_id.setGeometry(QtCore.QRect(50, 40, 16, 16))
        self.lbl_id.setObjectName("lbl_id")
        self.lbl_candidates = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_candidates.setGeometry(QtCore.QRect(100, 60, 81, 20))
        self.lbl_candidates.setObjectName("lbl_candidates")
        self.radio_john = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_john.setGeometry(QtCore.QRect(70, 110, 91, 21))
        self.radio_john.setObjectName("radio_john")
        self.radio_jane = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_jane.setGeometry(QtCore.QRect(70, 80, 82, 17))
        self.radio_jane.setObjectName("radio_jane")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_title.setText(_translate("MainWindow", "VOTING APPLICATION"))
        self.btn_submit_vote.setText(_translate("MainWindow", "SUBMIT VOTE"))
        self.lbl_id.setText(_translate("MainWindow", "ID"))
        self.lbl_candidates.setText(_translate("MainWindow", "CANDIDATES"))
        self.radio_john.setText(_translate("MainWindow", "John"))
        self.radio_jane.setText(_translate("MainWindow", "Jane"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
