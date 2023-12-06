import math
import soundfile as sf
import numpy as np
#import librosa


data, samplerate = sf.read('sineAmend.wav')
channels = len(data.shape)
length_s = len(data)/float(samplerate)

if (length_s < 6.0):
    n = math.ceil(6*samplerate/len(data))
if (channels == 2):
    data = np.tile(data, (n,1))
else:
    data = np.tile(data,n)

sf.write('new.wav', data, samplerate)
