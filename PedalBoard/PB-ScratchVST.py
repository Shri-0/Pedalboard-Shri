from pedalboard import Pedalboard, Chorus, Reverb, Delay, load_plugin
from pedalboard.io import AudioFile


effect = load_plugin("/Library/Audio/Plug-Ins/Components/Tent.component")

# Wrapping a sample C++ plugin and processing the sine wave through there


print(effect.parameters.keys())

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

with AudioFile('sineStereo.wav') as f:

    # Open an audio file to write to:
    with AudioFile('sineAmend.wav', 'w', f.samplerate, f.num_channels) as o:

        # Read one second of audio at a time, until the file is empty:
        while f.tell() < f.frames:
            chunk = f.read(f.samplerate)

            # Run the audio through our pedalboard:
            effected = effect(chunk, f.samplerate, reset=False)

            o.write(effected)
