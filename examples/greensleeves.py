#!/usr/bin/env python

from midiutil import MIDIFile

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)

"""
for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    time = time + 1
"""

MyMIDI.addNote(0,0, 64 ,  0  ,  1   ,100) #E
MyMIDI.addNote(0,0, 67 ,  1  ,  2   ,100) #G
MyMIDI.addNote(0,0, 69 ,  3  ,  1   ,100) #A
MyMIDI.addNote(0,0, 71 ,  4  ,  1.5 ,100) #B
MyMIDI.addNote(0,0, 72 ,  5.5,  0.5 ,100) #C
MyMIDI.addNote(0,0, 71 ,  6  ,  1   ,100) #B
MyMIDI.addNote(0,0, 69 ,  7  ,  2   ,100) #A
MyMIDI.addNote(0,0, 66 ,  9  ,  1   ,100) #(F#)
MyMIDI.addNote(0,0, 62 ,  10 ,  1.5 ,100) #D
MyMIDI.addNote(0,0, 64 ,  11.5, 0.5 ,100) #E
MyMIDI.addNote(0,0, 66 ,  12 ,  1.0 ,100) #(F#)
MyMIDI.addNote(0,0, 67 ,  13 ,  2   ,100) #G
MyMIDI.addNote(0,0, 64 ,  15 ,  1   ,100) #E

MyMIDI.addNote(0,0, 64 ,  16 ,  1.5 ,100) #E
MyMIDI.addNote(0,0, 63 ,  17.5, 0.5 ,100) #D
MyMIDI.addNote(0,0, 64 ,  18  , 1   ,100) #E
MyMIDI.addNote(0,0, 66 ,  19 ,  2   ,100) #(F#)
MyMIDI.addNote(0,0, 63 ,  21 ,  1   ,100) #(D#)
MyMIDI.addNote(0,0, 59 ,  22 ,  2   ,100) #B
MyMIDI.addNote(0,0, 64 ,  24 ,  1   ,100) #E
MyMIDI.addNote(0,0, 67 ,  25 ,  2   ,100) #G
MyMIDI.addNote(0,0, 69 ,  27 ,  1   ,100) #A
MyMIDI.addNote(0,0, 71 ,  28 ,  1.5 ,100) #B
MyMIDI.addNote(0,0, 72 ,  29.5, 0.5 ,100) #C
MyMIDI.addNote(0,0, 71 ,  30 ,  1   ,100) #D
MyMIDI.addNote(0,0, 69 ,  31 ,  2   ,100) #A
MyMIDI.addNote(0,0, 66 ,  33 ,  1   ,100) #(F#)

MyMIDI.addNote(0,0, 62 ,  34 ,  1.5 ,100) #D
MyMIDI.addNote(0,0, 64 ,  35.5, 0.5 ,100) #E
MyMIDI.addNote(0,0, 66 ,  36 ,  1   ,100) #F
MyMIDI.addNote(0,0, 67 ,  37 ,  1.5 ,100) #G
MyMIDI.addNote(0,0, 66 ,  38.5, 0.5 ,100) #F
MyMIDI.addNote(0,0, 64 ,  39 ,  1   ,100) #E
MyMIDI.addNote(0,0, 63 ,  40 ,  1.5 ,100) #(D#)
MyMIDI.addNote(0,0, 61 ,  41.5, 0.5 ,100) #(C#)
MyMIDI.addNote(0,0, 63 ,  42 ,  1   ,100) #(D#)
MyMIDI.addNote(0,0, 64 ,  43 ,  2   ,100) #E
MyMIDI.addNote(0,0, 64 ,  45 ,  1   ,100) #E
MyMIDI.addNote(0,0, 64 ,  46 ,  2.5 ,100) #E
MyMIDI.addNote(0,0, 74 ,  48.5, 3   ,100) #D
MyMIDI.addNote(0,0, 74 ,  51.5, 1.5 ,100) #D
MyMIDI.addNote(0,0, 73 ,  53 ,  0.5 ,100) #(C#)
MyMIDI.addNote(0,0, 71 ,  53.5, 1   ,100) #B  

MyMIDI.addNote(0,0, 69 ,  54.5, 2   ,100) #A
MyMIDI.addNote(0,0, 66 ,  56.5, 1   ,100) #(F#)
MyMIDI.addNote(0,0, 62 ,  57.5, 1.5 ,100) #D
MyMIDI.addNote(0,0, 64 ,  59  , 0.5 ,100) #E
MyMIDI.addNote(0,0, 66 ,  59.5, 1   ,100) #(F#)
MyMIDI.addNote(0,0, 67 ,  60.5, 2   ,100) #(G)
MyMIDI.addNote(0,0, 64 ,  62.5, 1   ,100) #E
MyMIDI.addNote(0,0, 64 ,  63.5, 1.5 ,100) #E
MyMIDI.addNote(0,0, 63 ,  65  , 0.5 ,100) #(D#)
MyMIDI.addNote(0,0, 64 ,  65.5, 1   ,100) #E
MyMIDI.addNote(0,0, 66 ,  66.5, 2   ,100) #(F#)
MyMIDI.addNote(0,0, 63 ,  68.5, 1   ,100) #(D#)
MyMIDI.addNote(0,0, 59 ,  69.5, 3   ,100) #(B)

MyMIDI.addNote(0,0, 74 ,  72.5, 3   ,100) #D
MyMIDI.addNote(0,0, 74 ,  75.5, 1.5 ,100) #D
MyMIDI.addNote(0,0, 73 ,  77  , 0.5 ,100) #(C#)
MyMIDI.addNote(0,0, 71 ,  77.5, 1   ,100) #B
MyMIDI.addNote(0,0, 69 ,  78.5, 2   ,100) #A
MyMIDI.addNote(0,0, 66 ,  80.5, 1   ,100) #(F#)
MyMIDI.addNote(0,0, 62 ,  81.5, 1.5 ,100) #D
MyMIDI.addNote(0,0, 64 ,  83  , 0.5 ,100) #E
MyMIDI.addNote(0,0, 66 ,  83.5, 1   ,100) #(F#)

MyMIDI.addNote(0,0, 67 ,  84.5, 1.5 ,100) #G
MyMIDI.addNote(0,0, 66 ,  86  , 0.5 ,100) #(F#)
MyMIDI.addNote(0,0, 64 ,  86.5, 1   ,100) #E
MyMIDI.addNote(0,0, 63 ,  87.5, 1.5 ,100) #(D#)
MyMIDI.addNote(0,0, 61 ,  89  , 0.5 ,100) #(C#)
MyMIDI.addNote(0,0, 63 ,  89.5, 1   ,100) #(D#)
MyMIDI.addNote(0,0, 64 ,  90.5, 3   ,100) #E
MyMIDI.addNote(0,0, 64 ,  93.5, 2   ,100) #E

with open("greensleeves.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
 
