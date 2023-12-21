from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")

audio = audio + 4   #+4 dB

audio = audio * 2    #repeat twice

audio = audio.fade_in(2000)

audio.export("change.mp3", format="mp3")

audio4 = AudioSegment.from_mp3("change.mp3")

print("done")
