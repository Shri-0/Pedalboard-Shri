from pedalboard import Pedalboard, Chorus, Reverb, Delay, load_plugin
from pedalboard.io import AudioFile
from mido import Message
import wave

# I am going to see if I can replicate the same results in an actual logic session using the same parameters here


# load an instrument from the VSt Library
instrument = load_plugin(
    "/Library/Audio/Plug-Ins/Components/Addictive Keys.component")

#instrument.show_editor()

# dict_keys(['modulation_x', 'ch1_level', 'ch2_level', 'ch3_level', 'ch1_sendfx1', 'ch1_sendfx2', 'ch2_sendfx1', 'ch2_sendfx2', 'ch3_sendfx1', 'ch3_sendfx2', 'fx1_level', 'fx2_level', 'master_level', 'master_filtlo', 'master_filthi'])


# Wrapping established 3rd party C++ plugins and processing audio files through here through there

# SketchCassette
SketchCassetteEffect = load_plugin(
    "/Library/Audio/Plug-Ins/Components/SketchCassette II.component")
# dict_keys(['input_gain', 'output_gain', 'comp_dry_wet', 'dropout_intensity', 'flutter_rate', 'comp_amount', 'tape_quality', 'wow_rate', 'saturation_type', 'flutter_offset', 'wow_offset', 'age', 'flutter_rhythm', 'comp_brightness', 'wow_rhythm', 'dropout_depth', 'flutter_depth', 'flutter_shape', 'flanging', 'tape_hiss', 'nr_comp', 'tape_dry_wet', 'wow_depth', 'wow_shape', 'wow_flutter_mode', 'dropout_width', 'tape_type', 'tempo_sync', 'saturation'])

SketchCassetteEffect.flutter_rate = 6.7

#SketchCassetteEffect.show_editor()
print(SketchCassetteEffect.flutter_rate)
#print(SketchCassetteEffect.tape_quality)
#print(SketchCassetteEffect.age)
#print(SketchCassetteEffect.output_gain)


# Valhalla Frequency Echo
ValhallaFreqEchoeffect = load_plugin(
    "/Library/Audio/Plug-Ins/Components/ValhallaFreqEcho.component")
# dict_keys(['wetdry', 'shift', 'delay', 'sync', 'feedback', 'lowcut', 'highcut', 'stereo'])

''''
ValhallaFreqEchoeffect.show_editor()
print(ValhallaFreqEchoeffect.wetdry)
print(ValhallaFreqEchoeffect.delay)
print(ValhallaFreqEchoeffect.sync)
print(ValhallaFreqEchoeffect.stereo)
'''



########################## Generation ###########################

sample_rate = 44100
audio = instrument(
    [Message("note_on", note=60), Message("note_off", note=60, time=5)],
    duration=5,  # seconds
    sample_rate=sample_rate,
)

print(audio)

#print("Number of channels", audio.getnchannels())  # 2
#print("sample width", audio.getsampwidth())  # 2
#print("frame rate", audio.getframerate())  # 16000
#print("Number of frames", audio.getnframes())  # 176000


#with AudioFile('Rhode_Effect.wav') as f:

#frames = audio.readframes(-1)  # reads all frames
#print(frames)

    # Open an audio file to write to:

with AudioFile('Rhode_Effect.wav', 'w', sample_rate, num_channels=2) as o:

        # Read one second of audio at a time, until the file is empty:
    while o.tell() < o.frames:
        chunk = o.read(o.samplerate)


            # Run the audio through our pedalboard:
effected = SketchCassetteEffect(audio, sample_rate)

#o.write(effected)

print(effected)







#print(SketchCassetteEffect.parameters.keys())
#print(ValhallaFreqEchoeffect.parameters.keys())
#print(instrument.parameters.keys())
