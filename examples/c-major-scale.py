#!/usr/bin/env python

from midiutil import MIDIFile

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)

"""
for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    time = time + 1
"""

MyMIDI.addNote(0,0,60,0,1,100)
MyMIDI.addNote(0,0,62,2,0.5,100)
MyMIDI.addNote(0,0,64,2.5,0.5,100)
MyMIDI.addNote(0,0,65,3,0.5,100)

MyMIDI.addTempo(track,time, 200)
MyMIDI.addNote(0,0,67,4,1,100)
MyMIDI.addNote(0,0,69,5,1,100)
MyMIDI.addNote(0,0,71,6,1,100)
MyMIDI.addNote(0,0,72,7,1,100)



with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
