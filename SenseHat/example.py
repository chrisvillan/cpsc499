from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

r = (255,0,0)
g = (0, 255, 0)
b = (0, 0, 255)

O = (0, 0, 0)

matrix = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, r, r, r, r, O, O,
    O, O, r, r, r, r, O, O,
    O, O, r, r, r, r, O, O,
    O, O, r, r, r, r, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

matrix2 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, b, b, O, O, O,
    O, O, b, b, b, b, O, O,
    O, O, b, b, b, b, O, O,
    O, O, O, b, b, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

for i in range (10):
    sense.set_pixels(matrix)
    sleep(0.2)
    sense.set_pixels(matrix2)
    sleep(0.2)
