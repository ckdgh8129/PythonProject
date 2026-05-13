import cv2
import numpy as np

cap = cv2.VideoCapture('opencv_study/video/video.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

pre_frame = None

#배경 제거기 만들기
bgdelete = cv2.createBackgroundSubtractorMOG2(
    history=200, #배경을 학습할 프레임 수 (너무 낮으면 잠시 멈춘사람도 배경취급)
    varThreshold=20, # 얼마나 달라 져야 움직임으로 판단하나?
    detectShadows=True # 그림자 처리 여부
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize( frame , (480,640))

    #배경 제거
    fmask = bgdelete.apply(frame, learningRate=0.005)

    _, thresh = cv2.threshold(
        fmask, 200, 255, cv2.THRESH_BINARY
    )

    kernel = np.ones((5,5), np.uint8)

    #모폴로지 노이즈 제거
    mask = cv2.morphologyEx(
        thresh,cv2.MORPH_OPEN,
        kernel, iterations=1
    )
    #영역 확장
    mask = cv2.dilate( mask, kernel, iterations=2)

    contours,_ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = frame.copy()

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 500:
            continue
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(
            result,
            (x,y),
            (x+w,y+h),
            (0,0,255),2
        )
        cv2.putText(
            result,
            'Motion',
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0,0,255),
            2
        )
    
    
    

    cv2.imshow('original', frame)
    cv2.imshow('blur', mask)
    cv2.imshow('motion', result)
    cv2.imshow('fmask', fmask)
    
    if cv2.waitKey(delay) == 27:
        break

#현재 프레임을 다음 프레임과 비교해야되니까 저장
    


cap.release()
cv2.destroyAllWindows()