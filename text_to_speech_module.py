import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) #음성 출력 속도 조절 라인
    engine.say(text)
    engine.runAndWait()