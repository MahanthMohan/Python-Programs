import os
from playsound import playsound

class AudioPlayer:

    def getFileName(self,path):
        self.path = path
        trimmed_path = path.replace("C:","")
        file_name = os.path.basename(trimmed_path)
        return file_name


    def playaudio(self,file_name,repeat):
        self.file_name = file_name
        self.repeat = repeat
        initial = 0
        while(initial < repeat):
            playsound(path)
            initial += 1

AudioPlayer = AudioPlayer()

path = input("Name/Path of the audio file: ")
repeat = int(input("Number of times: "))
AudioPlayer.playaudio(AudioPlayer.getFileName(path), repeat)