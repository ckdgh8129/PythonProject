import cv2
import numpy as np 

cap = cv2.VideoCapture('opencv_study/video/walk.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

pre_frame = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize( frame , (640,480))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if pre_frame is None:
        pre_frame = gray
        continue

    # blur = cv2.GaussianBlur(gray, (5,5), 0)
    diff = cv2.absdiff(pre_frame, gray)

    _, thresh = cv2.threshold(
        diff, 120, 255, cv2.THRESH_BINARY
    )

    # morphology 작업하기 - 끊어진 부분들은 연결 시키기
    kernel = np.ones((5,5), np.uint8)
    #노이즈 제거
    opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, 
                              kernel, iterations=1)

    #끊어진 영역 연결
    linked = cv2.morphologyEx(
        opened, cv2.MORPH_CLOSE, kernel, iterations=10
    )

    thresh = cv2.dilate(thresh, kernel, iterations=2)
    

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = frame.copy()
    for cnt in contours:
        if cv2.contourArea(cnt) < 500:
            continue
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(
            result, 
            (x,y), 
            (x+w,y+h), 
            (0,0,255), 2)
        cv2.putText(
            result,
            'Motion',
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0,255,255),
            2
        )
        
    

    cv2.imshow('frame', diff)
    cv2.imshow('diff', thresh)
    cv2.imshow('result', result)
    pre_frame = gray

    if cv2.waitKey(delay) == 27:
        break