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

MyMIDI.addNote(0,0, 66 ,  0  ,  0.5   ,100) #(F#)
MyMIDI.addNote(0,0, 69 ,  0.5,  0.5   ,100) #A
MyMIDI.addNote(0,0, 74 ,  1  ,  0.5   ,100) #D
MyMIDI.addNote(0,0, 78 ,  1.5,  0.5   ,100) #(F#)
MyMIDI.addNote(0,0, 78 ,  2  ,  0.5   ,100) #(F#)
MyMIDI.addNote(0,0, 78 ,  2.5,  1     ,100) #(F#)
MyMIDI.addNote(0,0, 69 ,  3.5,  0.5   ,100) #D



    
with open("underthesea.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
 
