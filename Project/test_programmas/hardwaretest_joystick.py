from gpiozero import Button
from time import sleep

joystick_left = Button(22)
joystick_right = Button(23)
joystick_up = Button(27)
joystick_down = Button(17)

while True:
    if joystick_left.is_pressed:
        print('left' )
    if joystick_right.is_pressed:
        print('right')
    if joystick_up.is_pressed:
        print('up')
    if joystick_down.is_pressed:
        print('down')
    sleep(1)