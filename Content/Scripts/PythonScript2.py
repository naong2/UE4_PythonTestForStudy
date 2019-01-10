from PyQt5.QtWidgets import QApplication, QWidget, QListWidget
import unreal_engine as ue

app = QApplication.instance()
if app is None:
    app = QApplication([])
else:
    print("App already running.")

win = QWidget()
win.setWindowTitle('Test Window')

wlist = QListWidget(win)

wlist.show()
win.show()
