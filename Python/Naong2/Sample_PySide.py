import ueqt
from PySide2 import QtCore, QtWidgets, QtGui
import unreal_engine as ue
import ue_asyncio

from unreal_engine import FARFilter

_filter = FARFilter()
_filter.class_names = ['SkeletalMesh']

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.vertical = QtWidgets.QVBoxLayout()
        self.scroll = QtWidgets.QScrollArea()
        self.content = QtWidgets.QWidget()
        self.scroll.setWidget(self.content)
        self.scroll.setWidgetResizable(True)
        self.layout = QtWidgets.QVBoxLayout()

        for asset_data in ue.get_assets_by_filter(_filter, True):
            try:
                thumbnail = asset_data.get_thumbnail()
            except:
                continue
            label = QtWidgets.QLabel()
            data = thumbnail.get_uncompressed_image_data()
            image = QtGui.QImage(data, 128, 128, QtGui.QImage.Format_RGB32)
            label.setPixmap(QtGui.QPixmap.fromImage(image).scaled(128, 128))
            self.layout.addWidget(label)

        self.content.setLayout(self.layout)
        self.vertical.addWidget(self.scroll)
        self.setLayout(self.vertical)

widget = MyWidget()
widget.resize(800, 600)
widget.show()

root_window = ue.get_editor_window()
root_window.set_as_owner(widget.winId())