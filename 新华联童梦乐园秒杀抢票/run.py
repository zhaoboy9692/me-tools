# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import json
import sys
import threading
from time import sleep

import requests
from PyQt5 import QtCore, QtWidgets

head = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; 16th Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/882 MMWEBSDK/190506 Mobile Safari/537.36 MMWEBID/715 MicroMessenger/7.0.6.1460(0x27000634) Process/tools NetType/WIFI Language/zh_CN',
    'Accept': 'application/json, text/plain, */*',
    'Connection': 'keep-alive',
    'Origin': 'https://pwx.cleartv.cn',
    'Referer': 'https://pwx.cleartv.cn/frontend/xhltmly/',
    'X-Requested-With': 'com.tencent.mm',
    'Accept-Language': 'zh-CN,en-US;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Sec-Fetch-Mode': 'corss',
    'Sec-Fetch-Sites': 'same-origin',
}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("新华联童梦乐园门票秒杀")
        MainWindow.resize(830, 598)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.get_yzm = QtWidgets.QPushButton(self.centralwidget)
        self.get_yzm.setGeometry(QtCore.QRect(200, 60, 93, 31))
        self.get_yzm.setObjectName("get_yzm")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 72, 15))
        self.label.setObjectName("label")
        self.phone = QtWidgets.QLineEdit(self.centralwidget)
        self.phone.setGeometry(QtCore.QRect(80, 10, 211, 31))
        self.phone.setObjectName("phone")
        self.yzm = QtWidgets.QLineEdit(self.centralwidget)
        self.yzm.setGeometry(QtCore.QRect(80, 60, 113, 31))
        self.yzm.setObjectName("yzm")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 72, 15))
        self.label_2.setObjectName("label_2")
        self.start_qg = QtWidgets.QPushButton(self.centralwidget)
        self.start_qg.setGeometry(QtCore.QRect(610, 10, 191, 51))
        self.start_qg.setObjectName("start_qg")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(300, 10, 301, 101))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setTabletTracking(False)
        self.textBrowser.setLineWrapColumnOrWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 160, 631, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 1, item)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(90, 390, 641, 181))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 100, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 130, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(590, 130, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.shi = QtWidgets.QRadioButton(self.centralwidget)
        self.shi.setEnabled(True)
        self.shi.setGeometry(QtCore.QRect(220, 130, 61, 16))
        self.shi.setAcceptDrops(False)
        self.shi.setAutoFillBackground(False)
        self.shi.setObjectName("shi")
        self.shis = QtWidgets.QRadioButton(self.centralwidget)
        self.shis.setGeometry(QtCore.QRect(290, 130, 61, 16))
        self.shis.setObjectName("shis")
        self.shib = QtWidgets.QRadioButton(self.centralwidget)
        self.shib.setGeometry(QtCore.QRect(350, 130, 61, 16))
        self.shib.setObjectName("shib")
        self.ershier = QtWidgets.QRadioButton(self.centralwidget)
        self.ershier.setGeometry(QtCore.QRect(420, 130, 61, 16))
        self.ershier.setObjectName("ershier")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 130, 72, 15))
        self.label_4.setObjectName("label_4")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(610, 70, 191, 51))
        self.stop.setObjectName("stop")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 130, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.get_yzm.clicked.connect(MainWindow.get_yzm_click)
        self.pushButton.clicked.connect(MainWindow.login)
        self.start_qg.clicked.connect(MainWindow.strat_miaosha)
        self.stop.clicked.connect(MainWindow.stop_miaosha)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "新华联童梦乐园门票秒杀"))
        self.get_yzm.setText(_translate("MainWindow", "获取验证码"))
        self.label.setText(_translate("MainWindow", "手机号码"))
        self.label_2.setText(_translate("MainWindow", "验证码"))
        self.start_qg.setText(_translate("MainWindow", "开始抢购"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">温馨提示：</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 请先输入手机号码，获取验证码并登陆</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 填写抢购信息，三者缺一不可,最多5个人</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 倒计时开始15秒钟，请点击开始抢购</p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 抢购购结束后 请在https://pwx.cleartv.cn/frontend/xhltmly/#/myOrder 里面查询订单，并支付订单</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 默认日期为20号10点，可以更改为19号，18号</p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "19"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "20"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "手机号码"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "身份证号码"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label_3.setText(_translate("MainWindow", "游玩日期"))
        self.lineEdit.setText(_translate("MainWindow", "2019-08-20"))
        self.shi.setText(_translate("MainWindow", "10点"))
        self.shis.setText(_translate("MainWindow", "14点"))
        self.shib.setText(_translate("MainWindow", "18点"))
        self.ershier.setText(_translate("MainWindow", "22点"))
        self.label_4.setText(_translate("MainWindow", "抢购时间"))
        self.stop.setText(_translate("MainWindow", "停止抢购"))
        self.lineEdit_2.setText(_translate("MainWindow", "cookie"))

class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.stop = False
        self.cookie = None

    def get_yzm_click(self):
        post_data = {
            'phone': self.phone.text(),
            'project': "xining"
        }
        url = 'https://pwx.cleartv.cn/app/verificationcode'
        res = requests.post(url, data=json.dumps(post_data), headers=head)
        if '200' in str(res.text):
            self.textBrowser_2.append(str('获取验证码成功'))
        else:
            self.textBrowser_2.append(str('获取验证码失败，' + str(res.text)))
        self.cookie = res.headers.get('Set-Cookie')
    def login(self):
        global head
        url = 'https://pwx.cleartv.cn/app/user/phonelogin'
        post_data = {
            'phone': str(self.phone.text()),
            'project': "xining",
            'code': str(self.yzm.text())
        }
        head['Cookie'] = self.cookie
        res = requests.post(url, data=json.dumps(post_data), headers=head)
        self.textBrowser_2.append(str(res.text))
        self.cookie = str(self.cookie).replace('; Path=/; HttpOnly', '')
        head['Cookie'] = self.cookie
        if '200' in str(res.text):
            self.textBrowser_2.append(str('登陆成功'))
        else:
            self.textBrowser_2.append(str('登陆失败，请重新尝试'))

    def stop_miaosha(self):
        self.stop = True

    def strat_miaosha(self):
        global head
        self.stop = False
        ticket_type_id = 99
        if 'cookie' not in str(self.lineEdit_2.text()):
            self.cookie=str(self.lineEdit_2.text())
            head['Cookie'] = self.cookie
        rows = self.tableWidget.rowCount()
        ll = []
        for rows_index in range(rows):
            try:
                dic = {
                    'buyer_name': self.tableWidget.item(rows_index, 0).text(),
                    'buyer_phone': self.tableWidget.item(rows_index, 1).text(),
                    'buyer_identify': self.tableWidget.item(rows_index, 2).text(),
                }
                ll.append(dic)
            except:
                break
        try:
            date = str(self.lineEdit.text()).split('-')[-1]
        except:
            self.textBrowser_2.append('游玩日期出现问题')
            return
        if self.shi.isChecked():
            if '18' in date:
                ticket_type_id = 93
            if '19' in date:
                ticket_type_id = 94
            if '20' in date:
                ticket_type_id = 95
        if self.shis.isChecked():
            if '18' in date:
                ticket_type_id = 96
            if '19' in date:
                ticket_type_id = 97
            if '20' in date:
                ticket_type_id = 98
        if self.shib.isChecked():
            if '18' in date:
                ticket_type_id = 99
            if '19' in date:
                ticket_type_id = 100
            if '20' in date:
                ticket_type_id = 102
        if self.ershier.isChecked():
            if '18' in date:
                ticket_type_id = 103
            if '19' in date:
                ticket_type_id = 104
            if '20' in date:
                ticket_type_id = 105
        threading.Thread(target=self.st, args=(ll, ticket_type_id)).start()

    def st(self, ll, ticket_type_id):
        while not self.stop:
            for d in ll:
                if not str(d.get('buyer_name')).strip():
                    continue
                post_data = {"buyer_name": d.get('buyer_name'), "buyer_phone": d.get('buyer_phone'),
                             "buyer_papers_type": "ID_CARD",
                             "buyer_identify": d.get('buyer_identify'), "price": 0.01,
                             "play_date_begin": self.lineEdit.text(),
                             "tickets": [
                                 {"guest_name": "", "guest_phone": "", "guest_identify": "", "ticket_type_id":ticket_type_id,
                                  "price": 0.01, "play_date_begin": self.lineEdit.text(), "errName": "", "errPhone": "",
                                  "errId": ""}], "guestCount": 1}
                threading.Thread(target=self.m, args=(post_data,d.get('buyer_name'))).start()
                sleep(0.1)

    def m(self, post_data,buyer_name):
        url = 'https://pwx.cleartv.cn/app/order'
        res = requests.post(url, data=json.dumps(post_data), headers=head)
        self.textBrowser_2.append(str(buyer_name)+'成功' if '200' in str(res.text) else str(buyer_name)+str(res.text))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())
