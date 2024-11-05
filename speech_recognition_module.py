# import speech_recognition as sr

# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("편하게 말씀해주시면 됩니다...")
#         audio = recognizer.listen(source)

#         try:
#             text = recognizer.recognize_google(audio, language='ko-KR')
#             print("음성 인식 결과:", text)
#             return text  # 인식 결과 반환
#         except sr.UnknownValueError:
#             print("다시 한번 말씀해주세요.")
#         except sr.RequestError:
#             print("Google 음성 인식 서비스에서 문제가 발생했습니다.")
#         return None  # 오류 발생 시 None 반환


import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    # 음성 인식 코드 주석 처리
    # with sr.Microphone() as source:
    #     print("편하게 말씀해주시면 됩니다...")
    #     audio = recognizer.listen(source)

    # 테스트용으로 하드코딩된 문자열 반환 (음성 인식 없이)
    text = "하드코딩된 음성 인식 결과입니다."
    print("음성 인식 결과:", text)
    return text  # 인식 결과 반환

    # 원래 코드는 아래와 같이 유지
    # try:
    #     text = recognizer.recognize_google(audio, language='ko-KR')
    #     print("음성 인식 결과:", text)
    #     return text  # 인식 결과 반환
    # except sr.UnknownValueError:
    #     print("다시 한번 말씀해주세요.")
    # except sr.RequestError:
    #     print("Google 음성 인식 서비스에서 문제가 발생했습니다.")
    # return None  # 오류 발생 시 None 반환
