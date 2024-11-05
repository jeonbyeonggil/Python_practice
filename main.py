from speech_recognition_module import recognize_speech
from text_to_speech_module import speak_text

if __name__ == "__main__":
    text = recognize_speech()
    if text:
        speak_text(text)
