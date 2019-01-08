import sys
import os.path
import unreal_engine as ue

#sys.path.insert ( 0 , 'C:/Users/naong/AppData/Local/Programs/Python/Python36/Lib/site-packages' )
#import autopep8

from unreal_engine import FSlateIcon, FSlateStyleSet, FLinearColor
from unreal_engine.structs import SlateBrush, SlateColor, Vector2D

# this code must be in ue_site.py, extenders must be  registered during editor startup phase !!!
# we create a new StyleSet to register a new Icon
# create a new styleset
style = FSlateStyleSet('PyStyle')
# allocate a solid color brush (check here https://docs.unrealengine.com/latest/INT/API/Runtime/SlateCore/Styling/FSlateBrush/index.html)
brush = SlateBrush(TintColor=SlateColor(SpecifiedColor=FLinearColor(1, 0, 0, 1)))
# register the brush in the 'PyStyle' StyleSet
style.set('SolidBrush001', brush)
# allocate a brush image (best image size for toolbar is 64x64)
# Note: pass a path to a valid image file
#brush2 = SlateBrush(ResourceName='D:/PythonTest/ChessBoard.png', ImageSize=Vector2D(X=32, Y=32))
# register the brush
#style.set('ImageBrush001', brush2)
# register the new style
style.register()

# this is called whenever you select the SimpleMenuExtension entry
def dumb():
   ue.log('HELLO WORLD')

# this generates the menu entries
def open_menu(menu):
   menu.begin_section('test1', 'test2')
   menu.add_menu_entry('Renamer Assets', 'Renamer Assets', lambda: ue.exec('Renamer_Tutorial.py'))
   menu.end_section()

# this fills the toolbar
def fill_toolbar(toolbar):
	icon1 = FSlateIcon('PyStyle', 'SolidBrush001')
	icon2 = FSlateIcon('PyStyle', 'ImageBrush001')
	toolbar.add_tool_bar_button('리네임툴', '리네임툴', 'Button001 tooltip', icon1, lambda: ue.exec('Renamer_Replace.py'))
	#toolbar.add_tool_bar_button('리네임툴', '리네임툴', '아직 Prefix 추가만 사용 가능', icon2, lambda: ue.exec('Renamer_Tutorial.py'))

ue.add_menu_extension('Python Tools Menu', dumb)

ue.add_menu_bar_extension('Python Tools MenuBar', open_menu)

ue.add_tool_bar_extension('Python Tools ToolBar', fill_toolbar)