#########Tutorial



import unreal_engine as ue 
from unreal_engine import SWindow, STextBlock, SButton, SVerticalBox, SEditableTextBox, UObject


def OKClicked():
	assets = ue.get_selected_assets()
	for i in range(0, len(assets)):
		#풀경로
		AssetFullName = assets[i].get_path_name()
		#이름
		AssetNameOnly = assets[i].get_name()

		AssetPathLength = len(AssetFullName) - (len(AssetNameOnly)*2+1)

		#경로만 
		AssetPathNameOnly = AssetFullName[0:AssetPathLength]

		#최종 변경할 에셋 이름
		LastAssetName = AssetPathNameOnly + myinput.get_text() + AssetNameOnly

		ue.rename_asset(AssetFullName, LastAssetName)

		ue.log(AssetFullName)





	

#mywindow = SWindow(client_size=(300,300))
mywindow = SWindow(is_topmost_window=True).resize(300,300).set_title('리네임툴')
myvertical = SVerticalBox()
myinput = SEditableTextBox()

mytext = STextBlock(text='추가할 문자열을 적어주세요')

mybutton = SButton(v_align=2,h_align=2).set_content(STextBlock(text='OK'))
mybutton.bind_on_clicked(OKClicked)


#버티컬에 항목 추가하기
myvertical.add_slot(mytext)
myvertical.add_slot(myinput)
myvertical.add_slot(mybutton)

mywindow.set_content(myvertical)

