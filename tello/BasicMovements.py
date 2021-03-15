import djitellopy as tello
from time import sleep

me = tello.Tello()
me.connect()

me.takeoff()
print(me.get_battery())
me.send_rc_control(0,10,0,0)
sleep(1)
me.send_rc_control(0,0,0,0)
me.land()