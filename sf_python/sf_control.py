# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sf_control.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from hw_control import hw


class Ui_sfController(object):

    def setupUi(self, sfController):
        sfController.setObjectName("sfController")
        sfController.resize(800, 600)
        self.btns = QtWidgets.QWidget(sfController)
        self.btns.setObjectName("btns")

        self.start_btn = QtWidgets.QPushButton(self.btns)
        self.start_btn.setGeometry(QtCore.QRect(80, 90, 191, 81))
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(hw.start)

        self.stop_btn = QtWidgets.QPushButton(self.btns)
        self.stop_btn.setGeometry(QtCore.QRect(520, 90, 191, 81))
        self.stop_btn.setObjectName("stop_btn")
        self.stop_btn.clicked.connect(hw.stop)

        self.pathA_btn = QtWidgets.QPushButton(self.btns)
        self.pathA_btn.setGeometry(QtCore.QRect(80, 270, 191, 81))
        self.pathA_btn.setObjectName("pathA_btn")
        self.pathA_btn.clicked.connect(hw.path_A)

        self.pathB_btn = QtWidgets.QPushButton(self.btns)
        self.pathB_btn.setGeometry(QtCore.QRect(300, 270, 191, 81))
        self.pathB_btn.setObjectName("pathB_btn")
        self.pathB_btn.clicked.connect(hw.path_B)

        self.pathC_btn = QtWidgets.QPushButton(self.btns)
        self.pathC_btn.setGeometry(QtCore.QRect(520, 270, 191, 81))
        self.pathC_btn.setObjectName("pathC_btn")
        self.pathC_btn.clicked.connect(hw.path_C)

        self.s_up_btn = QtWidgets.QPushButton(self.btns)
        self.s_up_btn.setGeometry(QtCore.QRect(190, 390, 191, 81))
        self.s_up_btn.setObjectName("s_up_btn")
        self.s_up_btn.clicked.connect(hw.speed_up)


        self.s_down_btn = QtWidgets.QPushButton(self.btns)
        self.s_down_btn.setGeometry(QtCore.QRect(410, 390, 191, 81))
        self.s_down_btn.setObjectName("s_down_btn")
        self.s_down_btn.clicked.connect(hw.speed_down)

        sfController.setCentralWidget(self.btns)
        self.statusbar = QtWidgets.QStatusBar(sfController)
        self.statusbar.setObjectName("statusbar")
        sfController.setStatusBar(self.statusbar)

        self.retranslateUi(sfController)
        QtCore.QMetaObject.connectSlotsByName(sfController)

    def retranslateUi(self, sfController):
        _translate = QtCore.QCoreApplication.translate
        sfController.setWindowTitle(_translate("sfController", "MainWindow"))
        self.start_btn.setText(_translate("sfController", "Start"))
        self.stop_btn.setText(_translate("sfController", "Stop"))
        self.pathA_btn.setText(_translate("sfController", "A"))
        self.pathB_btn.setText(_translate("sfController", "B"))
        self.pathC_btn.setText(_translate("sfController", "C"))
        self.s_up_btn.setText(_translate("sfController", "Speed Up"))
        self.s_down_btn.setText(_translate("sfController", "Speed Down"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sfController = QtWidgets.QMainWindow()
    ui = Ui_sfController()
    ui.setupUi(sfController)
    sfController.show()
    sys.exit(app.exec_())
