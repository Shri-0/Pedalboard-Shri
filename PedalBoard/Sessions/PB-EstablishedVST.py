from pedalboard import Pedalboard, Chorus, Reverb, Delay, load_plugin
from pedalboard.io import AudioFile
from mido import Message
import wave
import numpy as np


# I am going to see if I can replicate the same results in an actual logic session using the same parameters here


# load an instrument from the VSt Library
instrument = load_plugin(
    "/Library/Audio/Plug-Ins/Components/Addictive Keys.component")

# instrument.show_editor()

# dict_keys(['modulation_x', 'ch1_level', 'ch2_level', 'ch3_level', 'ch1_sendfx1', 'ch1_sendfx2', 'ch2_sendfx1', 'ch2_sendfx2', 'ch3_sendfx1', 'ch3_sendfx2', 'fx1_level', 'fx2_level', 'master_level', 'master_filtlo', 'master_filthi'])


# Wrapping established 3rd party C++ plugins and processing audio files through here through there

# SketchCassette
SketchCassetteEffect = load_plugin(
    "/Library/Audio/Plug-Ins/Components/SketchCassette II.component")
# dict_keys(['input_gain', 'output_gain', 'comp_dry_wet', 'dropout_intensity', 'flutter_rate', 'comp_amount', 'tape_quality', 'wow_rate', 'saturation_type', 'flutter_offset', 'wow_offset', 'age', 'flutter_rhythm', 'comp_brightness', 'wow_rhythm', 'dropout_depth', 'flutter_depth', 'flutter_shape', 'flanging', 'tape_hiss', 'nr_comp', 'tape_dry_wet', 'wow_depth', 'wow_shape', 'wow_flutter_mode', 'dropout_width', 'tape_type', 'tempo_sync', 'saturation'])

SketchCassetteEffect.flutter_rate = 11.9
SketchCassetteEffect.age = 0.9
SketchCassetteEffect.output_gain = -2.0
SketchCassetteEffect.tape_quality = 'Cheap'
SketchCassetteEffect.flutter_rhythm = '1/16 trip.'

# SketchCassetteEffect.show_editor()
print(SketchCassetteEffect.flutter_rate)
print(SketchCassetteEffect.tape_quality)
print(SketchCassetteEffect.age)
print(SketchCassetteEffect.output_gain)


# Valhalla Frequency Echo
ValhallaFreqEchoeffect = load_plugin(
    "/Library/Audio/Plug-Ins/Components/ValhallaFreqEcho.component")
# dict_keys(['wetdry', 'shift', 'delay', 'sync', 'feedback', 'lowcut', 'highcut', 'stereo'])


#ValhallaFreqEchoeffect.show_editor()
print(ValhallaFreqEchoeffect.wetdry)
print(ValhallaFreqEchoeffect.delay)
print(ValhallaFreqEchoeffect.sync)
print(ValhallaFreqEchoeffect.stereo)


ValhallaFreqEchoeffect.delay = 0.5



########################## Generation ###########################
'''
sample_rate = 44100
num_channels = 2
with AudioFile("Rhode.wav", "w", sample_rate, num_channels) as f:
    f.write(instrument(
        [Message("note_on", note=60), Message("note_off", note=60, time=4)],
        sample_rate=sample_rate,
        duration=8,
        num_channels=num_channels
    ))
'''


with AudioFile('Rhode.wav') as f:

    # Open an audio file to write to:
    with AudioFile('Rhode_SC.wav', 'w', f.samplerate, f.num_channels) as o:

        # Read one second of audio at a time, until the file is empty:
        while f.tell() < f.frames:
            chunk = f.read(f.samplerate)

            # Run the audio through our pedalboard:
            effected = SketchCassetteEffect(chunk, f.samplerate, reset=False)
            effected_V = SketchCassetteEffect(chunk, f.samplerate, reset=False)

            o.write(effected + effected_V)


# print(SketchCassetteEffect.parameters.keys())
# print(ValhallaFreqEchoeffect.parameters.keys())
# print(instrument.parameters.keys())
