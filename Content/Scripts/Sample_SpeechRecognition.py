import unreal_engine as ue
import speech_recognition as sr
from unreal_engine.classes import TextRenderComponent


class SpeechRecognition():

    def begin_play(self):
        self.uobject.bind_key('K', ue.IE_PRESSED, self.VoiceRecognition_K)

    def VoiceRecognition_K(self):
        ue.log('Start Recognition!!!!')
        MyBox = self.uobject.get_component_by_type(TextRenderComponent)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Speak : ')
            MyBox.SetText('Speak anithing~')
            self.uobject.call('ChangeDialogue')
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language="ko-KR")
                print('You said : {}'.format(text)) 
                MyBox.SetText(text)
                # Call CustomEvent in BP
                self.uobject.call('ChangeDialogue')
            except:
                print('Sorry could not recognize!!!')






