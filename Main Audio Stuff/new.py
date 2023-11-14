import matplotlib.pyplot as plt
import numpy as np
import wave

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
#times = np.linspace(0, t_audio, num=n_samples)  # x             - For Mono Files

print(signal_array)
print(times)

x = np.array(times)
y = np.array(signal_array)


plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time(s)")
plt.xlim(0, t_audio)
plt.show()



####################  DRY VOICE SIGNAL   ##############################

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
