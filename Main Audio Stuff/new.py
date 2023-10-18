import matplotlib.pyplot as plt
import numpy as np
import wave

obj = wave.open("shri_new.wav", "rb")

sample_freq = obj.getnframes()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_freq

print(t_audio)
