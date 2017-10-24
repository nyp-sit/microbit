from microbit import *
while True:
    value = pin0.read_analog()
    if value < 10:
        display.show('A')
    elif value < 60:            
        display.show('B')
    elif value < 110:
        display.show('C')
    elif value < 150:
        display.show('D')
    elif value < 550:
        display.show('E')