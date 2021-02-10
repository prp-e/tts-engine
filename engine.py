import wave 
import pyaudio 
from pydub import AudioSegment 

sound1 = AudioSegment.from_file("sounds/k.wav", format="wav")
sound2 = AudioSegment.from_file("sounds/aw.wav", format="wav")

overlay = sound1.append(sound2, crossfade=0)
file_handle = overlay.export("temp.wav", format="wav")


CHUNK = 1024 # size of data you want to read

wf = wave.open('temp.wav', 'rb') # audio sample 

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.close()
p.terminate()
