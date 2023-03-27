# Imports go at the top
from microbit import *
from MicroRover import*


robot = Micro_Rover()

while True:
    
    if button_a.is_pressed():
        robot.motor(255,255)
    else:
        button_b.is_pressed()
        robot.motor(-255,-255)
        
   
