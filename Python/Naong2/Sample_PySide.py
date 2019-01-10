import ueqt
from PySide2 import QtCore, QtWidgets, QtGui
import unreal_engine as ue

from unreal_engine import FARFilter

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.vertical = QtWidgets.QVBoxLayout()
        self.scroll = QtWidgets.QScrollArea()
        self.content = QtWidgets.QWidget()
        self.scroll.setWidget(self.content)
        self.scroll.setWidgetResizable(True)
        self.layout = QtWidgets.QVBoxLayout()

        self.content.setLayout(self.layout)
        self.vertical.addWidget(self.scroll)
        self.setLayout(self.vertical)

widget = MyWidget()
widget.resize(800, 600)
widget.show()

root_window = ue.get_editor_window()
root_window.set_as_owner(widget.winId())