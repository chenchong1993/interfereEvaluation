# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\薛志远\eric6\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import gc
from tkinter import _flatten

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import time
import os
# from PyRadar import Radar
# from PyRadar import ppi
# from PIL import Image
import json


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1200, 810)
        mainWindow.setMinimumSize(QtCore.QSize(1200, 810))
        mainWindow.setMaximumSize(QtCore.QSize(1200, 810))
        mainWindow.setStatusTip("")
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1191, 721))
        self.tabWidget.setObjectName("tabWidget")
        # 干扰监测与评估选项卡
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        # groupBox_9为左侧框内区域
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 10, 191, 681))
        self.groupBox_9.setObjectName("groupBox_9")
        #处理选项按钮组
        self.radioButton_SVnum = QtWidgets.QRadioButton(self.groupBox_9) #卫星数分析
        self.radioButton_SVnum.setGeometry(QtCore.QRect(15, 25, 89, 16))
        self.radioButton_SVnum.setObjectName("radioButton_SVnum")
        self.radioButton_CNO = QtWidgets.QRadioButton(self.groupBox_9) #载噪比分析
        self.radioButton_CNO.setGeometry(QtCore.QRect(15, 50, 100, 16))
        self.radioButton_CNO.setObjectName("radioButton_CNO")
        self.radioButton_DOP = QtWidgets.QRadioButton(self.groupBox_9)  # DOP值分析
        self.radioButton_DOP.setGeometry(QtCore.QRect(15, 75, 100, 16))
        self.radioButton_DOP.setObjectName("radioButton_DOP")
        self.radioButton_DOPusab = QtWidgets.QRadioButton(self.groupBox_9)  # DOP可用性分析
        self.radioButton_DOPusab.setGeometry(QtCore.QRect(15, 100, 100, 16))
        self.radioButton_DOPusab.setObjectName("radioButton_DOPusab")
        self.radioButton_flightPath = QtWidgets.QRadioButton(self.groupBox_9)  # 飞行轨迹
        self.radioButton_flightPath.setGeometry(QtCore.QRect(15, 125, 100, 16))
        self.radioButton_flightPath.setObjectName("radioButton_flightPath")


        self.buttonGroup =QtWidgets.QButtonGroup(self.groupBox_9) #将分析选项定义成按钮组
        self.buttonGroup.addButton(self.radioButton_SVnum,1) #对每个选项添加点击事件 #卫星数分析 = 1
        self.buttonGroup.addButton(self.radioButton_CNO,2)  #载噪比分析 = 2
        self.buttonGroup.addButton(self.radioButton_DOP, 3) #DOP值分析 = 3
        self.buttonGroup.addButton(self.radioButton_DOPusab, 4) #DOP可用性分析 = 4
        self.buttonGroup.addButton(self.radioButton_flightPath, 5) #飞行轨迹 = 5

        # 数据处理进度条
        self.progressBar_1 = QtWidgets.QProgressBar(self.groupBox_9)
        self.progressBar_1.setGeometry(QtCore.QRect(10, 650, 181, 20))
        self.progressBar_1.setProperty("value", 0)
        self.progressBar_1.setObjectName("progressBar_1")
        # 开始处理按钮
        self.start_process = QtWidgets.QPushButton(self.groupBox_9)
        self.start_process.setGeometry(QtCore.QRect(10, 520, 171, 41))
        self.start_process.setObjectName("start_process")

        # 绘制图像按钮
        self.points = QtWidgets.QPushButton(self.groupBox_9)
        self.points.setGeometry(QtCore.QRect(10, 580, 171, 41))
        self.points.setObjectName("points")
        # 中部框内区域
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_10.setGeometry(QtCore.QRect(200, 10, 721, 681))
        self.groupBox_10.setObjectName("groupBox_10")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_analysis = QtWidgets.QTextBrowser(self.groupBox_10)
        self.textBrowser_analysis.setFont(font)
        self.textBrowser_analysis.setGeometry(QtCore.QRect(10, 20, 701, 651))
        self.textBrowser_analysis.setObjectName("textBrowser_analysis")

        # 右侧上部区域
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_11.setGeometry(QtCore.QRect(930, 10, 251, 341))
        self.groupBox_11.setObjectName("groupBox_11")
        #右侧上部区域内文字描述
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_info = QtWidgets.QTextBrowser(self.groupBox_11)
        self.textBrowser_info.setFont(font)
        self.textBrowser_info.setGeometry(QtCore.QRect(10, 20, 231, 311))
        self.textBrowser_info.setObjectName("textBrowser_info")

        # 右侧下部区域
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_12.setGeometry(QtCore.QRect(930, 356, 251, 334))
        self.groupBox_12.setObjectName("groupBox_12")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.groupBox_12)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 20, 231, 304))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.tabWidget.addTab(self.tab_4, "")

        # 后台控制标签页
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        # 菜单栏
        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu") #文件
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2") #视图
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3") #关于
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4") #设置
        mainWindow.setMenuBar(self.menuBar)
        # 状态栏
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        # 工具栏
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionopen = QtWidgets.QAction(mainWindow)
        self.actionopen.setObjectName("actionopen") #打开文件
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setObjectName("action_2") #退出程序
        self.menu.addAction(self.actionopen)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.actionopen)
        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        #信号槽
        self.buttonGroup.buttonClicked.connect(self.rbclicked)  # 按钮组的点击事件槽函数
        self.actionopen.triggered.connect(lambda: self.display_1(0))  #事件记录
        self.action_2.triggered.connect(self.action_stop)  #退出程序
        self.actionopen.triggered.connect(self.open_file)  #打开文件
        self.start_process.clicked.connect(self.process_data) #开始处理的信号槽，链接到process_data函数
        self.points.clicked.connect(self.plot_points)  #绘制图像信号槽，链接到plot_points

        # 全局变量
        self.analysisOptions = ''
        self.satlist = []
        self.bdslist = []
        self.gpslist = []
        self.hlist = []
        self.hasData = 0 #是否读入了数据


    def open_file(self):
        try:
            SAfile = QtWidgets.QFileDialog.getOpenFileName(mainWindow, "选取数据文件",
                                                           "c:/data/gui/data")  # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.data_absolute_path = SAfile[0] #文件路径
            self.textBrowser_1.append(self.data_absolute_path)
            # 打开并读取文件,进行数据预处理
            self.ephdata = [[0 for col in range(10)] for row in range(100000)]
            self.progressBar_1.setValue(10)
            self.DATA = ""
            num = 0
            linenum = 1
            GSA = []
            GSV = []
            GGAdic = {}
            with open(self.data_absolute_path,"r") as file_object:
                for line in file_object:
                    print(linenum)
                    linenum +=1
                    if "GGA" in line:
                        navlist = line.split(",")
                        time = navlist[1]
                        lat = navlist[2] + navlist[3]
                        lng = navlist[4] + navlist[5]
                        posFlag = navlist[6]
                        posSatnum = navlist[7]
                        if posSatnum == '':
                            posSatnum = 0
                        else:
                            posSatnum = int(posSatnum)
                        Hdop = navlist[8]
                        h = navlist[9]+navlist[10]
                        h0 = navlist[11]+navlist[12]
                        DGPSsnum = navlist[13]
                        GGAdic ={"time": time, #时刻，UTC时间
                                 "lat": lat,
                                 "lng": lng,
                                 "posFlag": posFlag, #定位质量标识，0：未定位，1：单点，2：DGPS
                                 "posSatnum": posSatnum, #用于定位解算的卫星颗数
                                 "HDOP": Hdop,
                                 "h": h,
                                 "h0": h0,
                                 "DGPSsnum": DGPSsnum #DGPS基准站号
                                 }
                    elif "GSA" in line:
                        GSA.append(line)
                    elif "GSV" in line:
                        GSV.append(line)
                    elif "RMC" in line:
                        if GSA:
                            GSAres = max(GSA, key=len, default='')
                            GSAlist = GSAres.split(",")
                            recvMode = GSAlist[1]
                            posMode = GSAlist[2]
                            satList = GSAlist[3:3+int(posSatnum)]
                            Pdop = GSAlist[-4]
                            # Hdop = GSAlist[-3]
                            Vdop = GSAlist[-2]
                            GSAdic = {"recvMode": recvMode, #接收机操作模式：A自动选择，M强制进行二维或三维
                                      "posMode": posMode, #定位模式：1无有效定位，2二维定位，3三维定位
                                      "satList": satList, #用于定位的卫星编号
                                      "Pdop": Pdop,
                                      "Vdop": Vdop}
                            GGAdic.update(GSAdic)
                        if GSV:
                            # pass
                            gpsnum = ""
                            bdsnum = ""
                            gpslist = []
                            bdslist = []
                            for i in GSV:
                                if "GPGSV" in i:
                                    gplist = i.split(",")
                                    gpsnum = gplist[3]
                                    if gpsnum == '':
                                        gpsnum = 0
                                    else:
                                        gpsnum = int(gpsnum)
                                    last = gplist[-1].split("*")[0]
                                    gplist = gplist[4:-1]
                                    gplist.append(last)
                                    gpslist.append(gplist)
                                elif "BDGSV" in i:
                                    bdlist = i.split(",")
                                    bdsnum = bdlist[3]
                                    if bdsnum == '':
                                        bdsnum = 0
                                    else:
                                        bdsnum = int(bdsnum)
                                    last = bdlist[-1].split("*")[0]
                                    bdlist = bdlist[4:-1]
                                    bdlist.append(last)
                                    bdslist.append(bdlist)
                            gpslist = list(_flatten(gpslist))
                            bdslist = list(_flatten(bdslist))
                            GSVdic = {"gpsnum":gpsnum, #GPS可视卫星数
                                      "bdsnum":bdsnum,
                                      "gpslist":gpslist, #GPS可视卫星列表，四个为一组，分别为卫星号、仰角、方位角、载噪比
                                      "bdslist":bdslist}
                            GGAdic.update(GSVdic)
                        rmclist = line.split(",")
                        posQua = rmclist[2]
                        speed = rmclist[7]
                        speedDir = rmclist[8]
                        date = rmclist[9]
                        magnetic = rmclist[10] + rmclist[11]
                        mode = rmclist[-1]
                        mode = mode.split("*")[0]
                        RMCdic = {"posQua":posQua, #定位质量标志，A代表GPS定位有效，V无效
                                  "speed":speed, #地面速度
                                  "speedDir":speedDir, #速度方向，单位度
                                  "date":date, #日期
                                  "magnetic":magnetic,#磁偏角
                                  "mode":mode #模式指示，A自主定位，D差分，E估算，N无效
                                  }
                        GGAdic.update(RMCdic)
                        self.ephdata[num] = GGAdic
                        num += 1
                        GSA.clear()
                        GSV.clear()
                    self.progressBar_1.setValue(40)

                print("读取完成")
                self.progressBar_1.setValue(100)
                if num > 0:
                    self.hasData = 1
                self.ephdata = self.ephdata[:num]

            self.display_info(self.ephdata)
            self.display_1(1)

        except:
            pass


    # 数据参数显示
    def display_info(self,text = []):
        self.textBrowser_info.clear()
        tex = "单点定位"
        satlist = []
        bdslist = []
        gpslist = []
        hlist = []
        for i in text:
            self.satlist.append(int(i["posSatnum"]))
            self.bdslist.append(int(i["bdsnum"]))
            self.gpslist.append(int(i["gpsnum"]))
            self.hlist.append(float(i["h"][:-1]))

        # print(text[0]["time"] )
        self.textBrowser_info.append("观测时段：" + text[0]["time"] + "-" + text[-1]["time"] + "\n" +
                                     "厉元数：" + str(len(text)) + "\n" +
                                     "定位最大卫星数：" + str(max(self.satlist)) + "\n" +
                                     "可视最大GPS卫星数：" + str(max(self.gpslist)) + "\n" +
                                     "可视最大BDS卫星数：" + str(max(self.bdslist)) + "\n" +
                                     "发射坐标：" + text[0]["lat"] + "," + text[0]["lng"] + "\n" +
                                     "落地坐标：" + text[-1]["lat"] + "," + text[-1]["lng"] + "\n" +
                                     "最大高度：" + str(max(self.hlist)) + "m" + "\n" +
                                     "定位方式：" + tex + "\n")

    def display_1(self, order):
        info = ['正在读取数据...', '数据读取成功', '数据处理中...', '处理完成', '正在绘制图像...', '绘制完成',
                '正在初始化数据...', '工作路径已选择', '卫星数图像绘制完成', '未读入数据', '', '', '', '', '', '', '', '', '', '', ]
        self.textBrowser_1.append(time.strftime("%H:%M:%S", time.localtime()))
        self.textBrowser_1.append(info[order])

    #选择分析种类函数
    def rbclicked(self):
        # sender = self.groupBox_9.sender()

        if self.buttonGroup.checkedId() == 1:
            self.analysisOptions = '卫星数'
        elif self.buttonGroup.checkedId() == 2:
            self.analysisOptions = '载噪比'
        elif self.buttonGroup.checkedId() == 3:
            self.analysisOptions = 'DOP值'
        elif self.buttonGroup.checkedId() == 4:
            self.analysisOptions = 'DOP可用性'
        elif self.buttonGroup.checkedId() == 5:
            self.analysisOptions = '飞行轨迹'
        # print(self.analysisOptions)

    def process_data(self):
        try:
            print("正在处理")
            if self.hasData == 0:
                self.display_1(9)
            if self.analysisOptions == '卫星数':
                self.textBrowser_analysis.clear()
                self.textBrowser_analysis.append("卫星数分析结果")
                # print(self.satlist)
                # print(self.gpslist)
                # print(self.bdslist)
                # print("卫星数")
            elif self.analysisOptions == "载噪比":
                self.textBrowser_analysis.clear()
                self.textBrowser_analysis.append("载噪比分析结果")
            elif self.analysisOptions == "载噪比":
                self.textBrowser_analysis.clear()
                self.textBrowser_analysis.append("载噪比分析结果")
            elif self.analysisOptions == "DOP值":
                self.textBrowser_analysis.clear()
                self.textBrowser_analysis.append("DOP值分析结果")
            elif self.analysisOptions == "DOP可用性":
                self.textBrowser_analysis.clear()
                self.textBrowser_analysis.append("DOP可用性分析结果")
            elif self.analysisOptions == "飞行轨迹":
                self.textBrowser_analysis.clear()
                self.textBrowser_analysis.append("飞行轨迹")
            else:
                self.textBrowser_analysis.clear()
                self.textBrowser_analysis.append("未选择评估类型")
                print("未选择")
            # print(self.analysisOptions)
            # self.display_1(2)
        except:
            pass

    # 以图像弹出框的形式画图
    def plot_points(self):
        try:
            # self.k.points()
            if self.hasData == 0:
                self.display_1(9)
            print("正在绘制图像")
            if self.analysisOptions == '卫星数':
                self.progressBar_1.setValue(10)
                # 用于定位的卫星数
                satx = list(range(1,len(self.satlist)+1))
                plt.scatter(satx, self.satlist)
                plt.ylim(-1, 15)
                plt.show()
                self.progressBar_1.setValue(40)
                #可见北斗卫星数
                BDSx = list(range(1, len(self.bdslist) + 1))
                plt.scatter(BDSx, self.bdslist)
                plt.ylim(-1, 15)
                plt.show()
                self.progressBar_1.setValue(80)
                # 可见GPS卫星数
                GPSx = list(range(1, len(self.gpslist) + 1))
                plt.scatter(GPSx, self.gpslist)
                plt.ylim(-1, 15)
                plt.show()
                self.progressBar_1.setValue(100)
                self.display_1(8)
            else:
                print("未选择")

        except:
            pass

    # 退出程序
    def action_stop(self):
        sys.exit(0)


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "干扰监测与评估软件"))
        self.groupBox_9.setStatusTip(_translate("mainWindow", "分析方法选择"))
        self.groupBox_9.setTitle(_translate("mainWindow", "分析方法选择"))
        self.radioButton_SVnum.setText(_translate("MainWindow", "卫星数分析"))
        self.radioButton_CNO.setText(_translate("MainWindow", "载噪比分析"))
        self.radioButton_DOP.setText(_translate("MainWindow", "DOP值分析"))
        self.radioButton_DOPusab.setText(_translate("MainWindow", "DOP可用性分析"))
        self.radioButton_flightPath.setText(_translate("MainWindow", "飞行轨迹"))
        self.progressBar_1.setStatusTip(_translate("mainWindow", "数据处理进度"))
        self.start_process.setStatusTip(_translate("mainWindow", "开始处理所选数据"))
        self.start_process.setText(_translate("mainWindow", "开始处理"))
        self.points.setStatusTip(_translate("mainWindow", "绘制图像"))
        self.points.setText(_translate("mainWindow", "图像绘制"))
        self.groupBox_10.setTitle(_translate("mainWindow", "评估结果"))
        self.groupBox_10.setStatusTip(_translate("mainWindow", "评估结果详情"))
        self.groupBox_11.setStatusTip(_translate("mainWindow", "数据详情"))
        self.groupBox_11.setTitle(_translate("mainWindow", "数据参数"))
        # self.label_31.setText(_translate("mainWindow", "观测时段：   "))
        # self.station_number_2.setText(_translate("mainWindow", "Z9527"))
        self.groupBox_12.setTitle(_translate("mainWindow", "事件记录"))
        self.textBrowser_1.setStatusTip(_translate("mainWindow", "历史事件记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("mainWindow", "干扰监测与评估"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("mainWindow", "后台控制"))
        self.menu.setTitle(_translate("mainWindow", "文件"))
        self.menu_2.setTitle(_translate("mainWindow", "视图"))
        self.menu_3.setTitle(_translate("mainWindow", "关于"))
        self.menu_4.setTitle(_translate("mainWindow", "设置"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.actionopen.setText(_translate("mainWindow", "打开文件"))
        self.actionopen.setShortcut(_translate("mainWindow", "Ctrl+O"))
        self.action_2.setText(_translate("mainWindow", "退出程序"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

