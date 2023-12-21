from pedalboard import Pedalboard, Chorus, Compressor, Delay, Gain, Reverb, Phaser, load_plugin, Convolution
from pedalboard.io import AudioStream
#import wave
#import pyaudio


input_device_name = AudioStream.input_device_names[1]
output_device_name = AudioStream.output_device_names[1]


#def liveAudio():
with AudioStream(
		input_device_name, output_device_name

	) as stream:
		stream.plugins = Pedalboard([
			Chorus(),
			Phaser(),
			Reverb(room_size=0.25),
		]
                              )
input("Press enter to stop streaming...")


print(input_device_name)
print(output_device_name)







'''
def main():
    liveAudio()


if __name__ == "__main__":
    main()


'''













'''
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 2
# CHANNELS = 1

RATE = 16000
'''


'''
	frames = []

    ##### insert loop ####



    ##### insert loop ####


	obj = wave.open("demoV1.wav", "wb")
	obj.setnchannels(CHANNELS)
	obj.setsampwidth(stream.get_sample_size(FORMAT))
	obj.setframerate(RATE)
	obj.writeframes(b"".join(frames))
	obj.close()


'''



'''
SketchCassetteEffect = load_plugin(
    "/Library/Audio/Plug-Ins/Components/SketchCassette II.component")

print(SketchCassetteEffect.flutter_rate)
print(SketchCassetteEffect.tape_quality)
print(SketchCassetteEffect.age)
print(SketchCassetteEffect.output_gain)

SketchCassetteEffect.flutter_rate = 5.0
SketchCassetteEffect.tape_quality = "Standard"
SketchCassetteEffect.age = 0.8
SketchCassetteEffect.output_gain = 0.4

# 5.0
# Standard
# 0.0
# 0.0
'''

'''
Was able to run synth into Audio interface and out through monitors when hitting enter

Still want to see if an external plugin can be run through this in the future
'''
