from pedalboard import Pedalboard, Chorus, Reverb, Delay
from pedalboard.io import AudioFile


#test


def test():
	# Make a Pedalboard object, containing multiple audio plugins:
	board = Pedalboard([Chorus(), Reverb(room_size=0.50),
					Delay(delay_seconds=0.08, mix=0.5)])

	# Open an audio file for reading, just like a regular file:
	with AudioFile('shri_new.wav') as f:

	# Open an audio file to write to:
		with AudioFile('outputFour.wav', 'w', f.samplerate, f.num_channels) as o:

			# Read one second of audio at a time, until the file is empty:
			while f.tell() < f.frames:
				chunk = f.read(f.samplerate)

				# Run the audio through our pedalboard:
				effected = board(chunk, f.samplerate, reset=False)

				# Write the output to our output file:
				o.write(effected)


def main():
    test()




if __name__ == "__main__":
    main()
