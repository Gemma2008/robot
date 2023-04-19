# Imports go at the top
from microbit import *
from Maqueen import *

robot = Maqueen()
while True:
    distancia = robot.read_distance()
    display.scroll(int(distancia))
    if distancia >= 5:
        robot.set_motor(0,0)
        robot.set_motor(1,0)
    else:
        robot.set_motor(0,0)
        robot.set_motor(1,0)
        
