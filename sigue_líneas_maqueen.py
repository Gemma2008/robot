from microbit import *
from maqueen import *

robot = Maqueen()

while True:
    left_line = robot.read_patrol(0)
    right_line = robot.read_patrol(1)
    
    if left_line == 0 and right_line == 0: # Ambos sensores detectan línea
        display.show(Image.ARROW_N)
        robot.forward()
    elif left_line == 1 and right_line == 0: # Solo el sensor izquierdo detecta línea
        display.show(Image.ARROW_E)
        robot.turn_right()     
    elif left_line == 0 and right_line == 1: # Solo el sensor derecho detecta línea
        display.show(Image.ARROW_W)
        robot.turn_left()
    elif left_line == 1 and right_line == 1: # Ambos sensores no detectan línea
        display.show(Image.ARROW_N)
        robot.set_motor(0,-50)
        robot.set_motor(1,-50) 
