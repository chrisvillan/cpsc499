#!/usr/bin/env python

from midiutil import MIDIFile

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 150   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)

a=[]
"""
for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    time = time + 1
"""

MyMIDI.addNote(0,0, 66 ,  0  ,  0.5   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 69 ,  0.5,  0.5   ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 74 ,  1  ,  0.5   ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 78 ,  1.5,  0.5   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 78 ,  2  ,  0.5   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 78 ,  2.5,  1     ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 69 ,  3.5,  0.5   ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 76 ,  4  ,  1     ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 79 ,  5  ,  1     ,100) #G
a.append("G")
MyMIDI.addNote(0,0, 78 ,  6  ,  1     ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 74 ,  7  ,  1     ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 62 ,  8  ,  0.5   ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 66 ,  8.5,  0.5   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 69 ,  9  ,  0.5   ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 74 ,  9.5,  0.5   ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  10 ,  0.5   ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  10.5, 1     ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 64 ,  11.5, 0.5   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 73 ,  12  , 1     ,100) #(C#)
a.append("C#")
MyMIDI.addNote(0,0, 76 ,  13  , 1     ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 74 ,  14  , 2     ,100) #D
a.append("D")

#Next Line
#Quarter Rest | Time + 1
MyMIDI.addNote(0,0, 74 ,  17  ,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  17.5,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  18  ,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  18.5,  1    ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  19.5,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 73 ,  20  ,  1    ,100) #(C#)
a.append("C#")
MyMIDI.addNote(0,0, 76 ,  21  ,  1    ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 74 ,  22  ,  1    ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 69 ,  23  ,  1    ,100) #A
a.append("A")
#Quarter Rest | Time + 1
MyMIDI.addNote(0,0, 66 ,  25  ,  0.5  ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 69 ,  25.5,  0.5  ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 69 ,  26  ,  0.5  ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 69 ,  26.5,  1    ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 66 ,  27.5,  0.5  ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 64 ,  28  ,  1    ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 69 ,  29  ,  1    ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 66 ,  30  ,  1    ,100) #(F#)
a.append("F#")


#Next Line
#Quarter Rest | Time + 1
MyMIDI.addNote(0,0, 74 ,  32  ,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  32.5,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  33  ,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  33.5,  1    ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  34.5,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 73 ,  35  ,  1    ,100) #(C#)
a.append("C#")
MyMIDI.addNote(0,0, 76 ,  36  ,  1    ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 74 ,  37  ,  1    ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 69 ,  38  ,  1    ,100) #A
a.append("A")
#Quarter Rest | Time + 1
MyMIDI.addNote(0,0, 66 ,  40  ,  0.5  ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 69 ,  40.5,  0.5  ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 69 ,  41  ,  0.5  ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 69 ,  41.5,  1    ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 66 ,  42.5,  0.5  ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 64 ,  43  ,  1    ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 69 ,  44  ,  1    ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 66 ,  45  ,  1    ,100) #(F#)
a.append("F#")

#Next Line
#Quarter Rest | Time + 1
MyMIDI.addNote(0,0, 71 ,  47  ,  0.5  ,100) #B
a.append("B")
MyMIDI.addNote(0,0, 74 ,  47.5,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  48  ,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  48.5,  1    ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 71 ,  49.5,  0.5  ,100) #B
a.append("B")
MyMIDI.addNote(0,0, 69 ,  50  ,  1    ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 74 ,  51  ,  1    ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 69 ,  52  ,  1    ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 74 ,  53  ,  1    ,100) #D
a.append("D")
#Quarter Rest | Time + 1
MyMIDI.addNote(0,0, 73 ,  55  ,  0.5  ,100) #(C#)
a.append("C#")
MyMIDI.addNote(0,0, 76 ,  55.5,  0.5  ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 76 ,  56  ,  0.5  ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 76 ,  56.5,  1    ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 74 ,  57.5,  0.5  ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 78 ,  58  ,  1    ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 76 ,  59  ,  1    ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 74 ,  60  ,  1    ,100) #D
a.append("D")

key = "C major"
sharp = 0
Fsharp = False
Csharp = False
firstC = False


#note count
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0 

for i in range(len(a)):

    if a[i] == "A":
        A += 1
    elif a[i] == "B":
        B += 1
    elif a[i] == "C":
        C += 1
    elif a[i] == "D":
        D += 1
    elif a[i] == "E":
        E += 1
    elif a[i] == "F":
        F += 1
    elif a[i] == "G":
        G += 1





     
    if a[i] == "F#" and Fsharp == False:
        Fsharp = True
        key = "G Major or E Minor"
        print("Hit F#!")
        print(key)
    #E Minor (E,G,B, - cannot change) (G Major - G,B,D, they cannot change)

    #Case for E Minor
    if a[i] == "D#" and Fsharp == True and key !="E Minor":
        key = "E Minor"
        print("Hit D#!")
        print(key)

    
    #Case for G Major
    if a[i] == "E#" and Fsharp == True:
        key = "G Major"
        print("Hit D#!")
        print(key)

 
    if a[i] == "C" and Csharp == False:
        firstC = True
        print("Hit")
    if a[i] == "C#" and Csharp == False and firstC == False:
        Csharp = True
        print("Hit C#!")
        if Fsharp == True:
            key = "D Major or B Minor"
            print(key)

    if key == "D Major or B Minor" and i == 20:
        if D > B:
            key = "D Major"
        elif B > D:
            key = "B Minor"
        else:
            print("Don't know")
            
        print(key)

            


with open("underthesea.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
 
