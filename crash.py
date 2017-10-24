from microbit import *
count = 0
while True:
    value = pin0.read_analog() < 10:
        count += 1
        display.show(str(count))
        
    