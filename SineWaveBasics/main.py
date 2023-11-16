
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt


# frequency - number of times a sine wave repeats in a second. We will use 1k
frequency = 1000

# sampling rate - let's take 48
num_samples = 48000

# sine wave formula : y(t) = A * sin(2 * pi * f * t)

# y(t) is the axis we want to sample to calculate x axis sample t
# A is amplitude
# pi is pi
# f is frequency
# t is our sample

# sampling rate
sampling_rate = 48000.0
amplitude = 16000
file = "Sines.wav"


# function
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate)
             for x in range(num_samples)]

# [] = final answer will be converted into a list
# range() function generates a list of numbers from 0 to num_samples....looping over a variable from 0 to 48000

nframes = num_samples
comptype = "NONE"
compname = "not compressed"
# nchannels=1
nchannels = 2

sampwidth = 2

wav_file = wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(
    sampling_rate), nframes, comptype, compname))
# opening the file and setting the parameters

for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
