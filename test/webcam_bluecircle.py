import numpy as np
import cv2
import serial


webcam = cv2.VideoCapture(0)


while(1):
    _, frame = webcam.read()
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blue_lower = np.array([90, 50, 50], np.uint8)
    blue_upper = np.array([130, 255, 255], np.uint8)
    blue_mask1 = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    kernel = np.ones((5, 5), "uint8")

    blue_mask2 = cv2.dilate(blue_mask1, kernel)

    res_blue = cv2.bitwise_and(frame, frame, mask = blue_mask2)


    gray = cv2.cvtColor(res_blue, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11,11), 0)

    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100,
                               param1=100,param2=90,minRadius=0,maxRadius=400)
    if circles is not None:

        circles = np.round(circles[0, :].astype("int"))

        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 3)
            cv2.circle(frame, (x, y), 3, (0, 255, 0, -1))
            print('blue circle')
            #arudino.write(b'100\n')
            #.reset_output_buffer()

    else:
        print('nothing')
        #arudino.write(b'0\n')
        #arudino.reset_output_buffer()


    cv2.imshow("circle", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break