import wave


# - number of channels
# - sample width
# - framerate/sample_rate...usually 44,100
# - number of frames
# - values of a frame...this will be initially in a binary format

obj = wave.open("Rainbow.WAV", "rb")

print("Number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)   #reads all frames
print(type(frames), type(frames[0]))
print(len(frames))
