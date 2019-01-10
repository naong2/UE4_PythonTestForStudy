from PyQt5.QtWidgets import QApplication, QWidget, QListWidget
import unreal_engine as ue
import sys
import traceback

def ue_exception(_type, value, back):
    ue.log_error(value)
    tb_lines = traceback.format_exception(_type, value, back)
    for line in tb_lines:
        ue.log_error(line)

sys.excepthook = ue_exception

skeletal_mappings = {}

def selected_skeletal_mesh(item):
    uobject = skeletal_mappings[item.data()]
    ue.log('Ready to reimport: ' + uobject.get_name())
    uobject.asset_reimport()

app = QApplication([])

win = QWidget()
win.setWindowTitle('Unreal Engine 4 skeletal meshes reimporter')

wlist = QListWidget(win)
for asset in ue.get_assets_by_class('SkeletalMesh'):
    wlist.addItem(asset.get_name())
    skeletal_mappings[asset.get_name()] = asset

wlist.clicked.connect(selected_skeletal_mesh)
wlist.show()

win.show()