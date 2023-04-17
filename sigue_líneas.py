# Imports go at the top
from microbit import *
from Micro_Rover import*

robot = Micro_Rover()

while True:
    sensor = robot.infrared_sensor_value()
    display.show(str(sensor))
    if sensor == 2:
        robot.motor(255,255)
    else:
        sensor == 4
        robot.motor(255,0)
