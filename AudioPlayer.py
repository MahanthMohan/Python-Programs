import os
from playsound import playsound

def getFileName(path):
    trimmed_path = path.replace("C:","")
    file_name = os.path.basename(trimmed_path)
    return file_name


def playaudio(file_name,repeat):
    initial = 0
    while(initial < repeat):
        playsound(path)
        initial += 1

path = input("Name/Path of the audio file: ")
repeat = int(input("Number of times: "))
playaudio(getFileName(path), repeat)