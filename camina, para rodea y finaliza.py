# Imports go at the top
from microbit import *
from microrover import*

rover = Micro_Rover()
distancia= rover.get_distance()
andar1 = True
andar2= False

while(andar1 == True):
distancia= rover.get_distance()
rover.motor(255,255)
if distancia<10:
rover.motor(0,255)
sleep(500)
rover.motor(255,255)
sleep(500)
rover.motor(255,0)
sleep(500)
rover.motor(255,255)
sleep(500)
rover.motor(255,0)
sleep(500)
rover.motor(255,255)
sleep(500)
rover.motor(0,255)
andar1=False
andar2=True

while (andar2==True):
distancia= rover.get_distance()
rover.motor(255,255)
if distancia<10:
rover.motor(0,0)
