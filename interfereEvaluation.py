# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\薛志远\eric6\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import gc
from math import sqrt
from tkinter import _flatten

from PyQt5.QtGui import QIcon
# from fiona import _shim, schema
# from shapely.geometry import *
# from geopandas import *
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from pylab import mpl
import resource
import os
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1200, 810)
        mainWindow.setMinimumSize(QtCore.QSize(1200, 810))
        mainWindow.setMaximumSize(QtCore.QSize(1200, 810))
        mainWindow.setStatusTip("")
        mainWindow.setWindowIcon(QIcon(":/cetc.ico"))
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
        self.radioButton_SVnum.setGeometry(QtCore.QRect(15, 25, 190, 16))
        self.radioButton_SVnum.setObjectName("radioButton_SVnum")
        self.radioButton_CNO = QtWidgets.QRadioButton(self.groupBox_9) #载噪比分析
        self.radioButton_CNO.setGeometry(QtCore.QRect(15, 50, 190, 16))
        self.radioButton_CNO.setObjectName("radioButton_CNO")
        self.radioButton_DOP = QtWidgets.QRadioButton(self.groupBox_9)  # DOP值分析
        self.radioButton_DOP.setGeometry(QtCore.QRect(15, 75, 190, 16))
        self.radioButton_DOP.setObjectName("radioButton_DOP")
        self.radioButton_DOPusab = QtWidgets.QRadioButton(self.groupBox_9)  # DOP可用性分析
        self.radioButton_DOPusab.setGeometry(QtCore.QRect(15, 100, 190, 16))
        self.radioButton_DOPusab.setObjectName("radioButton_DOPusab")
        # self.radioButton_flightPath = QtWidgets.QRadioButton(self.groupBox_9)  # 飞行轨迹
        # self.radioButton_flightPath.setGeometry(QtCore.QRect(15, 125, 190, 16))
        # self.radioButton_flightPath.setObjectName("radioButton_flightPath")
        self.radioButton_posEffi = QtWidgets.QRadioButton(self.groupBox_9)  # 定位有效性
        self.radioButton_posEffi.setGeometry(QtCore.QRect(15, 125, 190, 16))
        self.radioButton_posEffi.setObjectName("radioButton_posEffi")
        self.radioButton_flyH = QtWidgets.QRadioButton(self.groupBox_9)  # 飞行高度
        self.radioButton_flyH.setGeometry(QtCore.QRect(15, 150, 190, 16))
        self.radioButton_flyH.setObjectName("radioButton_flyH")


        self.buttonGroup =QtWidgets.QButtonGroup(self.groupBox_9) #将分析选项定义成按钮组
        self.buttonGroup.addButton(self.radioButton_SVnum,1) #对每个选项添加点击事件 #卫星数分析 = 1
        self.buttonGroup.addButton(self.radioButton_CNO,2)  #载噪比分析 = 2
        self.buttonGroup.addButton(self.radioButton_DOP, 3) #DOP值分析 = 3
        self.buttonGroup.addButton(self.radioButton_DOPusab, 4) #DOP可用性分析 = 4
        # self.buttonGroup.addButton(self.radioButton_flightPath, 5) #飞行轨迹 = 5
        self.buttonGroup.addButton(self.radioButton_posEffi,6) #定位有效性 = 6
        self.buttonGroup.addButton(self.radioButton_flyH,7) #飞行高度 = 7

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
                    # print(linenum)
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
                            # GSAres = max(GSA, key=len, default='')
                            satList = []
                            for i in GSA:
                                satList.extend(i.split(",")[3:-5])
                            while "" in satList:
                                satList.remove("")
                            GSAlist = GSA[0].split(",")
                            recvMode = GSAlist[1]
                            posMode = GSAlist[2]
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
                self.progressBar_1.setValue(60)
                if num > 0:
                    self.hasData = 1
                self.ephdata = self.ephdata[:num]

            self.display_info(self.ephdata)

            self.CN0List = [[0 for col in range(1)] for row in range(36)]
            self.bdCN0List = [[0 for col in range(1)] for row in range(60)]
            self.progressBar_1.setValue(70)
            gpsCn0 = []
            bdsCn0 = []
            for i in self.ephdata:
                gcn0 = []
                bcn0 = []
                a = int(len(i["gpslist"]) / 4)
                for j in range(int(len(i["gpslist"]) / 4)):
                    if i["gpslist"][j * 4 + 3] != "":
                        gcn0.append(int(i["gpslist"][j * 4]))
                        gcn0.append(int(i["gpslist"][j * 4 + 3]))
                    else:
                        gcn0.append(int(i["gpslist"][j * 4]))
                        gcn0.append(0)
                for k in range(int(len(i["bdslist"]) / 4)):
                    if i["bdslist"][k * 4 + 3] != "":
                        bcn0.append(int(i["bdslist"][k * 4])-140)
                        bcn0.append(int(i["bdslist"][k * 4 + 3]))
                    else:
                        bcn0.append(int(i["bdslist"][k * 4])-140)
                        bcn0.append(0)
                gpsCn0.append(gcn0)
                bdsCn0.append(bcn0)
            self.progressBar_1.setValue(85)
            for i in gpsCn0:
                for j in range(int(len(i) / 2)):
                    m = 0
                    n = 0
                    for m in range(36):
                        if i[2 * j] == m:
                            self.CN0List[n].append(i[2 * j + 1])
                        n += 1
            self.progressBar_1.setValue(90)
            for i in bdsCn0:
                for j in range(int(len(i) / 2)):
                    m = 0
                    n = 0
                    for m in range(60):
                        if i[2 * j] == m:
                            self.bdCN0List[n].append(i[2 * j + 1])
                        n += 1

            self.isGPScn0 = False
            self.isBDScn0 = False
            for i in self.CN0List:
                if any(i) is False:
                    del i[1:]
                else:
                    self.isGPScn0 = True
            for i in self.bdCN0List:
                for j in i:
                    if j != 0:
                        self.isBDScn0 = True
                        break

            self.progressBar_1.setValue(100)

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
            if i["posSatnum"] == "":
                self.satlist.append(0)
            else:
                self.satlist.append(int(i["posSatnum"]))
            if i["bdsnum"] == "":
                self.bdslist.append(0)
            else:
                self.bdslist.append(int(i["bdsnum"]))
            if i["gpsnum"] == "":
                self.gpslist.append(0)
            else:
                self.gpslist.append(int(i["gpsnum"]))
            if i["h"][:-1] == "":
                self.hlist.append(0)
            else:
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
        elif self.buttonGroup.checkedId() == 6:
            self.analysisOptions = '定位有效性'
        elif self.buttonGroup.checkedId() == 7:
            self.analysisOptions = '飞行高度'
        # print(self.analysisOptions)

    def process_data(self):
        try:
            print("正在处理")
            if self.hasData == 0:
                self.display_1(9)
            if self.analysisOptions == '卫星数':
                self.display_1(2)
                self.textBrowser_analysis.clear()

                def dataAnay(list):
                    maxnum = max(list) #最大
                    minnum = min(list) #最小
                    mean = np.mean(list) #平均
                    # median = np.median(list)
                    # 求众数
                    counts = np.bincount(list)
                    median = np.argmax(counts)
                    anayStr = "最大值为"+str(maxnum)+"，最小值为"+str(minnum)+"，平均数为"+str(int(mean))+"，众数为"+str(median)
                    return anayStr

                def noPos(self):
                    noeph = 0
                    eph = 0
                    for i in self.satlist:
                        if i < 4:
                            noeph += 1
                        if 4<i<6:
                            eph += 1
                    return "总计"+ str(noeph) + "个历元，用于定位的卫星数少于4颗，此时受到强干扰，无法定位。\n" + "总计"+ str(eph) + "个历元，用于定位的卫星数多余4颗少于6颗，此时受到弱干扰，定位质量较差。"

                if self.hasData == 1:
                    self.textBrowser_analysis.append("卫星数分析结果:" + "\n\n"
                                                     "点击图像绘制可生成本次飞行试验卫星导航模块的收星数变化图" + "\n\n"
                                                     "全程数据记录时间为" + self.ephdata[0]["time"] +"-"+self.ephdata[-1]["time"]+ "总计" + str(len(self.ephdata)) + "个历元\n"
                                                     "用于定位的卫星总计" + str(min(self.satlist)) + "-" +str(max(self.satlist)) + "颗。其" + dataAnay(self.satlist) + "\n"
                                                     "可见的GPS卫星总计" + str(min(self.gpslist)) + "-" +str(max(self.gpslist)) + "颗。其" + dataAnay(self.gpslist) + "\n"
                                                     "可见的BDS卫星总计" + str(min(self.bdslist)) + "-" +str(max(self.bdslist)) + "颗。其" + dataAnay(self.bdslist) + "\n\n"
                                                     + noPos(self) + "\n"
                                                     )
                else:
                    self.textBrowser_analysis.append("卫星数分析结果:" + "\n\n"
                                                     "未选择数据文件"
                                                     )
                self.display_1(3)
                # print(self.satlist)
                # print(self.gpslist)
                # print(self.bdslist)
                # print("卫星数")
            elif self.analysisOptions == "载噪比":
                self.textBrowser_analysis.clear()
                self.display_1(2)
                # TODO
                def getMaxMin(self):
                    if self.isGPScn0 is True:
                        num = 0
                        prn = []
                        maxCn0 = []
                        minCn0 = []
                        disableList = []
                        ableList = []
                        niceList = []
                        allList = []
                        for i in self.CN0List:
                            disabled = 0
                            able = 0
                            nice = 0
                            all = 0

                            if i == [0]:
                                pass
                            else:
                                cn0Max = max(i[1:])
                                temlist = []
                                temlist = i.copy()
                                for j in range(len(i)):
                                    if 0 < temlist[j] < 37:
                                        disabled += 1
                                    elif 37 <= temlist[j] < 40:
                                        able += 1
                                    elif temlist[j] > 40:
                                        nice += 1

                                    if temlist[j] == 0:
                                        temlist[j] = 999
                                    else:
                                        all += 1
                                cn0Min = min(temlist)
                                maxCn0.append(cn0Max)
                                minCn0.append(cn0Min)
                                disableList.append(disabled)
                                ableList.append(able)
                                niceList.append(nice)
                                allList.append(all)
                                prn.append(num)
                            num += 1
                        strPrn = ""
                        for i in range(len(prn)):
                            strPrn = strPrn + "卫星号为G" + str(prn[i]) + "的卫星，其载噪比最大值为" + str(maxCn0[i]) + "，最小值为" + str(minCn0[i]) + "。" + str(round(disableList[i]/allList[i] * 100,2)) + "%为不可用，"+ str(round(ableList[i]/allList[i] *100 ,2)) +"%为基本可用，"+ str(round(niceList[i]/allList[i] *100 ,2)) + "%为信号良好。\n"

                        return "\n数据记录的所有GPS卫星的载噪比的最大值为：" + str(max(maxCn0)) + "，最小值为：" + str(max(minCn0)) + "。\n" + strPrn
                    else:
                        return "\n当前无GPS卫星载噪比记录"

                def getBDS(self):
                    if self.isBDScn0 is True:
                        num = 0
                        prn = []
                        maxCn0 = []
                        minCn0 = []
                        disableList = []
                        ableList = []
                        niceList = []
                        allList = []
                        for i in self.bdCN0List:
                            disabled = 0
                            able = 0
                            nice = 0
                            all = 0

                            if i == [0]:
                                pass
                            else:
                                cn0Max = max(i[1:])
                                temlist = []
                                temlist = i.copy()
                                for j in range(len(i)):
                                    if 0 < temlist[j] < 37:
                                        disabled += 1
                                    elif 37 <= temlist[j] < 40:
                                        able += 1
                                    elif temlist[j] > 40:
                                        nice += 1

                                    if temlist[j] == 0:
                                        temlist[j] = 999
                                    else:
                                        all += 1
                                cn0Min = min(temlist)
                                maxCn0.append(cn0Max)
                                minCn0.append(cn0Min)
                                disableList.append(disabled)
                                ableList.append(able)
                                niceList.append(nice)
                                allList.append(all)
                                prn.append(num)
                            num += 1
                        strPrn = ""
                        for i in range(len(prn)):
                            strPrn = strPrn + "卫星号为C" + str(prn[i]) + "的卫星，其载噪比最大值为" + str(maxCn0[i]) + "，最小值为" + str(
                                minCn0[i]) + "。" + str(round(disableList[i] / allList[i] * 100, 2)) + "%为不可用，" + str(
                                round(ableList[i] / allList[i] * 100, 2)) + "%为基本可用，" + str(
                                round(niceList[i] / allList[i] * 100, 2)) + "%为信号良好。\n"

                        return "\n数据记录的所有北斗卫星的载噪比的最大值为：" + str(max(maxCn0)) + "，最小值为：" + str(max(minCn0)) + "。\n" + strPrn
                    else:
                        return "\n当前无北斗卫星载噪比记录。"



                self.display_1(3)
                self.textBrowser_analysis.append("载噪比分析结果\n\n"
                                                 "点击图像绘制可生成本次飞行试验卫星导航模块的载噪比变化图" + "\n\n"
                                                 "全程数据记录时间为" + self.ephdata[0]["time"] + "-" + self.ephdata[-1]["time"] + "总计" + str(len(self.ephdata)) + "个历元\n"
                                                 "对干扰进行分级评估，载噪比低于37时为不可用，37-40为基本可用，40以上为信号良好。\n"
                                                 + getMaxMin(self)
                                                 + getBDS(self)

                                                 )
            elif self.analysisOptions == "DOP值":
                self.textBrowser_analysis.clear()
                self.display_1(2)
                # TODO
                def anayDop(self):
                    hdopList = []
                    pdopList = []
                    vdopList = []
                    hnum = 0
                    hdisable = 0
                    hable = 0
                    hnice = 0
                    pnum = 0
                    pdisable = 0
                    pable = 0
                    pnice = 0
                    vnum = 0
                    vdisable = 0
                    vable = 0
                    vnice = 0
                    for i in self.ephdata:
                        if "HDOP" in i:
                            if float(i["HDOP"]) != 0:
                                hdopList.append(float(i["HDOP"]))
                            if 0 <= float(i["HDOP"]) < 6:
                                hnice += 1
                            elif 6 <= float(i["HDOP"]) < 10:
                                hable += 1
                            elif float(i["HDOP"]) >= 10:
                                hdisable += 1
                            hnum += 1
                        if "Pdop" in i:
                            if float(i["Pdop"]) != 0:
                                pdopList.append(float(i["Pdop"]))
                            if 0 <= float(i["Pdop"]) < 6:
                                pnice += 1
                            elif 6 <= float(i["Pdop"]) < 10:
                                pable += 1
                            elif float(i["Pdop"]) >= 10:
                                pdisable += 1
                            pnum += 1
                        if "Vdop" in i:
                            if float(i["Vdop"]) != 0:
                                vdopList.append(float(i["Vdop"]))
                            if 0 <= float(i["Vdop"]) < 6:
                                vnice += 1
                            elif 6 <= float(i["Vdop"]) < 10:
                                vable += 1
                            elif float(i["Vdop"]) >= 10:
                                vdisable += 1
                            vnum += 1
                    return "数据记录的所有历元中:\n" \
                           "PDOP最大值为" + str(max(pdopList)) + "，最小值为" + str(min(pdopList)) + "。PDOP不可用占比" + str(round(pdisable/pnum*100,2)) +"%，基本可用占比" + str(round(pable/pnum*100,2)) + "%,可信占比为" + str(round(pnice/pnum*100,2)) + "%。\n" \
                           "VDOP最大值为" + str(max(vdopList)) + "，最小值为" + str(min(vdopList)) + "。PDOP不可用占比" + str(round(vdisable/vnum*100,2)) +"%，基本可用占比" + str(round(vable/vnum*100,2)) + "%,可信占比为" + str(round(vnice/vnum*100,2)) + "%。\n" \
                           "HDOP最大值为" + str(max(hdopList)) + "，最小值为" + str(min(hdopList)) + "。PDOP不可用占比" + str(round(hdisable/hnum*100,2)) +"%，基本可用占比" + str(round(hable/hnum*100,2)) + "%,可信占比为" + str(round(hnice/hnum*100,2)) + "%。\n"

                self.display_1(3)
                self.textBrowser_analysis.append("DOP值分析结果:\n\n"
                                                 "点击图像绘制可生成本次飞行试验卫星导航模块的PDOP、VDOP、HDOP变化图" + "\n\n"
                                                 "全程数据记录时间为" + self.ephdata[0]["time"] +"-"+self.ephdata[-1]["time"]+ "总计" + str(len(self.ephdata)) + "个历元\n"
                                                 "对干扰进行分级评估，DOP值在10以上时为不可用，6-10为基本可用，6以下为可信。\n\n"
                                                 + anayDop(self)
                                                 )
            elif self.analysisOptions == "DOP可用性":
                self.textBrowser_analysis.clear()
                self.display_1(2)
                # TODO
                def getDOPusable(self):
                    Hnum = 0
                    Pnum = 0
                    Vnum = 0
                    for i in self.ephdata:
                        if "HDOP" in i and 0<float(i["HDOP"])<10:
                            Hnum += 1
                        if "Pdop" in i and 0<float(i["Pdop"])<10:
                            Pnum += 1
                        if "Vdop" in i and 0<float(i["Vdop"])<10:
                            Vnum += 1
                    return "该段时间的数据中:\n" \
                           "HDOP的可用性指标为" + str(round(Hnum/(1+len(self.ephdata))*100,2)) + "%，PDOP的可用性指标为" + str(round(Pnum/(1+len(self.ephdata))*100,2)) +"%，VDOP的可用性指标为" + str(round(Vnum/(1+len(self.ephdata))*100,2)) + "%。\n"

                self.display_1(3)
                self.textBrowser_analysis.append("DOP可用性分析结果：\n\n"
                                                 "点击图像绘制可生成本次飞行试验卫星导航模块的PDOP、VDOP、HDOP可用性图" + "\n\n"
                                                 "全程数据记录时间为" + self.ephdata[0]["time"] +"-"+self.ephdata[-1]["time"]+ "总计" + str(len(self.ephdata)) + "个历元\n"
                                                 "DOP可用性是指DOP可以使用的时间百分率，标志着系统某一指定区域内可以使用的导航服务的能力。\n"
                                                 "设定系统精度因子DOP值得标准阈值为10，计算系统服务的可用性指标。可用性指标越高说明系统导航服务能力越稳定，受到干扰越小。\n"
                                                 + getDOPusable(self)
                                                 )
            elif self.analysisOptions == "飞行轨迹":
                self.textBrowser_analysis.clear()
                self.display_1(2)
                # TODO
                def getDistance(self):

                    latStart = float(self.ephdata[0]["lat"][:2])+float(self.ephdata[0]["lat"][2:-1])/60
                    latEnd = float(self.ephdata[-1]["lat"][:2])+float(self.ephdata[-1]["lat"][2:-1])/60

                    lngStart = float(self.ephdata[0]["lng"][:3])+float(self.ephdata[0]["lng"][3:-1])/60
                    lngEnd = float(self.ephdata[-1]["lng"][:3])+float(self.ephdata[-1]["lng"][3:-1])/60

                    dlat = (latEnd-latStart)*111000
                    dlng = (lngEnd-lngStart)*111000

                    return "本次飞行试验的平面飞行距离为" + str(round(sqrt(dlat*dlat+dlng*dlng),2)) +"m。"

                self.display_1(3)
                self.textBrowser_analysis.append("飞行轨迹分析结果:" + "\n\n"
                                                 "点击图像绘制可生成本次飞行试验卫星导航模块的飞行轨迹图" + "\n\n"
                                                 "全程数据记录时间为" + self.ephdata[0]["time"] +"-"+self.ephdata[-1]["time"]+ "总计" + str(len(self.ephdata)) + "个历元\n"
                                                 "本次飞行试验的发射坐标：" + self.ephdata[0]["lat"] + "," + self.ephdata[0]["lng"] + "\n"
                                                 "本次飞行试验的落地坐标：" + self.ephdata[-1]["lat"] + "," + self.ephdata[-1]["lng"] + "\n"
                                                 + getDistance(self)
                                                 )
            elif self.analysisOptions == "定位有效性":
                self.textBrowser_analysis.clear()
                self.display_1(2)
                # TODO
                def getTyofPos(self):
                    num = 0
                    noNum = 0
                    sppNum = 0
                    dgpsNum = 0
                    for i in self.ephdata:
                        if int(i["posFlag"]) == 0:
                            noNum += 1
                        elif int(i["posFlag"]) == 1:
                            sppNum += 1
                        elif int(i["posFlag"]) == 2:
                            dgpsNum += 1
                        num += 1
                    return "本次飞行试验总计" + str(noNum) + "个历元无定位，占所有历元的"+ str(round(noNum/num*100,2)) + "%，\n"\
                           + str(sppNum) + "个历元为单点定位，占所有历元的" + str(round(sppNum/num*100,2)) + "%，\n" \
                           + str(dgpsNum) + "个历元为差分定位，占所有历元的" + str(round(dgpsNum/num*100,2)) + "%。"
                self.display_1(3)
                self.textBrowser_analysis.append("定位有效性分析结果:" + "\n\n"
                                                 "点击图像绘制可生成本次飞行试验卫星导航模块的定位有效性图" + "\n\n"
                                                 "全程数据记录时间为" + self.ephdata[0]["time"] + "-" + self.ephdata[-1]["time"] + "总计" + str(len(self.ephdata)) + "个历元\n"
                                                 + getTyofPos(self)
                                                 )
            elif self.analysisOptions == "飞行高度":
                self.textBrowser_analysis.clear()
                self.display_1(2)
                # TODO
                def getH(self):
                    hlist = []
                    for i in self.ephdata:
                        if int(i["posFlag"]) != 0:
                            hlist.append(float(i["h"][:-1]))
                    return "本次飞行试验，起飞的高度为：" + str(hlist[0]) + "m，落地点高度为：" + str(hlist[-1]) + "m，最大飞行高度为：" + str(max(hlist)) + "m，平均飞行高度为：" + str(round(np.mean(hlist),3)) + "m。"
                self.display_1(3)
                self.textBrowser_analysis.append("飞行高度分析结果:" + "\n\n"
                                                 "点击图像绘制可生成本次飞行试验卫星导航模块的飞行高度趋势图" + "\n\n"
                                                 "全程数据记录时间为" + self.ephdata[0]["time"] + "-" + self.ephdata[-1]["time"] + "总计" + str(len(self.ephdata)) + "个历元\n"
                                                 + getH(self)
                                                 )
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
            if self.hasData == 0:
                self.display_1(9)
            print("正在绘制图像")
            if self.analysisOptions == '卫星数':
                self.progressBar_1.setValue(10)
                # 用于定位的卫星数
                satx = list(range(1,len(self.satlist)+1))
                fig = plt.figure(num="定位用星数分析")
                ax1 = fig.add_subplot(111)
                ax1.set_title('Analysis of the number of satellites used for positioning')
                # ax1.set_title('用于定位的卫星数序列图')
                plt.xlabel('Number of measurements')
                # plt.xlabel('测量次数')
                # plt.ylabel('卫星数')
                plt.ylabel('Number of satellites')
                plt.scatter(satx, self.satlist,marker = 'o',s = 5,c = 'g')
                plt.ylim(-1, 15)
                plt.show()
                self.progressBar_1.setValue(40)
                #可见北斗卫星数
                BDSx = list(range(1, len(self.bdslist) + 1))
                fig = plt.figure(num="可见北斗卫星数分析")
                ax1 = fig.add_subplot(111)
                ax1.set_title('Analysis of the number of BDS satellites that can be observed')
                plt.xlabel('Number of measurements')
                plt.ylabel('Number of satellites')
                # ax1.set_title('可见BDS卫星数序列图')
                # plt.xlabel('测量次数')
                # plt.ylabel('卫星数')
                plt.scatter(BDSx, self.bdslist,marker = 'o',s = 5,c = 'r')
                plt.ylim(-1, 15)
                plt.show()
                self.progressBar_1.setValue(80)
                # 可见GPS卫星数
                GPSx = list(range(1, len(self.gpslist) + 1))
                fig = plt.figure(num="可见GPS卫星数分析")
                ax1 = fig.add_subplot(111)
                ax1.set_title('Analysis of the number of GPS satellites that can be observed')
                plt.xlabel('Number of measurements')
                plt.ylabel('Number of satellites')
                # ax1.set_title('可见GPS卫星数序列图')
                # plt.xlabel('测量次数')
                # plt.ylabel('卫星数')
                plt.scatter(GPSx, self.gpslist,marker = 'o',s = 5,c = 'b')
                plt.ylim(-1, 15)
                plt.show()
                self.progressBar_1.setValue(100)
                self.display_1(8)
            elif self.analysisOptions == "载噪比":
                if self.isGPScn0 is True:
                    fig = plt.figure(num="GPS载噪比分析")
                    ax1 = fig.add_axes([0.1, 0.1, 0.7, 0.75])
                    ax1.set_title('GPS Carrier Noise Ratio analysis')
                    # ax1.set_title('GPS载噪比分析')
                    prn = 0
                    for i in self.CN0List:
                        if i == [0]:
                            pass
                        else:
                            x = list(range(1, len(i)))
                            plt.scatter(x, i[1:],marker = '+',s = 5,label="G"+str(prn))
                            ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
                        prn+=1
                    self.progressBar_1.setValue(90)
                    plt.xlabel('Number of measurements')
                    plt.ylabel('CNR')
                    # plt.xlabel('测量次数')
                    # plt.ylabel('载噪比')
                    plt.show()
                if self.isBDScn0 is True:
                    fig = plt.figure(num="BDS载噪比分析")
                    ax1 = fig.add_axes([0.1, 0.1, 0.7, 0.75])
                    ax1.set_title('BDS Carrier Noise Ratio analysis')
                    # ax1.set_title('BDS载噪比分析')
                    prn = 0
                    for i in self.bdCN0List:
                        if i == [0]:
                            pass
                        else:
                            x = list(range(1, len(i)))
                            plt.scatter(x, i[1:],marker = '+',s = 5,label="C"+str(prn))
                            ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
                        prn+=1
                    self.progressBar_1.setValue(90)
                    plt.xlabel('Number of measurements')
                    plt.ylabel('CNR')
                    # plt.xlabel('测量次数')
                    # plt.ylabel('载噪比')
                    plt.show()
                self.progressBar_1.setValue(100)
            elif self.analysisOptions == "DOP值":
                self.progressBar_1.setValue(10)
                hdopList = []
                pdopList = []
                vdopList = []
                for i in self.ephdata:
                    if "HDOP" in i:
                        hdopList.append(float(i["HDOP"]))
                    if "Pdop" in i:
                        pdopList.append(float(i["Pdop"]))
                    if "Vdop" in i:
                        vdopList.append(float(i["Vdop"]))
                self.progressBar_1.setValue(40)
                # hdop绘制
                hdopx = list(range(1, len(hdopList) + 1))
                fig = plt.figure(num="HDOP分析")
                ax1 = fig.add_subplot(111)
                ax1.set_title('HDOP analysis')
                plt.xlabel('Number of measurements')
                plt.ylabel('HDOP')
                # ax1.set_title('HDOP分析')
                # plt.xlabel('测量次数')
                # plt.ylabel('HDOP')
                plt.scatter(hdopx, hdopList,marker = 'o',s = 5,c = 'r')
                plt.show()
                self.progressBar_1.setValue(60)
                # pdop绘制
                pdopx = list(range(1, len(pdopList) + 1))
                fig = plt.figure(num="PDOP分析")
                ax1 = fig.add_subplot(111)
                ax1.set_title('PDOP analysis')
                plt.xlabel('Number of measurements')
                plt.ylabel('PDOP')
                # ax1.set_title('PDOP分析')
                # plt.xlabel('测量次数')
                # plt.ylabel('PDOP')
                plt.scatter(pdopx, pdopList,marker = 'o',s = 5,c = 'g')
                # print(pdopList)
                plt.show()
                self.progressBar_1.setValue(80)
                # vdop绘制
                vdopx = list(range(1, len(vdopList) + 1))
                fig = plt.figure(num="VDOP分析")
                ax1 = fig.add_subplot(111)
                ax1.set_title('VDOP analysis')
                plt.xlabel('Number of measurements')
                plt.ylabel('VDOP')
                # ax1.set_title('VDOP分析')
                # plt.xlabel('测量次数')
                # plt.ylabel('VDOP')
                plt.scatter(vdopx, vdopList,marker = 'o',s = 5,c = 'b')
                plt.show()
                self.progressBar_1.setValue(100)
            elif self.analysisOptions == "DOP可用性":
                Hnum = 0
                Pnum = 0
                Vnum = 0
                for i in self.ephdata:
                    if "HDOP" in i and 0<float(i["HDOP"])<10:
                        Hnum += 1
                    if "Pdop" in i and 0<float(i["Pdop"])<10:
                        Pnum += 1
                    if "Vdop" in i and 0<float(i["Vdop"])<10:
                        Vnum += 1
                Hava = round(Hnum/(1+len(self.ephdata))*100,2)
                Pava = round(Pnum/(1+len(self.ephdata))*100,2)
                Vava = round(Vnum/(1+len(self.ephdata))*100,2)
                dop = [Hava, Pava, Vava]
                def millions(x, pos):
                    """The two args are the value and tick position."""
                    return '{:1.2f}%'.format(x)

                fig0 = plt.figure(num="DOP可用性指标")
                ax0 = fig0.add_axes([0.18, 0.1, 0.7, 0.75])
                # Use automatic FuncFormatter creation
                ax0.yaxis.set_major_formatter(millions)
                ax0.bar(['HDOP', 'PDOP', 'VDOP'], dop)
                ax0.set_title('DOP availability metrics')
                plt.xlabel('Category')
                plt.ylabel('Percentage')
                # ax.set_title('DOP可用性分析')
                # plt.xlabel('类别')
                # plt.ylabel('百分比')
                plt.show()
            # elif self.analysisOptions == "飞行轨迹":
            #     self.progressBar_1.setValue(10)
            #     latList = []
            #     lngList = []
            #     for i in self.ephdata:
            #         if "lat" in i:
            #             du = i["lat"][:2]
            #             fen = i["lat"][2:-1]
            #             # print(float(i["lat"][:-1]))
            #             if int(i["posFlag"]) != 0:
            #                 latList.append(float(du)+float(fen)/60)
            #         if "lng" in i:
            #             du = i["lng"][:3]
            #             fen = i["lng"][3:-1]
            #             # print(float(i["lat"][:-1]))
            #             if int(i["posFlag"]) != 0:
            #                 lngList.append(float(du)+float(fen)/60)
            #     self.progressBar_1.setValue(60)
            #     pts = GeoSeries([Point(x, y) for x, y in zip(latList, lngList)])
            #     pts.plot(marker='+', color='red', markersize=5)
            #     plt.title("Flight trajectory")
            #     plt.xlabel('Latitude')
            #     plt.ylabel('Longitude')
            #     plt.xlim(min(latList) - 0.00001, max(latList) + 0.00001)
            #     plt.ylim(min(lngList) - 0.00001, max(lngList) + 0.00001)
            #     # ptj.plot()
            #     # x刻度数值旋转90°
            #     # plt.xticks(rotation=90)
            #     plt.grid("on")
            #     plt.show()
            #     self.progressBar_1.setValue(100)
            elif self.analysisOptions == "定位有效性":
                num = 0
                noNum = 0
                sppNum = 0
                dgpsNum = 0
                for i in self.ephdata:
                    if int(i["posFlag"]) == 0:
                        noNum+=1
                    elif int(i["posFlag"]) == 1:
                        sppNum+=1
                    elif int(i["posFlag"]) == 2:
                        dgpsNum+=1
                    num+=1
                fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"),num="定位有效性")
                recipe = [str(noNum)+"  Not-positioned",
                          str(sppNum)+" SPP",
                          str(dgpsNum)+" DGPS"]
                # recipe = [str(noNum) + "  未定位",
                #           str(sppNum) + " 单点定位",
                #           str(dgpsNum) + " 差分定位"]
                data = [float(x.split()[0]) for x in recipe]
                ingredients = [x.split()[-1] for x in recipe]
                def func(pct, allvals):
                    absolute = int(pct / 100. * np.sum(allvals))
                    return "{:.1f}%\n({:d})".format(pct, absolute)
                wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                                  textprops=dict(color="w"))
                ax.legend(wedges, ingredients,
                          title="The type of positioning",
                          loc="center left",
                          bbox_to_anchor=(1, 0, 0.5, 1))
                # ax.legend(wedges, ingredients,
                #           title="定位类型",
                #           loc="center left",
                #           bbox_to_anchor=(1, 0, 0.5, 1))
                plt.setp(autotexts, size=8, weight="bold")
                ax.set_title("Positioning effectiveness")
                # ax.set_title("定位有效性")
                plt.show()
            elif self.analysisOptions == "飞行高度":
                hlist = []
                for i in self.ephdata:
                    if int(i["posFlag"]) != 0:
                        hlist.append(float(i["h"][:-1]))
                hx = list(range(1,len(hlist)+1))
                fig = plt.figure(num="飞行高度")
                ax1 = fig.add_subplot(111)
                ax1.set_title('Flight altitude')
                plt.xlabel('Number of measurements')
                plt.ylabel('Flight altitude/m')
                # ax1.set_title('飞行高度')
                # plt.xlabel('测量次数')
                # plt.ylabel('飞行高度/m')
                plt.scatter(hx, hlist,marker = 'o',s = 5,c = 'r')
                plt.show()
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
        # self.radioButton_flightPath.setText(_translate("MainWindow", "飞行轨迹"))
        self.radioButton_posEffi.setText(_translate("MainWindow", "定位有效性分析"))
        self.radioButton_flyH.setText(_translate("MainWindow", "飞行高度"))
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

        self.textBrowser_analysis.append("欢迎使用干扰监测与评估软件" + "\n"
                                         "本软件支持NMEA 0183格式数据输入，点击选择文件即可选定待分析文件" + "\n"
                                         "选定文件之后，右侧会显示当前文件的数据参数" + "\n"
                                         "本软件支持卫星数、载噪比、DOP值、DOP可用性、定位有效性、飞行高度分析" + "\n"
                                         "文件载入后，选择左侧分析方法，点击开始处理即可显示分析报告，点击图像绘制即可生成相关图像" + "\n")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


