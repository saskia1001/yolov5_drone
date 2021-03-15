from djitellopy import tello
from time import sleep
import KeyPressModule as kp 

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey('LEFT'): lr = -speed
    elif kp.getKey('RIGHT'): lr = speed

    if kp.getKey('UP'): fb = speed
    elif kp.getKey('DOWN'): fb = -speed

    if kp.getKey('w'): ud = speed
    elif kp.getKey('s'): ud = -speed

    if kp.getKey('a'): yv = speed
    elif kp.getKey('d'): yv = -speed

    if kp.getKey('q'): me.land()

    if kp.getKey('e'): me.takeoff()

    if kp.getKey('x'):
        me.land()
        me.end()
        sleep(.4)
        exit()

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    sleep(0.05)
