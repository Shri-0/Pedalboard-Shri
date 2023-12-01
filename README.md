# Pedalboard-Shri
1.  Main Audio Stuff : Record.py - Can record your own voice
2.  SineWaveBasics : main.py - can generate sine wave in mono or stereo
3.  PedalBoard : Contains Python files with various test secanrios using Pedalboard.


----------------

Current Objectives:
A.  Results so far: Can successsfully plot sinewaves through matplotlib, and can process basic voice recordings and create basic notes from MIDI Generation.
	- Able to load multiple plugins into one file. Need to see if multiple effects from plugins can be put into one generated sound...so far I can use Valhalla Echo and SketchCassette and implement both (still more effects need to be added for notable difference.)
B.  3rd Party Established VSTs need extensive testing - Implementation into Live audio needs to be looked into
C.  Can route audio out from synth into interface, and can adjust audio as necessary in pedalboard when start button is pressed

D. Will need to graphically analyze and plot sounds generated from PedalBoard session folder. Includes taking Signal arrays and combining them, filtering out frequencies between multiple generated audio files (higher level functionality needed).


---------------

Errors that need resolving:

1. Files with processing (test and established plugins) with freq. range in the 100k+ Hz category needed inverse fourier transform method to resolve it to a reasonable frequency range......Raw Voice File and combined are 11000 Hz...which makes more sense

However...Delay processed samples still show massive frequency range even with ifft established...

2. Raw MIDI generation freq range is 2000HZ which is accurate (PB-EstablishedVST.py)
