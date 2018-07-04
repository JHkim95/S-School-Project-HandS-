import cv2
import numpy as np
import math

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (45, 45), 5)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0,40,60])
    upper_skin = np.array([20,150,255])
    mask_skin = cv2.inRange(hsv, lower_skin, upper_skin)                #손이라고 판단되는 색 영역만 걸러내는 mask.
    res_skin = cv2.bitwise_and(frame, frame, mask = mask_skin)

    thresh = cv2.threshold(mask_skin, 15, 255, cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
    if not contours:
        key = cv2.waitKey(1)&0xFF
        if key == ord("q"):
            break
        cv2.imshow("2", frame)
        
    else:
        cnts = max(contours, key = lambda x: cv2.contourArea(x))        #손의 굴곡진 영역까지을 잡아주는? 비슷한 느낌.
#   cnts = list(filter(lambda x: cv2.contourArea(x), contours))
#   (x, y, w, h) = cv2.boundingRect(cnts)
#   cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 0)

    hull = cv2.convexHull(cnts)                                         #손의 최외각 영역을 잡아주는? 그런 느낌.
    cv2.drawContours(frame, [cnts], 0, (0, 255, 0), 0)                  #색을 칠해준다.
    cv2.drawContours(frame, [hull], 0, (0, 0, 255), 0)                  #색을 칠해준다. 순서는 BGR이다.

    key = cv2.waitKey(1)&0xFF
    if key == ord("q"):
        break                                                           #q를 누를시 실행 종료.

#    cv2.imshow("1", res_skin)
#    cv2.imshow("3", mask_skin)
    cv2.imshow("2", frame)
#    cv2.imshow("4", thresh)

camera.release()
cv2.destoryAllWindows()

####용도####
#손을 제외한 부분을 검은색으로 처리하고, 손이라고 추측이 되는 부분만 추출(색으로 구별)
#손 하나만 추적

####문제점####
#조도에 따른 변화를 감지 못함.
