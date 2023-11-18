from pedalboard import Pedalboard, Chorus, Reverb, Delay, load_plugin
from pedalboard.io import AudioFile
import wave
import matplotlib.pyplot as plt
import numpy as np


effect = load_plugin("/Library/Audio/Plug-Ins/Components/Tent.component")

# Wrapping a sample C++ plugin and processing the sine wave through there


# print(effect.parameters.keys())

# dict_keys(['par0', 'par1', 'par2', 'par3', 'par4', 'par5', 'par6', 'par7', 'par8', 'par9', 'toggle0', 'toggle1', 'toggle8', 'toggle9', 'par10', 'par11',
#          'par12', 'par13', 'par14', 'par15', 'par16', 'calinput', 'sidebutton0', 'sidebutton1', 'sidebutton2', 'fft_window', 'fft_size', 'scalefactor'])

effect.par0 = 0.96
effect.par1 = -0.96
effect.par2 = 0.503
effect.par3 = 0.477
effect.par4 = 0.51
effect.par5 = 1.00
effect.par6 = 0.10
effect.par7 = 0.14
effect.par8 = 0.00
effect.par9 = 0.00
effect.par10 = 0.00
effect.par11 = 500
effect.par12 = 0.0
effect.par13 = 5.00
effect.par14 = 5.00
effect.par15 = 5.00

# file = "sine.wav"

# effected = effect(file)

def overWrite():

	with AudioFile('test_message.wav') as f:

		# Open an audio file to write to:
		with AudioFile('Test_Two.wav', 'w', f.samplerate, f.num_channels) as o:

			# Read one second of audio at a time, until the file is empty:
			while f.tell() < f.frames:
				chunk = f.read(f.samplerate)

				# Run the audio through our pedalboard:
				effected = effect(chunk, f.samplerate, reset=False)

				o.write(effected)


######### Plotting The Wave #########

# encoding - pcm_s16le
# format - s16
# number of channels - 2 (stereo)
# sample_rate - 16000
# file_size - 704104 bytes
# duration - 11s


def new():
	obj = wave.open("Test_Two.WAV", "rb")


	print("Number of channels", obj.getnchannels())  # 2
	print("sample width", obj.getsampwidth())  # 2
	print("frame rate", obj.getframerate())  # 16000
	print("Number of frames", obj.getnframes())  # 176000


	print("parameters", obj.getparams())
	# comptype = NONE, comname= "not compressed"

	frames = obj.readframes(-1)  # reads all frames
	print(type(frames), type(frames[0]))
	print(len(frames) / 2)  # 352000.0 frames

	obj_new = wave.open("testing_change.wav", "wb")

	obj_new.setnchannels(2)
	obj_new.setsampwidth(2)
	obj_new.setframerate(16000.0)
	obj_new.writeframes(frames)

	obj_new.close()

####### Soundfile has been converted ###


def main():
    overWrite()
    new()



if __name__ == "__main__":
    main()
