from microbit import *

while True :
    gesture = accelerometer.current_gesture()
    if gesture == 'face up' :
        display.show(Image.HAPPY)
    elif gesture == 'face down' :
        display.show(Image.SAD)
    elif gesture == 'shake' : 
        display.show(Image.CONFUSED)
    else : 
        display.show(Image.ANGRY)
    