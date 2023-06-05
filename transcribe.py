import azure.cognitiveservices.speech as speechsdk
# import cognitive
import os


def from_mic():
    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ.get('subscription'), region=os.environ.get('region'))
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("plz command")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    return result.text
