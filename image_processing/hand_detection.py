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
    mask_skin = cv2.inRange(hsv, lower_skin, upper_skin)
    res_skin = cv2.bitwise_and(frame, frame, mask = mask_skin)

    thresh = cv2.threshold(mask_skin, 15, 255, cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
    if not contours:
        key = cv2.waitKey(1)&0xFF

        if key == ord("q"):
            break

        cv2.imshow("2", frame)
        
    else:
        cnts = max(contours, key = lambda x: cv2.contourArea(x))
#   cnts = list(filter(lambda x: cv2.contourArea(x), contours))
#   (x, y, w, h) = cv2.boundingRect(cnts)
#   cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 0)

    hull = cv2.convexHull(cnts)

#    drawing = np.zero(frame.shape, np.uint8)
    cv2.drawContours(frame, [cnts], 0, (0, 255, 0), 0)
    cv2.drawContours(frame, [hull], 0, (0, 0, 255), 0)

    key = cv2.waitKey(1)&0xFF

    if key == ord("q"):
        break

#    cv2.imshow("1", res_skin)
#    cv2.imshow("3", mask_skin)
    cv2.imshow("2", frame)
#    cv2.imshow("4", thresh)

camera.release()
cv2.destoryAllWindows()
