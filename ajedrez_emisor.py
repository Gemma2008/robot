from microbit import *
import radio
from Maqueen import*

radio.on()
radio.config(channel=8, group=0)

robot = Maqueen()

def moverComoTorre():
    for i in range(1,8):
     robot.mover_celda()

def moverComoCaballo():
    robot.mover_celda()
    robot.mover_celda()
    robot.mover_celda()
    robot.girar_derecha()
    robot.mover_celda()

    
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        moverComoTorre()
    elif button_a.is_pressed():
        moverComoCaballo()
        sleep(100)
    elif button_b.is_pressed():
        robot.mover_celda()
        sleep(100)
    else:
        sleep(100)

