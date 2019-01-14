import sys
import os.path
import unreal_engine as ue
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
brush2 = SlateBrush(ResourceName=ue.get_content_dir() + 'Scripts/UI/Rename.png', ImageSize=Vector2D(X=50, Y=50))
# register the brush
style.set('ImageBrush001', brush2)
# register the new style
style.register()

# this is called whenever you select the SimpleMenuExtension entry
def dumb():
   ue.log('HELLO WORLD')

# this generates the menu entries
def open_menu(menu):
   menu.begin_section('test1', 'test2')
   menu.add_menu_entry('LoadUI', 'QtDesigner에서 만든 UI 불러오기', lambda: ue.exec('/QtSample/PyQt_LoadUI.py'))
   menu.add_menu_entry('AnimationTiles', 'PySide 애니메이션 예제', lambda: ue.exec('/QtSample/PySide_animatedtiles.py'))
   menu.add_menu_entry('Bar 3D', 'Bar 3D', lambda: ue.exec('/QtSample/PySide_bars3D.py'))
   menu.add_menu_entry('Shooting Game', 'Shooting Game', lambda: ue.exec('/QtSample/PySide_shootingGame.py'))
   menu.add_menu_entry('ThumbNail', 'ThumbNail', lambda: ue.exec('/QtSample/PySide_thumbnail.py'))

   menu.end_section()

# this fills the toolbar
def fill_toolbar(toolbar):
	icon1 = FSlateIcon('PyStyle', 'SolidBrush001')
	icon2 = FSlateIcon('PyStyle', 'ImageBrush001')
	toolbar.add_tool_bar_button('Renamer', 'Renamer', 'Button001 tooltip', icon2, lambda: ue.exec('/Naong2/Renamer_Replace.py'))
	toolbar.add_tool_bar_button('PythonScript1', 'PythonScript1', '테스트하기 좋으라고 만든 버튼', icon1, lambda: ue.exec('PythonScript1.py'))

#그냥 일반 메뉴에 들어간거
ue.add_menu_extension('TestMenu 01', dumb)

ue.add_menu_bar_extension('PyQt Samples', open_menu)

ue.add_tool_bar_extension('SimpleToolBarExtension', fill_toolbar)