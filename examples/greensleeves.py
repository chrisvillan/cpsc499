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



with open("greensleeves.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
 
