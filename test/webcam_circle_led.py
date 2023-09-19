import numpy as np
import cv2

webcam = cv2.VideoCapture(0)

while(1):
    _, frame = webcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11,11), 0)

    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100,
                               param1=100,param2=90,minRadius=0,maxRadius=400)
    if circles is not None:

        circles = np.round(circles[0, :].astype("int"))

        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 3)
            cv2.circle(frame, (x, y), 3, (0, 255, 0, -1))
            print("circle found")

    elif circles is None:
        print("no circle")



    else:
        print('circle none')
    cv2.imshow("circle", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break