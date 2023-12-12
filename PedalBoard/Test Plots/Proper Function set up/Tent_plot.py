import matplotlib.pyplot as plt
import numpy as np
import wave
import struct


# obj = wave.open("shri_new.wav", "rb")

############## WET VOICE SIGNAL ##############

def postProcess():

	obj = wave.open("PedalBoard/Test Files - .WAV/Tent/Spare/testing_change.wav", "rb")

	sample_freq = obj.getframerate()
	n_samples = obj.getnframes()
	signal_wave = obj.readframes(-1)
	# signal_wave_freq = obj.readframes(n_samples)

	obj.close()

	infile = "PedalBoard/Test Files - .WAV/Tent/Spare/testing_change.wav"
	wav_file = wave.open(infile, 'r')
	data = wav_file.readframes(n_samples)

	t_audio = n_samples / sample_freq

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
	print("The main frequency is {} Hz".format(np.argmax(frequencies)))

	plt.subplot(2, 1, 1)
	plt.plot(data[:500000])  # this will cut off the graph at hz
	plt.title("Post Tent Audio Wave")
	plt.subplot(2, 1, 2)
	plt.plot(frequencies)
	plt.title("Frequencies Found")
	plt.xlim(0, 25000)
	plt.show()


	plt.figure(figsize=(15, 5))
	plt.plot(times, signal_array)
	plt.title("Post Tent signal")
	plt.ylabel("Signal Wave")
	plt.xlabel("Time(s)")
	plt.xlim(0, t_audio)
	plt.show()

	class postSignals:
			def returnTheSecondDataElements():
				return n_samples, times, t_audio




####################  DRY VOICE SIGNAL   ##############################

def preProcess():

	obj_two = wave.open("PedalBoard/Test Files - .WAV/Tent/Spare/test_message.wav", "rb")

	sample_freq_two = obj_two.getframerate()
	n_samples_two = obj_two.getnframes()
	signal_wave_two = obj_two.readframes(-1)
	obj_two.close()

	t_audio_two = n_samples_two / sample_freq_two
	signal_array_two = np.frombuffer(signal_wave_two, dtype=np.int16)  # y
	times_two = np.linspace(0, t_audio_two, num=n_samples_two*2)  # x


	infile = "PedalBoard/Test Files - .WAV/Tent/Spare/test_message.wav"
	wav_file = wave.open(infile, 'r')
	data = wav_file.readframes(n_samples_two)

	t_audio = n_samples_two / sample_freq_two


	data = struct.unpack('{n}h'.format(n=n_samples_two*2), data)
	data = np.array(data)

	# converting data to numpy array

	data_fft = np.fft.fft(data)
	# print(data_fft)

	# we are going to get the frequencies we want
	frequencies = np.abs(data_fft)

	print("The main frequency is {} Hz".format(np.argmax(frequencies)))

	plt.subplot(2, 1, 1)
	plt.plot(data[:500000])  # this will cut off the graph at hz
	plt.title("Pre Tent Audio wave")
	plt.subplot(2, 1, 2)
	plt.plot(frequencies)
	plt.title("Frequencies Found")
	plt.xlim(0, 25000)
	plt.show()


	plt.figure(figsize=(15, 5))
	plt.plot(times_two, signal_array_two)
	plt.title("Pre Tent signal")
	plt.ylabel("Signal Wave")
	plt.xlabel("Time(s)")
	plt.xlim(0, t_audio_two)
	plt.show()


	class preSignals:
		def returnTheFirstDataElements():
			return signal_array_two, times_two, t_audio_two




####################  Return Example   ##############################

'''
class num:
	def returnTheseValues(x, y):
		return x + y

number = num()
'''
####################  Combined   ###############################

'''
def combined():
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
	print("The main frequency is {} Hz".format(np.argmax(frequencies)))

	plt.subplot(2, 1, 1)
	plt.plot(data[:500000])  # this will cut off the graph at hz
	plt.title("Combined Tent wave")
	plt.subplot(2, 1, 2)
	plt.plot(frequencies)
	plt.title("Frequencies Found")
	plt.xlim(0, 25000)
	plt.show()

'''
####### Combination ##########


def main():

	#print(num.returnTheseValues(3,7))

    postProcess()
    preProcess()
    #combined()

    # combine(signal_array, times, n_samples, signal_array_two, t_audio_two,times_two)
    # combine()


if __name__ == "__main__":
    main()
