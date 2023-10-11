import numpy as np
import cv2
import serial
import time


arduino = serial.Serial('/dev/ttyUSB0',115200)
j = 0
k = 0
sign = 'haha' 

def sign_color(img):
    
    global j
    global k
    global sign
    
    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blue_lower = np.array([90, 50, 50], np.uint8)
    blue_upper = np.array([130, 255, 200], np.uint8)
    blue_mask1 = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    red_lower = np.array([170,70,50], np.uint8)
    red_upper = np.array([180,255,200], np.uint8)
    red_mask1 = cv2.inRange(hsvFrame, red_lower, red_upper)

    yellow_lower = np.array([20,100,100], np.uint8)
    yellow_upper = np.array([40,255,255], np.uint8)
    yellow_mask1 = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    kernel = np.ones((5, 5), "uint8")

    blue_mask2 = cv2.dilate(blue_mask1, kernel)
    red_mask2 = cv2.dilate(red_mask1, kernel)
    yellow_mask2 = cv2.dilate(yellow_mask1, kernel)



    res_blue = cv2.bitwise_and(img, img, mask = blue_mask2)
    res_red = cv2.bitwise_and(img, img, mask = red_mask2)
    res_yellow = cv2.bitwise_and(img, img, mask = yellow_mask2)


    gray_blue = cv2.cvtColor(res_blue, cv2.COLOR_BGR2GRAY)
    gray_red = cv2.cvtColor(res_red, cv2.COLOR_BGR2GRAY)
    gray_yellow = cv2.cvtColor(res_yellow, cv2.COLOR_BGR2GRAY)

    blurred_blue = cv2.GaussianBlur(gray_blue, (11,11), 0)
    blurred_red = cv2.GaussianBlur(gray_red, (11,11), 0)
    blurred_yellow = cv2.GaussianBlur(gray_yellow, (11,11), 0)

    circles_blue = cv2.HoughCircles(blurred_blue, cv2.HOUGH_GRADIENT, 1, 100,
                               param1=100,param2=90,minRadius=0,maxRadius=400)

    circles_red = cv2.HoughCircles(blurred_red, cv2.HOUGH_GRADIENT, 1, 100,
                               param1=100,param2=90,minRadius=0,maxRadius=400)

    
    if k == 0:
        if circles_blue is not None:

                circles_blue = np.round(circles_blue[0, :].astype("int"))

                time.sleep(5)
                #print('blue')
                arduino.write(b'1\n')
                arduino.reset_output_buffer()
                j = 1
                k = 1

                
                
        elif circles_red is not None:
                circles_red = np.round(circles_red[0, :].astype("int"))

                time.sleep(5)
                #print('red')
                arduino.write(b'2\n')
                arduino.reset_output_buffer()
                j = 2
                k = 1
               
                
        

        '''contours, hierarchy = cv2.findContours(yellow_mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                      area = cv2.contourArea(contour)
                      if(area > 5000):
                           time.sleep(5)
                           #print('yellow')
                           arduino.write(b'3\n')
                           arduino.reset_output_buffer()
                           j = 3
                           k = 1'''

        if j == 1:
                 sign = 'blue_shroom'
                 
                 #return sign
                 

        elif j == 2:
                 sign = 'red_shroom'
               
                 #return sign
                 

        elif j == 3:
                 sign = 'yellow_shroom'
                 
                 #return sign
                 
            
            
    return sign
    



def shroom_rec():

    webcam = cv2.VideoCapture(0)
    
    shroomx = 0
    p = 0
    

    while webcam.isOpened():
        ret, frame = webcam.read()
        if ret:
            
            cv2.imshow('cc', frame)
        else:
            break
        if cv2.waitKey(50) == ord('q'):
            break

        shroom_g = sign_color(frame)
        print(shroom_g)
        

        if shroom_g == 'blue_shroom':

              hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
              blue_lower = np.array([90, 50, 50], np.uint8)
              blue_upper = np.array([130, 255, 200], np.uint8)
              blue_mask1 = cv2.inRange(hsvFrame, blue_lower, blue_upper)
              kernel = np.ones((5, 5), "uint8")
              blue_mask2 = cv2.dilate(blue_mask1, kernel)


              contours, hierarchy = cv2.findContours(blue_mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
              for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area > 1000):
                    #print('blue shroom')

                    x, y, w, h = cv2.boundingRect(contour)
                    frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

                    onex = int(x+(w/2))

                    while p < 10000:
                         shroomx = shroomx + onex
                         p = p+1
                    averagex = int(shroomx/10000)
                    p = 0
                    shroomx = 0
                    if 610 < averagex & averagex < 670:
                         #print('stop')
                         arduino.write(b'4\n')
                         arduino.reset_output_buffer()

        if shroom_g == 'red_shroom':

              hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
              red_lower = np.array([170,70,50], np.uint8)
              red_upper = np.array([180,255,200], np.uint8)
              red_mask1 = cv2.inRange(hsvFrame, red_lower, red_upper)
              kernel = np.ones((5, 5), "uint8")
              red_mask2 = cv2.dilate(red_mask1, kernel)


              contours, hierarchy = cv2.findContours(red_mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
              for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area > 1000):
                    #print('red shroom')

                    x, y, w, h = cv2.boundingRect(contour)
                    frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)

                    onex = int(x+(w/2))

                    while p < 10000:
                         shroomx = shroomx + onex
                         p = p+1

                    averagex = int(shroomx/10000)
                    p = 0
                    shroomx = 0
                    #if 640 - 30 < averagex < 640 + 30 send stop signal
                    if 610 < averagex & averagex < 670:
                         #print('stop')
                         arduino.write(b'4\n')
                         arduino.reset_output_buffer()

        '''if shroom_g == 'yellow_shroom':

             hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
             yellow_lower = np.array([20,100,100], np.uint8)
             yellow_upper = np.array([40,255,255], np.uint8)
             yellow_mask1 = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)
             kernel = np.ones((5,5), "uint8")
             yellow_mask2 = cv2.dilate(yellow_mask1, kernel)


             contours, hierarchy = cv2.findContours(yellow_mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
             for pic, contour in enumerate(contours):
              area = cv2.contourArea(contour)
              if(area > 1000):
                   #print('yellow shroom')
                   arduino.write(b'4\n')
                   arduino.reset_output_buffer()

                   x, y, w, h = cv2.boundingRect(contour)
                   frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (60, 100, 100), 2)

                   onex = int(x+(w/2))

                   while p < 10000:
                         shroomx = shroomx + onex
                         p = p+1

                   averagex = int(shroomx/10000)
                   p = 0
                   shroomx = 0
                   if 610 < averagex & averagex < 670:
                        #print('stop')
                        arduino.write(b'4\n')
                        arduino.reset_output_buffer()'''
                        
                        
                        
                        
                        
                        
shroom_rec()
























