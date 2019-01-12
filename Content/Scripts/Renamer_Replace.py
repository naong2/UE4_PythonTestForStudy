#
# 2018.12.19
# mailto: naong2@gmail.com
#
import unreal_engine as ue
from unreal_engine import SWindow, SButton,SEditableTextBox, STextBlock, SGridPanel, SHorizontalBox, SCheckBox

assets = 0

#버튼 클릭하면 실행하는 부분
def OKclicked():
    ret = ue.message_dialog_open(ue.APP_MSG_TYPE_YES_NO, "실행할까요? \n돌이킬 수 없습니다\n퇴사해야할지도 몰라요\n업데이트는 다 받고 하는거죠?\n\n전 책임안집니다? \n동의하면 YES")
    if ret == ue.APP_RETURN_TYPE_YES:
        assets = ue.get_selected_assets()
        for i in range(0, len(assets)):

            AssetFullPath = assets[i].get_path_name()
            AssetName = assets[i].get_name()

            #폴더 경로까지의 문자열 길이
            AssetPathOnlyLenth = len(AssetFullPath) - (len(assets[i].get_name())*2 +1)
            AssetPathNameOnly = AssetFullPath[0:AssetPathOnlyLenth]

            if replace_checkbox.is_checked():
                #문자열 교체
                if inputbox_replace.get_text() == '':
                    ret = ue.message_dialog_open(ue.APP_MSG_TYPE_OK, "대체할 기존 문자열이 공백이면 실행할 수 없습니다.")
                    return                
                else:
                    AssetName = AssetName.replace(inputbox_replace.get_text(), inputbox_prefix.get_text())
                    RenamedAssetName = AssetPathNameOnly + AssetName
                 
            else:
                #추가
                if suffix_checkbox.is_checked():
                    #Suffix
                    RenamedAssetName = AssetPathNameOnly + AssetName + inputbox_prefix.get_text()
                else:
                    #Prefix
                    RenamedAssetName = AssetPathNameOnly + inputbox_prefix.get_text() + AssetName
                
                                           
            #리네임 시키는 부분
            ue.rename_asset(AssetFullPath,RenamedAssetName)
        
        if replace_checkbox.is_checked():
            if inputbox_prefix.get_text() == '':
                ue.log('총 {0}개의 에셋에서 {1} 문자를 제거하였습니다.'.format(len(assets),inputbox_replace.get_text()))
            else:
                ue.log('총 {0}개의 에셋에서 {1}을 {2}로 교체하였습니다.'.format(len(assets),inputbox_replace.get_text(), inputbox_prefix.get_text()))
        else:
            if suffix_checkbox.is_checked():
                ue.log('총 {0}개의 에셋에서 이름뒤에 {1}를 추가하였습니다.'.format(len(assets), inputbox_prefix.get_text()))
            else:
                ue.log('총 {0}개의 에셋에서 이름앞에 {1}를 추가하였습니다.'.format(len(assets), inputbox_prefix.get_text()))
        #window.request_destroy()
            
    return True

def GetAssetClicked():
    # 선택한 에셋들 가져오기
    assets = ue.get_selected_assets()
    selected = len(assets)
    button.set_content(STextBlock().set_text(str(selected) + '개 선택완료'))
    ue.log('에셋 선택 완료')
    return True


# 추가할 입력 받는 곳
inputbox_prefix = SEditableTextBox().set_text('').set_tooltip_text('추가할 문자를 적는 곳입니다. \n삭제 활성화에 체크되어 있고, 여기를 공백으로 남겨두면 원하는 글자를 삭제해줍니다.')

# 변경할 문자 적는 곳
inputbox_replace = SEditableTextBox().set_text('').set_tooltip_text('변경하거나 지우고 싶은 문자열이 없을때는 그냥 공백으로 두면 됩니다.')

#창 사이즈
window = SWindow(screen_position=(100,100),is_topmost_window=True).resize(280, 250).set_title('naOng2 ReNamer').set_sizing_rule(1)
horizontal = SHorizontalBox()

#버튼 추가
button = SButton(h_align=2, v_align=2).set_content(STextBlock().set_text('변경할 에셋 선택하기')).set_tooltip_text('Content Browser에서 이름을 변경하고 싶은 에셋을 고른후에 누르세요')
button.bind_on_clicked(GetAssetClicked)

button2 = SButton(h_align=2, v_align=2).set_content(STextBlock().set_text('Apply')).set_tooltip_text('아무생각없이 누르면 엉뚱한 녀석이 리네임 됩니다. 정신 똑바로 차리고 누르세요')
button2.bind_on_clicked(OKclicked)



# 체크
replace_checkbox = SCheckBox().set_tooltip_text('대체하고 싶은 문자열이 있거나, 특정 문자열을 지우고 싶을 때 체크합니다. ')
suffix_checkbox = SCheckBox().set_tooltip_text('비활성화시 이름 앞에 추가할 문자열이 추가됩니다. 문자열을 뒤쪽으로 붙이고 싶을때 체크하세요')

# Grid에 쳐 넣기
grid = SGridPanel()

#grid.add_slot(STextBlock(text='이름을 변경할 에셋들을 \n먼저 선택해 주세요\n'), 0, 0)
#grid.add_slot(button, 1, 0)

#grid.add_slot(STextBlock(text='-------------------------------------'), 0, 1)
#grid.add_slot(STextBlock(text='-------------------------------------'), 1, 1)

grid.add_slot(STextBlock(text='Suffix 활성화\n'), 0, 2)
grid.add_slot(suffix_checkbox, 1, 2)
grid.add_slot(STextBlock(text='추가할 문자열\n'), 0, 3)
grid.add_slot(inputbox_prefix, 1, 3)

grid.add_slot(STextBlock(text='-------------------------------------'), 0, 4)
grid.add_slot(STextBlock(text='-------------------------------------'), 1, 4)

grid.add_slot(STextBlock(text='문자열 대체/삭제 활성화\n'), 0, 5)
grid.add_slot(replace_checkbox, 1,5)

grid.add_slot(STextBlock(text='기존 문자열 \n'), 0, 6)
grid.add_slot(inputbox_replace, 1, 6)

grid.add_slot(STextBlock(text='-------------------------------------'), 0, 7)
grid.add_slot(STextBlock(text='-------------------------------------\n'), 1, 7)

grid.add_slot(STextBlock(text='리네임 실행\n'), 0, 8)
grid.add_slot(button2, 1, 8)


# Horizontal에 쳐 넣기
horizontal.add_slot(grid, v_align=2, h_align=2)

#창 띄우기
window.set_content(horizontal)