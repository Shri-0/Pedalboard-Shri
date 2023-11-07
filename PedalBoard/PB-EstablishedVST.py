from pedalboard import Pedalboard, Chorus, Reverb, Delay, load_plugin
from pedalboard.io import AudioFile
from mido import Message


# load an instrument from the VSt Library
instrument = load_plugin( "/Library/Audio/Plug-Ins/Components/Addictive Keys.component")

# dict_keys(['modulation_x', 'ch1_level', 'ch2_level', 'ch3_level', 'ch1_sendfx1', 'ch1_sendfx2', 'ch2_sendfx1', 'ch2_sendfx2', 'ch3_sendfx1', 'ch3_sendfx2', 'fx1_level', 'fx2_level', 'master_level', 'master_filtlo', 'master_filthi'])



# Wrapping established 3rd party C++ plugins and processing audio files through here through there

#SketchCassette
SketchCassetteEffect = load_plugin("/Library/Audio/Plug-Ins/Components/SketchCassette II.component")
# dict_keys(['input_gain', 'output_gain', 'comp_dry_wet', 'dropout_intensity', 'flutter_rate', 'comp_amount', 'tape_quality', 'wow_rate', 'saturation_type', 'flutter_offset', 'wow_offset', 'age', 'flutter_rhythm', 'comp_brightness', 'wow_rhythm', 'dropout_depth', 'flutter_depth', 'flutter_shape', 'flanging', 'tape_hiss', 'nr_comp', 'tape_dry_wet', 'wow_depth', 'wow_shape', 'wow_flutter_mode', 'dropout_width', 'tape_type', 'tempo_sync', 'saturation'])

#Valhalla Frequency Echo
ValhallaFreqEchoeffect = load_plugin("/Library/Audio/Plug-Ins/Components/ValhallaFreqEcho.component")
# dict_keys(['wetdry', 'shift', 'delay', 'sync', 'feedback', 'lowcut', 'highcut', 'stereo'])









'''
print(SketchCassetteEffect.parameters.keys())
print(ValhallaFreqEchoeffect.parameters.keys())
print(instrument.parameters.keys())
'''
