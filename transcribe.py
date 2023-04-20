import azure.cognitiveservices.speech as speechsdk
import cognitive


def from_mic():
    speech_config = speechsdk.SpeechConfig(
        subscription=cognitive.subscription, region=cognitive.region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("plz command")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    return result.text
