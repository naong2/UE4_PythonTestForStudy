# UE4 Python 플러그인 버전
* UE4 4.21 버전 
* UnrealEnginePython #539 - 2019년 01월 10일자 버전
* https://github.com/20tab/UnrealEnginePython

# 저의 파이선 환경
* Python 3.6
* PyQt5 5.11.3
* PySide2 5.12.0
* autopep8-1.4.3
* numpy-1.13.3
* pandas-0.20.3
* SpeechRecognition-3.8.1

# 에디터 실행 전 DefaultEngine.ini 수정사항
* Config/DefaultEngine.ini 을 자신의 환경에 맞게 수정해야함
* Home = 자신의 파이선 환경 패스
* ScriptsPath = ue_site.py 파일이 있는 스크립트 루트
* AdditionalModulesPath = 추가하고 싶은 모듈 경로

```sh
[Python]
Home=G:/Anaconda3
ScriptsPath=G:/UE4_PythonTest/Python
AdditionalModulesPath=G:/UE4_PythonTest/Python/MyModule
```

# 스크립트 소개 (Project_Root/Python/)
* Python/ue_site.py : 버튼 메뉴 추가 샘플
* Python/kaiju_fbximport.py : 자동화 튜토리얼의 일부
* Python/Renamer_Replace.py : 에셋 리네임툴
* Python/Sample_PyQt.py : PyQt5 샘플윈도우창
* Python/PythonScript2.py : 추가모듈패스 설정후 불러오기 테스트
* Python/Naong2/Sample_PySide.py : PySide 샘플
