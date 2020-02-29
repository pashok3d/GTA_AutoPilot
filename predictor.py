import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D
from grabkeys import key_check
import os

from keras.models import load_model
from scanner import process_img

#loading model
model = load_model('model.h5')

#W key press-time bounds
PRESS = 0.23
RELEASE = 0.30

def auto_pilot(direction):
    if direction == 1:      #Left
        ReleaseKey(D)
        PressKey(A)
    elif direction == 2:    #Right
        ReleaseKey(A)
        PressKey(D)
    else:                   #Straight
        ReleaseKey(A)
        ReleaseKey(D)

def drive(times):
    elapsed_time = times[0]                 #Period of time from last W-key full release
    press_start = times[1]                  #Last time W-key was pressed
    loop = times[2]                         #Period of while loop
    press_time = time.time() - press_start  #Period of time W-key was pressed
    if elapsed_time < PRESS:
        if not press_start:
           press_start = time.time()
        PressKey(W)
        return [elapsed_time,press_start]
    elif elapsed_time < RELEASE:
        ReleaseKey(W)
        if press_start and (press_time > 0.25 or press_time) < 0.15:
           print('Warning: Press_time ' + str(press_time) + ' is out of bounds. Consider tuning PRESS/RELEASE parameters if the error occurs frequently.')
        return [elapsed_time,0.0]
    else:
        ReleaseKey(W)
        if press_start and (press_time > 0.25 or press_time) < 0.15:
           print('Warning: Press_time ' + str(press_time) + ' is out of bounds. Consider tuning PRESS/RELEASE parameters if the error occurs frequently.')
        return [0.0,0.0]

def main():
    for i in list(range(3))[::-1]:
        print(str(i+1))
        time.sleep(1)

    last_time = time.time()
    elapser = 0.0
    start = 0.0
    pause = False

    while True:

        keys = key_check()

        if 'Q' in keys:
            break   

        if 'P' in keys:
            if pause:
                pause = False
                time.sleep(1)
                print('UNPAUSED')
            else:
                pause = True  
                time.sleep(1)
                print('PAUSED')

        if not pause:

            loop = time.time() - last_time
            elapser = elapser + loop
            elapser, start = drive([elapser,start,loop])
            last_time = time.time()
            screen = grab_screen(region=(0,40,640,480))
            proc_img = process_img(screen)

            sample = proc_img.reshape(-1,100,100,1)
            sample = sample.astype('float32')
            sample /= 255

            pred = model.predict(sample)

            auto_pilot(np.argmax(pred))
            
main()