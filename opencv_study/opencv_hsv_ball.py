import cv2
import numpy as np

cap = cv2.VideoCapture("opencv_study/video/ball.mp4")

while True:
    r, fr = cap.read()
    if not r:
        break

    fr = cv2.resize(fr, ( 480, 640 ))
    hsv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array( [0,100,100] )
    up_red1 = np.array( [10,255,255] )

    lower_red2 = np.array( [150,100,100] )
    up_red2 = np.array( [180,255,255] )

    mask1 = cv2.inRange(hsv, lower_red1, up_red1)
    mask2 = cv2.inRange(hsv, lower_red2, up_red2)

    mask = mask1 + mask2

    kernel = np.ones((5,5), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    fr_copy = fr.copy()
    for cnt in contours:

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(fr, (x,y), (x+w, y+h), (0,0,255), 2)



    cv2.imshow("video", fr)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", fr_copy)
    if cv2.waitKey(30) ==27: break

cap.release()
cv2.destroyAllWindows()