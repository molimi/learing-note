"""
@author: CarpeDiem
@date: 23/5/1
@version: 0.1
@description: PyQt5初步使用
@Idea: Demo of GUI by PyQt5
"""
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_test03 import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)        # 创建应用程序对象
    main_window = QMainWindow()         # 创建主窗口
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()                  # 显示主窗口
    sys.exit(app.exec_())               # 在主线程中退出 