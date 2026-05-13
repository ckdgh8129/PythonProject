import cv2

cap = cv2.VideoCapture('opencv_study/video/motion_car.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

pre_frame = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize( frame , (480,640))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if pre_frame is None:
        pre_frame = gray
        continue

    blur = cv2.GaussianBlur(gray, (5,5), 0)
    if pre_frame is None:
        pre_frame = blur
        continue
    diff = cv2.absdiff(pre_frame, blur)

    _, thresh = cv2.threshold(
        diff, 11, 255, cv2.THRESH_BINARY
    )
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = frame.copy()
    for cnt in contours:
        if cv2.contourArea(cnt) < 900: 
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(
            result,
            (x, y), 
            (x+w, y+h), 
            (0, 0, 255), 2
        )
        cv2.putText(
            result,
            'Car',
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 250, 150),
            2
        )

    
    cv2.imshow('frame', frame)
    cv2.imshow('result', result)
    cv2.imshow('diff', diff)

    pre_frame = blur

    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()