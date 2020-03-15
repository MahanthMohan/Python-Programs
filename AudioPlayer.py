import os
import simpleaudio as audio
from playsound import playsound
audio = input("Enter the name of the audio file: ")
format = input("Enter the audio format (mp3 or wav) : ")

if(format == "mp3"):
 playsound(audio + ".{}".format(format))
elif(format == "wav"):
 audio_request = audio.WaveObject.from_wave_file(audio + ".{}".format(format))
 play = audio_request.play()
