# Pedalboard-Shri
1.  Main Audio Stuff : Record.py - Can record your own voice
2.  SineWaveBasics : main.py - can generate sine wave in mono or stereo
3.  PedalBoard : Contains Python files with various test secanrios using Pedalboard.


----------------

Current Objectives:
A.  Results so far: Can successsfully plot sinewaves through matplotlib, and can process basic voice recordings and create basic notes from MIDI Generation.
	- Able to load multiple plugins into one file. Need to see if multiple effects from plugins can be put into one generated sound...so far I can use Valhalla Echo and SketchCassette and implement both (still more effects need to be added for notable difference.)
B.  3rd Party Established VSTs need extensive testing (not sure if possible with Live Audio at the moment)
C.  Live Audiostream feature needs to be coded and tested - Update: Can route audio out from synth into interface, and can adjust audio as necessary in pedalboard when start button is pressed

D. Will need to graphically analyze and plot sounds generated from PedalBoard session folder (update: Implemented from PB-ScratchVST.py into Tent_plot.py) -> Need to work on combining wet and dry signals into one sound, and implement more filter seperation techniques (involves creating functions with return variables)


---------------

Errors that need resolving:

1. Files with extreme delay processing shows frequency range as 189,000+ HZ, further inquiry required (PB-ScratchVST.py into Tent_plot.py)

Raw Voice File and combined are 11000 Hz...which makes more sense

2. Raw MIDI generation freq range is 2000HZ which is accurate (PB-EstablishedVST.py)...same inquiry is needed with delay processed files
