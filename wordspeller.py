from gtts import gTTS
from playsound import playsound as ps
word = str(input("Enter a word to spell it out: "))
word_length = len(word)

command = str(input("Enter a command (spell or speak): "))

if command == "spell":
    for start_index in range(0,word_length):
        start_index = start_index
        print(word[start_index], end = " ")

elif command == "speak":
    tts = gTTS(word)
    tts.save('tts.mp3')
    ps("tts.mp3")

