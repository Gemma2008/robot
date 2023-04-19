# Imports go at the top
from microbit import *
from Maqueen import *

robot = Maqueen()
robot.set_motor(0,255)
robot.set_motor(1, 255)
sleep(3000)
robot.set_motor(0,0)
robot.set_motor(1,0)
