# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddUserswindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddUsersWindow(object):
    def setupUi(self, AddUsersWindow):
        AddUsersWindow.setObjectName("AddUsersWindow")
        AddUsersWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AddUsersWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitlWindow = QtWidgets.QLabel(self.centralwidget)
        self.labelTitlWindow.setEnabled(False)
        self.labelTitlWindow.setGeometry(QtCore.QRect(190, 0, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelTitlWindow.setFont(font)
        self.labelTitlWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTitlWindow.setObjectName("labelTitlWindow")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(510, 460, 261, 26))
        self.pushButton_8.setStyleSheet("background-color: rgb(0, 255, 20);\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 180, 321, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 230, 321, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 280, 321, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 330, 321, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        AddUsersWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddUsersWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        AddUsersWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddUsersWindow)
        self.statusbar.setObjectName("statusbar")
        AddUsersWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddUsersWindow)
        QtCore.QMetaObject.connectSlotsByName(AddUsersWindow)

    def retranslateUi(self, AddUsersWindow):
        _translate = QtCore.QCoreApplication.translate
        AddUsersWindow.setWindowTitle(_translate("AddUsersWindow", "MainWindow"))
        self.labelTitlWindow.setText(_translate("AddUsersWindow", "<html><head/><body><p><span style=\" color:#290808;\">Панель создание пользователя</span></p></body></html>"))
        self.pushButton_8.setText(_translate("AddUsersWindow", "Добавить сотрудника"))
        self.lineEdit.setPlaceholderText(_translate("AddUsersWindow", "Введите имя сотрудника"))
        self.lineEdit_2.setPlaceholderText(_translate("AddUsersWindow", "Введите логин сотрудника"))
        self.lineEdit_3.setPlaceholderText(_translate("AddUsersWindow", "Введите пароль сотрудника"))
        self.lineEdit_4.setPlaceholderText(_translate("AddUsersWindow", "Введите должность сотрудника"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddUsersWindow = QtWidgets.QMainWindow()
    ui = Ui_AddUsersWindow()
    ui.setupUi(AddUsersWindow)
    AddUsersWindow.show()
    sys.exit(app.exec_())
