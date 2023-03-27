# Imports go at the top
from microbit import *
from MicroRover import*


robot = Micro_Rover()

while True:
    
    if button_a.was_pressed():
        robot.motor(255,255)
    elif button_b.was_pressed():
        robot.motor(-255,-255)
        
   
