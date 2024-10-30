# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from src.Controllers.UsersController import *
from src.Views.admin_window import Ui_AdminWindow

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.Title_login = QtWidgets.QTextBrowser(self.centralwidget)
        self.Title_login.setGeometry(QtCore.QRect(210, 0, 341, 61))
        self.Title_login.setObjectName("Title_login")
        self.addLogin = QtWidgets.QTextEdit(self.centralwidget)
        self.addLogin.setGeometry(QtCore.QRect(70, 180, 301, 31))
        self.addLogin.setObjectName("addLogin")
        self.addPassword = QtWidgets.QTextEdit(self.centralwidget)
        self.addPassword.setGeometry(QtCore.QRect(420, 180, 301, 31))
        self.addPassword.setObjectName("addPassword")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(270, 300, 231, 41))
        self.LoginButton.setObjectName("LoginButton")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.Title_login.setHtml(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Приветсвуем Вас в информационой сиситеме КАФЕ</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пожалуста введите свой логин и пароль</p></body></html>"))
        self.addLogin.setHtml(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.addLogin.setPlaceholderText(_translate("Login", "Введите свой логин"))
        self.addPassword.setHtml(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.addPassword.setPlaceholderText(_translate("Login", "Введите свой пароль"))
        self.LoginButton.setText(_translate("Login", "Войти"))

    # метод обработки кнопки
    # def test_buthon(self):
    #     log = self.addLogin.toPlainText()
    #     passwd = self.addPassword.toPlainText()
    #     user = UsersControllers()
    #     result = user.log_in(log, passwd)
    #     print(result)
    #     print(log,passwd)
    #метод проверки логина и пароля и роли
    #если логин и пароль True, то проверяется для РОЛИ окно

    def open_panel(self):
        log = self.addLogin.toPlainText()
        passwd = self.addPassword.toPlainText()
        user = UsersControllers()#создается объект класса UsersController
        if user.log_in(log,passwd):
            if user.show(log).role_id.id == 1:
                print('Админ')
            elif user.show(log).role_id.id == 2:
                print('Повар')
            else:
                print('Официант')
        else:
            print('пароль или логин введены неверный')

    #метод открытия окна админа
    

    # кнопка
    def pressButthon(self):
        self.LoginButton.clicked.connect(self.open_panel)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    ui.pressButthon()
    sys.exit(app.exec_())
