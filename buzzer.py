from microbit import *
display.show(Image.CONFUSED)
while True :
    if button_a.is_pressed() and not button_b.is_pressed():
        display.show(Image.HAPPY)
        sleep(1000)
    elif button_b.is_pressed() and not button_a.is_pressed(): 
        display.show(Image.SAD)
        sleep(1000)
    elif button_b.is_pressed and button_a.is_pressed() :
        display.show(Image.CONFUSED)
        sleep(1000)