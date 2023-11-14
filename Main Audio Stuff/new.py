import matplotlib.pyplot as plt
import numpy as np
import wave
import struct


# obj = wave.open("shri_new.wav", "rb")

############## WET VOICE SIGNAL ##############

obj = wave.open("testing_change.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()
t_audio = n_samples / sample_freq

# print(t_audio)


signal_array = np.frombuffer(signal_wave, dtype=np.int16)  # y
times = np.linspace(0, t_audio, num=n_samples*2)  # x
# times = np.linspace(0, t_audio, num=n_samples)  # x             - For Mono Files

# print(signal_array)
# print(times)

# x = np.array(times)
# y = np.array(signal_array)


###########

data = struct.unpack('{n}h'.format(n=n_samples*2), signal_wave)
data = np.array(data)

# converting data to numpy array

data_fft = np.fft.fft(data)
# print(data_fft)

# we are going to get the frequencies we want
frequencies = np.abs(data_fft)

# data_fft[1] will contain frequency parts of 1Hz
# data_fft[2] will contain frequency part of 2Hz
print("The frequency is {} Hz".format(np.argmax(frequencies)))

plt.subplot(2, 1, 1)
plt.plot(data[:600])  # this will cut off the graph at hz
plt.title("Original audio wave")
plt.subplot(2, 1, 2)
plt.plot(frequencies)
plt.title("Frequencies Found")
plt.xlim(0, 1200)
plt.show()


plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time(s)")
plt.xlim(0, t_audio)
plt.show()


####################  DRY VOICE SIGNAL   ##############################
'''
obj_two = wave.open("test_message.wav", "rb")

sample_freq_two = obj_two.getframerate()
n_samples_two = obj_two.getnframes()
signal_wave_two = obj_two.readframes(-1)

obj_two.close()

t_audio_two = n_samples_two / sample_freq_two

signal_array_two = np.frombuffer(signal_wave_two, dtype=np.int16)  # y

times_two = np.linspace(0, t_audio_two, num=n_samples_two*2)  # x


plt.figure(figsize=(15, 5))
plt.plot(times_two, signal_array_two)
plt.title("Audio signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time(s)")
plt.xlim(0, t_audio_two)
plt.show()

####################  Combined   ##############################

combined_signal_array = signal_array + signal_array_two
combined_times = times + times_two

plt.figure(figsize=(15, 5))
plt.plot(combined_times, combined_signal_array)
plt.title("Audio signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time(s)")
plt.xlim(0, t_audio_two)
plt.show()




####################  Established Vst PRE   ##############################


####################  Established Vst POST   ##############################
'''
