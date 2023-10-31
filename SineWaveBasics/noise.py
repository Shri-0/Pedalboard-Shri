
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt


# we create a noisy sine wave and clean up the noise

frequency = 1000
noisy_freq = 50
num_samples = 48000

# sampling rate

sampling_rate = 48000.0
nframes = num_samples
comptype = "NONE"
compname = "not compressed"
nchannels = 1
sampwidth = 2
amplitude = 16000


sine_wav = [np.sin(2 * np.pi * frequency * x1/sampling_rate)
            for x1 in range(num_samples)]

sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/sampling_rate)
              for x1 in range(num_samples)]


# convert into num.py arrays

sine_wave = np.array(sine_wav)
noise_wav = np.array(sine_noise)
file = "testing.wav"

# put them together

combined_signal = sine_wave + noise_wav


wav_file = wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(
    sampling_rate), nframes, comptype, compname))
# opening the file and setting the parameters

for s in combined_signal:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))


plt.subplot(3, 1, 1)
plt.title("Original Sine Wave")

plt.subplots_adjust(hspace=.5)
plt.plot(sine_wave[:500])
plt.subplot(3, 1, 2)
plt.title("Noisy Wave")
plt.plot(sine_noise[:4000])
plt.subplot(3, 1, 3)

plt.title("Original + Noise")
plt.plot(combined_signal[:3000])
plt.show()

data_fft = np.fft.fft(combined_signal)  # contains the noise and signal wave
freq = (np.abs(data_fft[:len(data_fft)]))

plt.plot(freq)

plt.title("Before filtering: Will have main signal (1000hz) + noise frequency (50hz)")

plt.xlim(0, 1200)
plt.show()


###### Continue from here later########
'''
filtered_freq = []
index = 0
for f in freq:
# We create an empty list called filter_freq. freq stores the abs value of the fft(frequencies present)



    # Filter between lower and upper limits
    # Choosing 950, since it is closest to 1000.
    if index > 950 and index < 1050:
		#index = current array element in the array freq. you are searching for frequencies stored in the fft between
		#those values so that you can pinpoint 1000


        if f > 1:
            filtered_freq.append(f)
            #while all frequencis will be present, their abs values will be miniscule, and less than 1. If we find a value > 1, we store it in the array
        else:
            filtered_freq.append(0)
    else:
        filtered_freq.append(0)
index += 1
'''

filtered_freq = [f if (950 < index < 1050 and f > 1)
                 else 0 for index, f in enumerate(freq)]

# if the freuency is too low, we dont attach it, and we go through the index range some more

plt.plot(filtered_freq)
plt.title("After Filtering: Main signal only (1000Hz)")
plt.xlim(0, 1200)
plt.show()
plt.close()


# recovered signal - takes our signal and converts it back to time domain

recovered_signal = np.fft.ifft(filtered_freq)


plt.subplot(3, 1, 1)
plt.title("Original Sine Wave")

# Need to add empty space, else everything will looked scrunched up.

plt.subplots_adjust(hspace=.5)
plt.plot(sine_wave[:500])
plt.subplot(3, 1, 2)
plt.title("Noisy Wave")

plt.plot(combined_signal[:4000])
plt.subplot(3, 1, 3)
plt.title("Sine Wave after clean up")
plt.plot((recovered_signal[:500]))
plt.show()
