import cv2
import numpy as np
import math
import socket

left_3 = 100
left_2 = 200
left_1 = 300
right_3 = 700
right_2 = 600
right_1 = 500

direction = "00"
forward = "00"
backward = "00"
breaker = "00"
total_data = ""

host = ''
port = 
buf = 
ADDR = (host, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (800, 600))
    frame = cv2.GaussianBlur(frame, (31, 31), 5)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_Red = cv2.inRange(hsv, np.array([153, 100, 100]), np.array([179, 255, 255]))
    mask_Blu = cv2.inRange(hsv, np.array([82, 100, 80]), np.array([128, 255, 255]))

    res_Red = cv2.bitwise_and(frame, frame, mask = mask_Red)
    res_Blk = cv2.bitwise_and(frame, frame, mask = mask_Blu)

    thresh = cv2.threshold(mask_Red, 15, 255, cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
    thresh1 = cv2.threshold(mask_Blu, 15, 255, cv2.THRESH_BINARY)[1]
    contours1 = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]

    if not contours:
        direction = "00"
        forward = "00"
        pass
    else:
        cnts = max(contours, key = lambda x : cv2.contourArea(x))
        x, y, w, h = cv2.boundingRect(cnts)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 5)
        cen_x = (2*x + w) / 2
        cen_y = (2*y + h) / 2

        forward = "+1"

        if cen_x < left_3:
            direction = "+3"
        elif left_3 <= cen_x < left_2:
            direction = "+2"
        elif left_2 <= cen_x < left_1:
            direction = "+1"
        elif right_1 < cen_x <= right_2:
            direction = "-1"
        elif right_2 < cen_x <= right_3:
            direction = "-2"
        elif right_3 < cen_x:
            direction = "-3"
        else:
            direction = "00"

    if not contours1:
        backward = "00"
        pass
    else:
        cnts1 = max(contours1, key = lambda x1 : cv2.contourArea(x1))
        x1, y1, w1, h1 = cv2.boundingRect(cnts1)
        cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (0,255,0), 5)
        backward = "+1"

    if (forward == "00") & (backward == "00") & (direction == "00"):
        breaker = "+1"
    else:
        breaker = "00"

    total_data = forward + backward + direction + breaker

    client.send(total_data.encode())

    key = cv2.waitKey(1)&0xFF
    if key == 27:
        break

    cv2.imshow("1", res_Blk)
    cv2.imshow("2", res_Red)
    cv2.imshow("3", frame)
    print(forward)
    print(backward)
    print(direction)
    print(breaker)
    print(total_data)
    print("==================")

cap.release()
cv2.destroyAllWindows()
