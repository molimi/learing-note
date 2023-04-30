# -*- coding: utf-8 -*-
"""
@author: CarpeDiem
@date: 23/4/30
@version: 0.1
@description: PyQt5初步使用
@Idea: Demo of GUI by PyQt5
"""
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 初识化界面
    MainWindow = QtWidgets.QWidget()        # 生成一个主窗口
    MainWindow.show()                       # 显示主窗口
    sys.exit(app.exec_())                   # 在线程中退出  