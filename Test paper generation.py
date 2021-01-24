# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/19
# @Author : Baiyuan Qiu(Bugmaker)
# @Github : https://github.com/bugmaker2
# @File : Test paper generation.py
# @Software: Notepad++

import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import csv
import random

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 布局
        # # 总体布局
        self.setGeometry(300, 300, 1400, 750)
        self.setWindowTitle(u'组卷系统')
        self.setWindowIcon(QIcon('paper.png'))


        # # 菜单栏
        menubar = self.menuBar()
        # # # 题库选择
        choose_database = menubar.addMenu("题库选择")
        
        self.local_data = QAction('本地题库', self, checkable=True)
        self.local_data.setChecked(True)
        self.local_data.toggled.connect(self.local_data_choosed)
        choose_database.addAction(self.local_data)
        
        self.online_data = QAction('在线题库', self, checkable= True)
        self.online_data.setChecked(False)
        self.online_data.toggled.connect(self.online_data_choosed)
        choose_database.addAction(self.online_data)
        # # # 帮助
        help_menu = menubar.addMenu("帮助")
        
        self.tips = QAction('帮助', self)
        self.tips.triggered.connect(self.something_helpful)
        help_menu.addAction(self.tips)
        
        self.info = QAction('联系作者', self)
        self.info.triggered.connect(self.author)
        help_menu.addAction(self.info)
        
        
        # # 单选10*5
        title = QLabel(self)
        title.setText('一、单选题（每题5分，共10题）')
        title.adjustSize()
        title.move(60,40)
        for i in range(10):
            # 用exec批量生成题目
            content = "self.title{} = QLabel(self)".format(str(i))
            content += "\nself.title{}.setText('default')".format(str(i))
            content += "\nself.title{}.move(60,{})".format(str(i),(i+1)*60+20)
            content += "\nself.title{}.adjustSize()".format(str(i))
            content += "\nself.bg{} = QButtonGroup(self)".format(str(i))
            exec(content)
            for j in range(4):
                content = "self.but{} = QRadioButton('default',self)".format(str(i)+str(j))
                content += "\nself.but{}.move({},{})".format(str(i)+str(j),(j+1)*150-40,(i+1)*60+45)
                content += "\nself.bg{}.addButton(self.but{})".format(str(i),str(i)+str(j))
                exec(content)
                
                
        # # 填空3*10
        title = QLabel(self)
        title.setText('二、填空题（每题10分，共3题）')
        title.adjustSize()
        title.move(710,40)
        
        for i in range(3):
            # 用exec批量生成题目
            content = "self.cloze_title{} = QLabel(self)".format(str(i))
            content += "\nself.cloze_title{}.setText('default')".format(str(i))
            content += "\nself.cloze_title{}.move(710,{})".format(str(i),(i+1)*60+20)
            
            content += "\nself.cloze_ans{} = QLineEdit(self)".format(str(i))
            content += "\nself.cloze_ans{}.move(710,{})".format(str(i),(i+1)*60+50)
            content += "\nself.cloze_ans{}.resize(70,20)".format(str(i))
            exec(content)
        
        
        # # 判断2*10
        title = QLabel(self)
        title.setText('三、判断题（每题10分，共2题）')
        title.adjustSize()
        title.move(710,400)
        
        for i in range(2):
            content = "self.binery_choice{} = QLabel(self)".format(str(i))
            content += "\nself.binery_choice{}.setText('default')".format(str(i))
            content += "\nself.binery_choice{}.move(710,{})".format(str(i),(i+1)*60+380)
            exec(content)
        self.bc1 = QButtonGroup(self)
        self.bc2 = QButtonGroup(self)
        self.bc1_ansT = QRadioButton('T',self)
        self.bc1_ansF = QRadioButton('F',self)
        self.bc2_ansT = QRadioButton('T',self)
        self.bc2_ansF = QRadioButton('F',self)
        self.bc1.addButton(self.bc1_ansT)
        self.bc1.addButton(self.bc1_ansF)
        self.bc2.addButton(self.bc2_ansT)
        self.bc2.addButton(self.bc2_ansF)
        self.bc1_ansT.move(730,470)
        self.bc1_ansF.move(790,470)
        self.bc2_ansT.move(730,530)
        self.bc2_ansF.move(790,530)
        
        
        # # 组卷交卷评分
        self.make_paper = QPushButton("组卷",self)
        self.make_paper.clicked.connect(self.make)
        self.make_paper.move(420,680)
        self.btn_submit = QPushButton(u"交卷",self)
        self.btn_submit.clicked.connect(self.submit)
        self.btn_submit.move(550,680)
        
        self.flag = False
        
        # # 显示
        self.show()
        
    # 实现菜单栏单选
    def local_data_choosed(self):
        if self.local_data.isChecked():
            self.online_data.setChecked(False)
        else:
            self.online_data.setChecked(True)
    def online_data_choosed(self):
        if self.online_data.isChecked():
            self.local_data.setChecked(False)
        else:
            self.local_data.setChecked(True)
            
    # 实现菜单栏帮助选项
    def something_helpful(self):
        QMessageBox.information(self, "帮助信息", "点击组卷可以生成试卷\n点击交卷提交并评分\n线上题库将连接作者云服务器，服务在课程完成评分后关闭\n阅读README.md文件获取更多信息")
    def author(self):
        QMessageBox.information(self, "作者信息", "仇白渊\n2018011217014\nhttps://github.com/bugmaker2\n此作品为Python课程课设")
        
    # 组成试卷
    def make(self):
        self.flag = True
        if self.local_data.isChecked():
            self.make_from_local()
        elif self.online_data.isChecked():
            self.make_from_online()
            
    def make_from_local(self):
        self.ans = [] # 用于记录正确答案
        # 单选题组卷
        with open('single choice.csv','r') as f:
            reader = csv.reader(f)
            all_question = list(reader)
            ques_id = random.sample(range(len(all_question)),10) # 随机选取10题单选
            n = 0
            for i in ques_id:
                content = "self.title{}.setText(str({})+'.'+all_question[i][0])".format(str(n),n+1)
                content += "\nself.title{}.adjustSize()".format(str(n))
                # 打乱选项次序
                choice_id = random.sample(range(4),4)
                m = 0
                for abcd in choice_id:
                    content += "\nself.but{}.setText(all_question[i][{}])".format(str(n)+str(m),abcd+1)
                    content += "\nself.but{}.adjustSize()".format(str(n)+str(m))
                    m += 1
                n += 1
                exec(content)
                # 添加正确答案
                self.ans.append(all_question[i][5])
                
        # 填空题组卷
        with open('cloze.csv','r') as f:
            reader = csv.reader(f)
            all_question = list(reader)
            ques_id = random.sample(range(len(all_question)),3)
            n = 0
            
            for i in ques_id:
                content = "self.cloze_title{}.setText(all_question[i][0])".format(str(n))
                content += "\nself.cloze_title{}.adjustSize()".format(str(n))
                content += "\nself.cloze_ans{}.setText('')".format(str(n))
                exec(content)
                self.ans.append(all_question[i][1])
                n += 1
        
        # 判断题组卷
        with open('binery choice.csv','r') as f:
            reader = csv.reader(f)
            all_question = list(reader)
            ques_id = random.sample(range(len(all_question)),2)
            self.binery_choice0.setText(all_question[ques_id[0]][0])
            self.binery_choice1.setText(all_question[ques_id[1]][0])
            self.binery_choice0.adjustSize()
            self.binery_choice1.adjustSize()
            
            self.ans.append(all_question[ques_id[0]][1])
            self.ans.append(all_question[ques_id[1]][1])

    def make_from_online(self):
        QMessageBox.information(self, "Warnning", "此功能仅作为展示\nsocket服务端已关闭（忘了续费了）")
        
        
    # 交卷并评分
    def submit(self):
        # 算分
        if self.complete() and self.flag:
            reply = QMessageBox.question(self, 'Message',"确定交卷吗？",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.count()
        elif self.flag:
            QMessageBox.information(self, 'Warning',"还有题目没做完！")
        else:
            QMessageBox.information(self,'Warnning',"请先组卷")
        
    def complete(self):
        # 判断是否写完
        flag = True
        if not(self.but00.isChecked() or self.but01.isChecked() or self.but02.isChecked() or self.but03.isChecked()): return False
        if not(self.but10.isChecked() or self.but11.isChecked() or self.but12.isChecked() or self.but13.isChecked()): return False
        if not(self.but20.isChecked() or self.but21.isChecked() or self.but22.isChecked() or self.but23.isChecked()): return False
        if not(self.but30.isChecked() or self.but31.isChecked() or self.but32.isChecked() or self.but33.isChecked()): return False
        if not(self.but40.isChecked() or self.but41.isChecked() or self.but42.isChecked() or self.but43.isChecked()): return False
        if not(self.but50.isChecked() or self.but51.isChecked() or self.but52.isChecked() or self.but53.isChecked()): return False
        if not(self.but60.isChecked() or self.but61.isChecked() or self.but62.isChecked() or self.but63.isChecked()): return False
        if not(self.but70.isChecked() or self.but71.isChecked() or self.but72.isChecked() or self.but73.isChecked()): return False
        if not(self.but80.isChecked() or self.but81.isChecked() or self.but82.isChecked() or self.but83.isChecked()): return False
        if not(self.but90.isChecked() or self.but91.isChecked() or self.but92.isChecked() or self.but93.isChecked()): return False
        if self.cloze_ans0.text() == "": return False
        if self.cloze_ans1.text() == "": return False
        if self.cloze_ans2.text() == "": return False
        if not(self.bc1_ansT.isChecked() or self.bc1_ansF.isChecked()): return False
        if not(self.bc2_ansT.isChecked() or self.bc2_ansF.isChecked()): return False
        
        return flag
        
    def count(self):
        self.score = 0
        print(self.bg0.checkedButton().text())
        for i in range(10):
            content = "self.bg{}.checkedButton().text()==self.ans[i]".format(i)
            if eval(content):
                self.score += 5
        if self.cloze_ans0.text()==self.ans[10]: self.score += 10
        if self.cloze_ans1.text()==self.ans[11]: self.score += 10
        if self.cloze_ans2.text()==self.ans[12]: self.score += 10
        if self.bc1.checkedButton().text()==self.ans[13]: self.score += 10
        if self.bc2.checkedButton().text()==self.ans[14]: self.score += 10
        if self.score >= 85:
            QMessageBox.information(self,'Score',"最终得分为："+str(self.score)+"\n太棒啦！继续努力学习嗷")
        else:
            QMessageBox.information(self,'Score',"最终得分为："+str(self.score)+"\n没有满绩！还要加油嗷")

        
    
    def closeEvent(self, event):
        # 关闭提示
        reply = QMessageBox.question(self, 'Message',"确定退出吗？",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
    


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())