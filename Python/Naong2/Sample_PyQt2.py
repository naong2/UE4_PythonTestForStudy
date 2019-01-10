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

#스켈레탈 담아놓을 리스트 하나 만듬
skeletal_mappings = {}


#선택한 녀석 리임포트하는 곳
def selected_skeletal_mesh(item):
    uobject = skeletal_mappings[item.data()]
    ue.log('리임포트 준비완료!: ' + uobject.get_name())
    uobject.asset_reimport()

app = QApplication.instance()
if app is None:
    app = QApplication([])
else:
    print("앱이 이미 실행중입니다.~~~~~!!!!!~~~~")

win = QWidget()
win.setWindowTitle('Unreal Engine 4 skeletal meshes reimporter')

#위젯을 품은 QList 하나 만듬
wlist = QListWidget(win)
for asset in ue.get_assets_by_class('SkeletalMesh'):
    #QList에 걸려든 녀석들 하나씩 밀어 넣어주는 곳
    wlist.addItem(asset.get_name())
    skeletal_mappings[asset.get_name()] = asset

# 클릭하면 실행
wlist.clicked.connect(selected_skeletal_mesh)

wlist.show()
win.show()
