

## QtDesigner에서 만든 ui 불러오는 예제

import ueqt
import os
from PyQt5 import QtCore, QtWidgets, QtGui, uic
import unreal_engine as ue

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(ue.get_content_dir() + 'Scripts/UI/qtdesigner_t01.ui', self)

widget = MyWindow()
widget.resize(800, 600)
widget.show()

root_window = ue.get_editor_window()
root_window.set_as_owner(widget.winId())