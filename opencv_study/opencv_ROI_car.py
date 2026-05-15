import cv2
import numpy as np

cap = cv2.VideoCapture('opencv_study/video/motion_car.mp4')

paused = False #영상 일시 정지용
roi_points = [] #좌표 저장용
current_frame = None
display = None
sel_roi = None

mask_enabled = False

def mouse_pos(event, x, y, flags, param):
    global roi_points, current_frame, display , sel_roi, mask_enabled
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_points.append((x,y))# 마우스 클릭 좌표 저장
        cv2.circle( display, (x,y), 5, (0,255,150), -1)

        if len(roi_points) >= 2: #좌표 두번 이상 클릭했다면
            cv2.line(display,
                     roi_points[-2],
                     roi_points[-1],
                     (255,0,0),2
                    )
    elif event == cv2.EVENT_RBUTTONDOWN: #좌표 전부 찍었다면 마우스 오른쪽 클릭
        if len(roi_points) >= 3:
            mask_enabled = True
            cv2.line( display, roi_points[-1], roi_points[0], (255,0,0), 2)

        # if len(roi_points) == 2:
        #     x1, y1 = roi_points[0]
        #     x2, y2 = roi_points[1]

        #     start_x = min(x1,x2)
        #     end_x = max(x1,x2)
        #     start_y = min(y1,y2)
        #     end_y = max(y1,y2)

        #     sel_roi = (start_x, start_y, end_x, end_y)

        #     cv2.rectangle(display, 
        #                   (start_x, start_y), 
        #                   (end_x, end_y), 
        #                   (255,0,0), 2)

        #     roi = current_frame[start_y:end_y, start_x:end_x]
        #     cv2.imshow('roi', roi)


cv2.namedWindow('org')
cv2.setMouseCallback('org', mouse_pos)

while True:
    if not paused:
        r, frame = cap.read()
        if not r:
            break
        frame = cv2.resize( frame , (480,640))

        current_frame = frame.copy()
        display = frame.copy()
        
        if mask_enabled:
            pts = np.array(roi_points, np.int32)
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            cv2.fillPoly(mask, [pts], 255)

            roi = cv2.bitwise_and(frame, frame, mask=mask)
            cv2.polylines(display, [pts], 
                          isClosed=True, color=(0,255,0), thickness=2)
            _, thresh = cv2.threshold(
                roi, 120, 255, cv2.THRESH_BINARY
            )
            kernel = np.ones((5,5), np.uint8)
            thresh = cv2.morphologyEx(
                thresh, cv2.MORPH_OPEN, kernel, iterations=1
              )
            thresh = cv2.morphologyEx(
                thresh, cv2.MORPH_CLOSE, kernel, iterations=2
            )

            contours,_ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
            for cnt in contours:
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(display, (x,y), (x+w, y+h), (0,0,255), 2)

            # cv2.imshow('roi', roi)

    cv2.imshow('org', display)
    

    k = cv2.waitKey(30)
    if k == 27:
        break
    elif k ==32: #스페이스바 키 값은 32 - 일시정지용으로 사용할꺼 (아스키코드)
        paused = not paused
    elif k==ord('r'):
        roi_points = []
        current_frame is not None
        display = current_frame.copy()

cap.release()
cv2.destroyAllWindows()