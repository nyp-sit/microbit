from microbit import *
import music
while True:
    if pin1.read_analog() < 5:
        music.pitch(175, 4)
    elif pin1.read_analog() < 60:
        music.pitch(196, 4)
    elif pin1.read_analog(( < 110:
        music.pitch(220, 4)
    elif pin1.read_analog() < 150:
        music.pitch(247, 4)
    elif pin1.read_analog() < 600:
        music.pitch(262, 4)
        
        