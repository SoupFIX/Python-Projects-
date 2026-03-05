import sounddevice as sd
from scipy.io.wavfile import write
#setting frequenc
freq = 48000
#setting record duration
duration = 15 #15seconds
#initializing the recorder with the given inputs
recording = sd.rec(int(duration*freq),samplerate=freq,channels=2)
print("The recording started.................")
#wait until the recording is completed
sd.wait()   
print("The recording finished and successfully saved!")
#convert the file from raw data as numbers into audible data
write("recordin2.wav",freq,recording)
