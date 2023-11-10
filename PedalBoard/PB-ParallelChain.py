from pedalboard import Pedalboard, Compressor, Delay, Distortion, Gain, PitchShift, Reverb, Mix, load_plugin


initial_gain = Gain(gain_db=0)


# SketchCassette
SketchCassetteEffect = load_plugin(
    "/Library/Audio/Plug-Ins/Components/SketchCassette II.component")
# dict_keys(['input_gain', 'output_gain', 'comp_dry_wet', 'dropout_intensity', 'flutter_rate', 'comp_amount', 'tape_quality', 'wow_rate', 'saturation_type', 'flutter_offset', 'wow_offset', 'age', 'flutter_rhythm', 'comp_brightness', 'wow_rhythm', 'dropout_depth', 'flutter_depth', 'flutter_shape', 'flanging', 'tape_hiss', 'nr_comp', 'tape_dry_wet', 'wow_depth', 'wow_shape', 'wow_flutter_mode', 'dropout_width', 'tape_type', 'tempo_sync', 'saturation'])

compress = Pedalboard([Compressor(threshold_db=-50, ratio=25, attack_ms=1, release_ms=100)])



