from gtts import gTTS
from playsound import playsound as ps

class wordspeller:

    def spellword(self, word):
        self.word = word
        self.command = command
        word_length = len(word)

        start_index = start_index
        tts = gTTS(word)
        tts.save('audio.mp3')
        ps("audio.mp3")

