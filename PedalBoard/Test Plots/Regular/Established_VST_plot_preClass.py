import matplotlib.pyplot as plt
import numpy as np
import wave
import struct

############# Regular MIDI .Wav SIGNAL ##############


# def sample_pure_rhodes():
obj = wave.open("PedalBoard/Test Files - .WAV/Established/Rhode_Note_V1.wav", "rb")

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

# print(signal_array)
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

# return n_samples, times, signal_array


####################  Processed MIDI .WAV SIGNAL   ##############################

# def sample_amend_rhodes():

obj_two = wave.open(
    "PedalBoard/Test Files - .WAV/Established/Rhode_SC_Note_Delay.wav", "rb")

sample_freq_two = obj_two.getframerate()
n_samples_two = obj_two.getnframes()
signal_wave_two = obj_two.readframes(-1)
obj_two.close()

t_audio_two = n_samples_two / sample_freq_two
signal_array_two = np.frombuffer(signal_wave_two, dtype=np.int16)  # y
times_two = np.linspace(0, t_audio_two, num=n_samples_two*2)  # x


infile = "PedalBoard/Test Files - .WAV/Established/Rhode_SC_Note_Delay.wav"
wav_file = wave.open(infile, 'r')
data = wav_file.readframes(n_samples_two)

t_audio_two = n_samples_two / sample_freq_two


data = struct.unpack('{n}h'.format(n=n_samples_two*2), data)
data = np.array(data)

# converting data to numpy array

data_fft = np.fft.fft(data)
# print(data_fft)

# we are going to get the frequencies we want
frequencies = np.abs(data_fft)

print("The frequency is {} Hz".format(np.argmax(frequencies)))


plt.subplot(2, 1, 1)
plt.plot(data[:500000])  # this will cut off the graph at hz
plt.title("Post SketchCassette Audio wave")
plt.subplot(2, 1, 2)
plt.plot(frequencies)
plt.title("Frequencies Found")
plt.xlim(0, 25000)
plt.show()


plt.figure(figsize=(15, 5))
plt.plot(times_two, signal_array_two)
plt.title("Post SketchCassette signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time(s)")
plt.xlim(0, t_audio_two)
plt.show()

# return signal_array_two, times_two, t_audio_two, n_samples_two

####################  Combined MIDI .WAV SIGNAL   ##############################


# def combine_signals(signal_array, signal_array_two, times, times_two, t_audio_two, n_samples):


# ------------------------------- Work In progress ------------------------------- #

combined_signal_array = signal_array + signal_array_two
combined_times = times + times_two


plt.figure(figsize=(15, 5))
plt.plot(combined_times, combined_signal_array)
plt.title("Combined signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time(s)")
plt.xlim(0, t_audio_two)
plt.show()


data = struct.unpack('{n}h'.format(n=n_samples*2), combined_signal_array)
data = np.array(data)

# converting data to numpy array

data_fft = np.fft.fft(data)
# print(data_fft)

# we are going to get the frequencies we want
frequencies = np.abs(data_fft)
print("The frequency is {} Hz".format(np.argmax(frequencies)))

plt.subplot(2, 1, 1)
plt.plot(data[:500000])  # this will cut off the graph at hz
plt.title("Combined Rhode and Delay wave")
plt.subplot(2, 1, 2)
plt.plot(frequencies)
plt.title("Frequencies Found")
plt.xlim(0, 25000)
plt.show()


####################  Filtered Delay  - Process  ##############################


####### Addition #########


# def addition():
'''
obj = wave.open("PedalBoard/Test Files - .WAV/Established/Rhode_SC.wav", "rb")
frames = obj.readframes(-1)

obj_two = wave.open("PedalBoard/Test Files - .WAV/Established/Rhode.wav", "rb")
frames_two = obj_two.readframes(-1)

obj_new = wave.open("Combination.WAV", "wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100.0)
obj_new.writeframes(frames + frames_two)

obj_new.close()

'''
#############################


# def main():
# sample_pure_rhodes()
# sample_amend_rhodes()

# signal_array = sample_pure_rhodes()
# signal_array_two = sample_amend_rhodes()
# times = sample_pure_rhodes()
# times_two = sample_amend_rhodes()
# t_audio_two = sample_amend_rhodes()
# n_samples = sample_pure_rhodes()

# combine_signals(signal_array, signal_array_two, times, times_two, t_audio_two, n_samples)
# addition()


# if __name__ == "__main__":
#   main()
