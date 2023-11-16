import matplotlib.pyplot as plt
import numpy as np
import wave
import struct

############## Regular MIDI .Wav SIGNAL ##############

obj = wave.open("PedalBoard/Test Files - .WAV/Established/Rhode.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)
# signal_wave_freq = obj.readframes(n_samples)

obj.close()

infile = "PedalBoard/Test Files - .WAV/Established/Rhode.wav"
wav_file = wave.open(infile, 'r')
data = wav_file.readframes(n_samples)

t_audio = n_samples / sample_freq

print(sample_freq)
print(n_samples)


# print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)  # y
times = np.linspace(0, t_audio, num=n_samples*2)  # x

# times = np.linspace(0, t_audio, num=n_samples)  # x             - For Mono Files

###########

data = struct.unpack('{n}h'.format(n=n_samples*2), data)
data = np.array(data)

# converting data to numpy array

data_fft = np.fft.fft(data)
# print(data_fft)

# we are going to get the frequencies we want
frequencies = np.abs(data_fft)

# time = np.argmax(frequencies)
# freeze = (n_samples / 2)
# print(freeze/time)


# data_fft[1] will contain frequency parts of 1Hz
# data_fft[2] will contain frequency part of 2Hz
print("The frequency is {} Hz".format(np.argmax(frequencies)))

plt.subplot(2, 1, 1)
plt.plot(data[:500000])  # this will cut off the graph at hz
plt.title("Pure Tone Audio Wave")
plt.subplot(2, 1, 2)
plt.plot(frequencies)
plt.title("Frequencies Found")
plt.xlim(0, 25000)
plt.show()


plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Pure Tone signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time(s)")
plt.xlim(0, t_audio)
plt.show()

