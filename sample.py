from playsound import playsound
from gtts import gTTS

mytext = input("入力：　")

tts = gTTS(text=mytext, lang = 'ja', slow = False)
tts.save('data.mp3')


playsound("data.mp3")
