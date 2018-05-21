#pip install MIDIUtil
#pip install pygame 

from midiutil import MIDIFile
import pygame

#MIDI Pygame documation - https://pypi.org/project/MIDIUtil/
degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)
MyMIDI2 = MIDIFile(1)  # One track
MyMIDI2.addTempo(track, time, 160)
MyMIDI3 = MIDIFile(1)  # One track
MyMIDI3.addTempo(track, time, 120)

a=[]
b=[]
c=[]

#CHOOSE SONG
#1 = Greensleeves
#2 = Under The Sea
#3 = Happy Birthday
songChoice = 3

"""
for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    time = time + 1
"""
#-----------Greensleeves---------------------

MyMIDI.addNote(0,0, 64 ,  0  ,  1   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 67 ,  1  ,  2   ,100) #G
a.append("G")
MyMIDI.addNote(0,0, 69 ,  3  ,  1   ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 71 ,  4  ,  1.5 ,100) #B
a.append("B")
MyMIDI.addNote(0,0, 72 ,  5.5,  0.5 ,100) #C
a.append("C")
MyMIDI.addNote(0,0, 71 ,  6  ,  1   ,100) #B
a.append("B")
MyMIDI.addNote(0,0, 69 ,  7  ,  2   ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 66 ,  9  ,  1   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 62 ,  10 ,  1.5 ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 64 ,  11.5, 0.5 ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 66 ,  12 ,  1.0 ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 67 ,  13 ,  2   ,100) #G
a.append("G")
MyMIDI.addNote(0,0, 64 ,  15 ,  1   ,100) #E
a.append("E")

#Next Line
MyMIDI.addNote(0,0, 64 ,  16 ,  1.5 ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 63 ,  17.5, 0.5 ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 64 ,  18  , 1   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 66 ,  19 ,  2   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 63 ,  21 ,  1   ,100) #(D#)
a.append("D#")
MyMIDI.addNote(0,0, 59 ,  22 ,  2   ,100) #B
a.append("B")
MyMIDI.addNote(0,0, 64 ,  24 ,  1   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 67 ,  25 ,  2   ,100) #G
a.append("G")
MyMIDI.addNote(0,0, 69 ,  27 ,  1   ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 71 ,  28 ,  1.5 ,100) #B
a.append("B")
MyMIDI.addNote(0,0, 72 ,  29.5, 0.5 ,100) #C
a.append("C")
MyMIDI.addNote(0,0, 71 ,  30 ,  1   ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 69 ,  31 ,  2   ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 66 ,  33 ,  1   ,100) #(F#)
a.append("F")

#Next Line
MyMIDI.addNote(0,0, 62 ,  34 ,  1.5 ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 64 ,  35.5, 0.5 ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 66 ,  36 ,  1   ,100) #F
a.append("F")
MyMIDI.addNote(0,0, 67 ,  37 ,  1.5 ,100) #G
a.append("G")
MyMIDI.addNote(0,0, 66 ,  38.5, 0.5 ,100) #F
a.append("F")
MyMIDI.addNote(0,0, 64 ,  39 ,  1   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 63 ,  40 ,  1.5 ,100) #(D#)
a.append("D#")
MyMIDI.addNote(0,0, 61 ,  41.5, 0.5 ,100) #(C#)
a.append("C#")
MyMIDI.addNote(0,0, 63 ,  42 ,  1   ,100) #(D#)
a.append("D#")
MyMIDI.addNote(0,0, 64 ,  43 ,  2   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 64 ,  45 ,  1   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 64 ,  46 ,  2.5 ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 74 ,  48.5, 3   ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  51.5, 1.5 ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 73 ,  53 ,  0.5 ,100) #(C#)
a.append("C#")
MyMIDI.addNote(0,0, 71 ,  53.5, 1   ,100) #B
a.append("B")

#Next Line
MyMIDI.addNote(0,0, 69 ,  54.5, 2   ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 66 ,  56.5, 1   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 62 ,  57.5, 1.5 ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 64 ,  59  , 0.5 ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 66 ,  59.5, 1   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 67 ,  60.5, 2   ,100) #(G)
a.append("G")
MyMIDI.addNote(0,0, 64 ,  62.5, 1   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 64 ,  63.5, 1.5 ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 63 ,  65  , 0.5 ,100) #(D#)
a.append("D#")
MyMIDI.addNote(0,0, 64 ,  65.5, 1   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 66 ,  66.5, 2   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 63 ,  68.5, 1   ,100) #(D#)
a.append("D#")
MyMIDI.addNote(0,0, 59 ,  69.5, 3   ,100) #(B)
a.append("B")

#Next Line
MyMIDI.addNote(0,0, 74 ,  72.5, 3   ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 74 ,  75.5, 1.5 ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 73 ,  77  , 0.5 ,100) #(C#)
a.append("C#")
MyMIDI.addNote(0,0, 71 ,  77.5, 1   ,100) #B
a.append("B")
MyMIDI.addNote(0,0, 69 ,  78.5, 2   ,100) #A
a.append("A")
MyMIDI.addNote(0,0, 66 ,  80.5, 1   ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 62 ,  81.5, 1.5 ,100) #D
a.append("D")
MyMIDI.addNote(0,0, 64 ,  83  , 0.5 ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 66 ,  83.5, 1   ,100) #(F#)
a.append("F#")

#Next Line
MyMIDI.addNote(0,0, 67 ,  84.5, 1.5 ,100) #G
a.append("G")
MyMIDI.addNote(0,0, 66 ,  86  , 0.5 ,100) #(F#)
a.append("F#")
MyMIDI.addNote(0,0, 64 ,  86.5, 1   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 63 ,  87.5, 1.5 ,100) #(D#)
a.append("D#")
MyMIDI.addNote(0,0, 61 ,  89  , 0.5 ,100) #(C#)
a.append("C#")
MyMIDI.addNote(0,0, 63 ,  89.5, 1   ,100) #(D#)
a.append("D#")
MyMIDI.addNote(0,0, 64 ,  90.5, 3   ,100) #E
a.append("E")
MyMIDI.addNote(0,0, 64 ,  93.5, 2   ,100) #E
a.append("E")
#--------------- End-------------------------------

#-----------------Under the Sea---------------------

MyMIDI2.addNote(0,0, 66 ,  0  ,  0.5   ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 69 ,  0.5,  0.5   ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 74 ,  1  ,  0.5   ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 78 ,  1.5,  0.5   ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 78 ,  2  ,  0.5   ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 78 ,  2.5,  1     ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 69 ,  3.5,  0.5   ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 76 ,  4  ,  1     ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 79 ,  5  ,  1     ,100) #G
b.append("G")
MyMIDI2.addNote(0,0, 78 ,  6  ,  1     ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 74 ,  7  ,  1     ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 62 ,  8  ,  0.5   ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 66 ,  8.5,  0.5   ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 69 ,  9  ,  0.5   ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 74 ,  9.5,  0.5   ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  10 ,  0.5   ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  10.5, 1     ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 64 ,  11.5, 0.5   ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 73 ,  12  , 1     ,100) #(C#)
b.append("C#")
MyMIDI2.addNote(0,0, 76 ,  13  , 1     ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 74 ,  14  , 2     ,100) #D
b.append("D")

#Next Line
#Quarter Rest | Time + 1
MyMIDI2.addNote(0,0, 74 ,  17  ,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  17.5,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  18  ,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  18.5,  1    ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  19.5,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 73 ,  20  ,  1    ,100) #(C#)
b.append("C#")
MyMIDI2.addNote(0,0, 76 ,  21  ,  1    ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 74 ,  22  ,  1    ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 69 ,  23  ,  1    ,100) #A
b.append("A")
#Quarter Rest | Time + 1
MyMIDI2.addNote(0,0, 66 ,  25  ,  0.5  ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 69 ,  25.5,  0.5  ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 69 ,  26  ,  0.5  ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 69 ,  26.5,  1    ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 66 ,  27.5,  0.5  ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 64 ,  28  ,  1    ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 69 ,  29  ,  1    ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 66 ,  30  ,  1    ,100) #(F#)
b.append("F#")


#Next Line
#Quarter Rest | Time + 1
MyMIDI2.addNote(0,0, 74 ,  32  ,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  32.5,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  33  ,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  33.5,  1    ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  34.5,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 73 ,  35  ,  1    ,100) #(C#)
b.append("C#")
MyMIDI2.addNote(0,0, 76 ,  36  ,  1    ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 74 ,  37  ,  1    ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 69 ,  38  ,  1    ,100) #A
b.append("A")
#Quarter Rest | Time + 1
MyMIDI2.addNote(0,0, 66 ,  40  ,  0.5  ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 69 ,  40.5,  0.5  ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 69 ,  41  ,  0.5  ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 69 ,  41.5,  1    ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 66 ,  42.5,  0.5  ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 64 ,  43  ,  1    ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 69 ,  44  ,  1    ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 66 ,  45  ,  1    ,100) #(F#)
b.append("F#")

#Next Line
#Quarter Rest | Time + 1
MyMIDI2.addNote(0,0, 71 ,  47  ,  0.5  ,100) #B
b.append("B")
MyMIDI2.addNote(0,0, 74 ,  47.5,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  48  ,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 74 ,  48.5,  1    ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 71 ,  49.5,  0.5  ,100) #B
b.append("B")
MyMIDI2.addNote(0,0, 69 ,  50  ,  1    ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 74 ,  51  ,  1    ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 69 ,  52  ,  1    ,100) #A
b.append("A")
MyMIDI2.addNote(0,0, 74 ,  53  ,  1    ,100) #D
b.append("D")
#Quarter Rest | Time + 1
MyMIDI2.addNote(0,0, 73 ,  55  ,  0.5  ,100) #(C#)
b.append("C#")
MyMIDI2.addNote(0,0, 76 ,  55.5,  0.5  ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 76 ,  56  ,  0.5  ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 76 ,  56.5,  1    ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 74 ,  57.5,  0.5  ,100) #D
b.append("D")
MyMIDI2.addNote(0,0, 78 ,  58  ,  1    ,100) #(F#)
b.append("F#")
MyMIDI2.addNote(0,0, 76 ,  59  ,  1    ,100) #E
b.append("E")
MyMIDI2.addNote(0,0, 74 ,  60  ,  1    ,100) #D
b.append("D")

#-------------------End-----------------------

#------------------Happy Birthday-------------
MyMIDI3.addNote(0,0, 62 ,  0  ,  0.5  ,100) #D
c.append("D")
MyMIDI3.addNote(0,0, 62 ,  0.5,  0.5  ,100) #D
c.append("D")
MyMIDI3.addNote(0,0, 64 ,  1  ,  1    ,100) #E
c.append("E")
MyMIDI3.addNote(0,0, 62 ,  2  ,  1    ,100) #D
c.append("D")
MyMIDI3.addNote(0,0, 67 ,  3  ,  1    ,100) #G
c.append("G")
MyMIDI3.addNote(0,0, 66 ,  4  ,  2    ,100) #(F#)
c.append("F#")
MyMIDI3.addNote(0,0, 62 ,  6  ,  0.5  ,100) #D
c.append("D")
MyMIDI3.addNote(0,0, 62 ,  6.5,  0.5  ,100) #D
c.append("D")
MyMIDI3.addNote(0,0, 64 ,  7  ,  1    ,100) #E
c.append("E")
MyMIDI3.addNote(0,0, 62 ,  8  ,  1    ,100) #D
c.append("D")
MyMIDI3.addNote(0,0, 69 ,  9  ,  1    ,100) #A
c.append("A")
MyMIDI3.addNote(0,0, 67 ,  10  ,  2   ,100) #G
c.append("G")
MyMIDI3.addNote(0,0, 62 ,  12  ,  0.5 ,100) #D
c.append("D")
MyMIDI3.addNote(0,0, 62 ,  12.5,  0.5 ,100) #D
c.append("D")
MyMIDI3.addNote(0,0, 74 ,  13  ,  1   ,100) #D
c.append("D")
MyMIDI3.addNote(0,0, 71 ,  14  ,  1   ,100) #B
c.append("B")
MyMIDI3.addNote(0,0, 67 ,  15  ,  1   ,100) #G
c.append("G")
MyMIDI3.addNote(0,0, 66 ,  16  ,  1   ,100) #(F#)
c.append("F#")
MyMIDI3.addNote(0,0, 64 ,  17  ,  1   ,100) #E
c.append("E")
MyMIDI3.addNote(0,0, 72 ,  18  ,  0.5 ,100) #C
c.append("C")
MyMIDI3.addNote(0,0, 72 ,  18.5,  0.5 ,100) #C
c.append("C")
MyMIDI3.addNote(0,0, 71 ,  19  ,  1   ,100) #B
c.append("B")
MyMIDI3.addNote(0,0, 67 ,  20  ,  1   ,100) #G
c.append("G")
MyMIDI3.addNote(0,0, 69 ,  21  ,  1   ,100) #A
c.append("A")
MyMIDI3.addNote(0,0, 67 ,  22  ,  2   ,100) #G
c.append("G")

#-------------------End------------------------


key = "C major"
sharp = 0
Fsharp = False
Csharp = False
firstC = False



if songChoice == 1:#Greensleeves
    song = a
elif songChoice == 2:#UnderTheSea
    song = b
elif songChoice == 3:#HappyBirthday
    song = c

noteCheck = 20 
#note count
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0 

for i in range(len(song)):

    if song[i] == "A":
        A += 1
    elif song[i] == "B":
        B += 1
    elif song[i] == "C":
        C += 1
    elif song[i] == "D":
        D += 1
    elif song[i] == "E":
        E += 1
    elif song[i] == "F":
        F += 1
    elif song[i] == "G":
        G += 1
     
    if song[i] == "F#" and Fsharp == False:
        Fsharp = True
        key = "G Major or E Minor"
        print("Hit F#!")
        sharp += 1
        print(key)
    #E Minor (E,G,B, - cannot change) (G Major - G,B,D, they cannot change)


    #Case for G Major
    if key == "G Major or E Minor" and i == noteCheck:
        if G > E:
            key = "G Major"
        elif E > G:
            key = "E Minor"
        else:
            noteCheck += 4
        print(key)

        
    #Case for E Minor
    if song[i] == "D#" and Fsharp == True and key !="E Minor" and sharp == 1:
        key = "E Minor"
        print("Hit D#!")
        print(key)

    
    if song[i] == "C" and Csharp == False:
        firstC = True
        
    if song[i] == "C#" and Csharp == False and firstC == False:
        Csharp = True
        print("Hit C#!")
        sharp += 1
        if Fsharp == True:
            key = "D Major or B Minor"
            print(key)

    if key == "D Major or B Minor" and i == noteCheck:
        if D > B:
            key = "D Major"
        elif B > D:
            key = "B Minor"
        else:
            print("Don't know")
        print(key)

if key == "C Major":
    print("Happy (:")
elif key == "G Major":
    print("Happy (:")
elif key == "D Major":
    print("Happy (:")
elif key == "A Minor":
    print("Sad ):")
elif key == "E Minor":
    print("Sad ):")
elif key == "B Minor":
    print("Sad ):")
else:
    print("I don't know")

    
with open("greensleeves.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

with open("underthesea.mid", "wb") as output_file:
    MyMIDI2.writeFile(output_file)

with open("happybirthday.mid", "wb") as output_file:
    MyMIDI3.writeFile(output_file)

#following code from https://gist.github.com/naotokui/29073690279056e9354e6259efbf8f30
#used to play midi type files on pygame
#only alteration is the midi_file
def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print "Music file %s loaded!" % music_file
    except pygame.error:
        print "File %s not found! (%s)" % (music_file, pygame.get_error())
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
# pick a midi music file you have ...
# (if not in working folder use full path)


if songChoice == 1:
    midi_file = 'greensleeves.mid'
elif songChoice == 2:
    midi_file = 'underthesea.mid'
elif songChoice == 3:
    midi_file = 'happybirthday.mid'

freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024    # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)
try:
    play_music(midi_file)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit

