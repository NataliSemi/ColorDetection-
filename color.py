import cv2
import numpy as np

# Specifying upper and lower ranges of color to detect in hsv format
light_blue = np.array([110,50,50])
dark_blue = np.array([130,255,255])

# Capturing webcam footage
webcam_video = cv2.VideoCapture(0)

while True:
    success, video = webcam_video.read() # Reading webcam footage

    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format

    mask = cv2.inRange(img, light_blue, dark_blue) # Masking the image to find our color

    mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image

    number_of_red = 0

    # Finding position of all contours
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 500:
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle
                number_of_red+=1
                print(number_of_red)



    cv2.imshow("mask image", mask) # Displaying mask image

    cv2.imshow("window", video) # Displaying webcam image

    cv2.waitKey(1)