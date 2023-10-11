import cv2

# Initialize the first camera
cap1 = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in camera).

# Initialize the second camera (change the index if needed)
cap2 = cv2.VideoCapture(1)  # 1 represents the second camera. You may need to adjust this index.

# Check if the cameras are opened successfully
if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Camera(s) not found or could not be opened.")
    exit()

while True:
    # Capture frames from the first camera
    ret1, frame1 = cap1.read()

    # Capture frames from the second camera
    ret2, frame2 = cap2.read()

    # Check if frames were successfully captured
    if not ret1 or not ret2:
        print("Error: Couldn't read frames from one or both cameras.")
        break

    # Display the frames from both cameras
    cv2.imshow('Camera 1', frame1)
    cv2.imshow('Camera 2', frame2)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera objects and close the display window
cap1.release()
cap2.release()
cv2.destroyAllWindows()