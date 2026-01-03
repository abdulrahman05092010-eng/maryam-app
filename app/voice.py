from plyer import tts

def speak(text):
    try:
        tts.speak(text)
    except:
        pass
