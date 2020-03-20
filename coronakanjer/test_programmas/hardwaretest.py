from gpiozero import Button
from time import sleep

button = Button(4)

while true:
    if button.is_pressed:
        print(' pressed' )
    sleep(1)