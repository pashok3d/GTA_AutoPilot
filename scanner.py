import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D
from grabkeys import key_check
import os

def process_img(image):
    proc_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    proc_img = proc_img[260:,:]     #Giving up top part of the screen 
    proc_img = cv2.resize(proc_img, (100,100))
    return proc_img

def keys_to_output(keys):
    output = 3
    if 'O' in keys:
        output = 0
        print('STRAIGHT')
    elif 'K' in keys:
        output = 1
        print('LEFT')
    elif 'L' in keys:
        output = 2
        print('RIGHT')       
    return output 

def drive(elapsed_time):
    if elapsed_time < 0.15:
        PressKey(W)
        return elapsed_time
    elif elapsed_time < 0.20:
        ReleaseKey(W)
        return elapsed_time
    else:
        ReleaseKey(W)
        return 0.0

def main():

    for i in list(range(3))[::-1]:
        print(str(i+1))
        time.sleep(1)

    last_time = time.time()
    elapser = 0.0
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

            elapser = elapser + (time.time() - last_time)
            elapser = drive(elapser)
            last_time = time.time()
            screen = grab_screen(region=(0,40,640,480))
            proc_img = process_img(screen)

            output = keys_to_output(keys)
            if output < 3:
                training_data.append([proc_img,output])

            if len(training_data) % 500 == 0:
                print(len(training_data))
                np.save(file_name,training_data)


if __name__ == '__main__':

    file_name = 'training_data.npy'

    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        training_data = list(np.load(file_name))
    else:
        print('File does not exist, starting fresh!')
        training_data = []

    main()  