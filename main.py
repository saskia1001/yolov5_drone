'''
The script allows to control a Tello drone (SDK 2.0) and 
streems the video feed to a device where a real-time object 
detection runs on the feed.
'''

import numpy as np
import cv2.cv2 as cv2
import torch
import time
from PIL import Image
import djitellopy as tello
import KeyPressModule as kp

# Load model from PyTorch Hub
model = torch.hub.load('ultralytics/yolov5', 
                        'custom', 
                        path_or_model='best.pt')  # Path to custom model weights

# Intitialize drone
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

global img

# Initiate video stream
me.streamon()

# Set control of drone
def getKeyboardInput():
    '''
    Function allows the control of the drone via keyboard.

        Parameters: 
            none
        Returns:
            [lr, fb, ud, yv]: list of integers
            lr: left, right
            fb: forwards, backwards
            ud: up, down
            yv: yaw velocity
    '''
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

    if kp.getKey('q'): me.land(); time.sleep(3)

    if kp.getKey('e'): me.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'{time.time()}.jpg', img)  # Choose path to store the image
        time.sleep(.3)

    if kp.getKey('x'):
        me.land()
        me.end()
        time.sleep(.3)
        exit()

    return [lr, fb, ud, yv]

# Control the drone
# Stream the video stream with object detection on screen
while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    img = me.get_frame_read().frame
    img_detect = model(img, size=416)  # default YOLOv5 size=460, custome model was trained with 416
    img_show = img_detect.render()
    cv2.imshow("Image", img_show[0])
    cv2.waitKey(1)