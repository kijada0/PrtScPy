import os
import cv2
import imutils
import numpy as np
import pyautogui
import time
from datetime import datetime
import winsound

flag = False

dir = "pictures/"
reg = (130, 80, 1660, 950)

pic1 = cv2.cvtColor(np.array(pyautogui.screenshot(region=reg)), cv2.COLOR_RGB2BGR)

while True:
    pic0 = pic1
    pic1 = cv2.cvtColor(np.array(pyautogui.screenshot(region=reg)), cv2.COLOR_RGB2BGR)

    pic0a = imutils.resize(pic0, height=512)
    pic1a = imutils.resize(pic1, height=512)

    diff = pic0a.copy()
    cv2.absdiff(pic0a, pic1a, diff)

    diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    for i in range(3):
        diff = cv2.dilate(diff, None, iterations=1+i)

    (T, thresh) = cv2.threshold(diff, 3, 255, cv2.THRESH_BINARY)
    cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(pic1a, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Marked differences" , pic1a)
    print("number of differences", len(cnts))

    if len(cnts) > 999:
        flag = False
        pic_name = "screenshot_" + datetime.now().strftime("%H-%M-%S_%d-%m-%Y") + ".png"
        cv2.imwrite(dir + pic_name, pic1)
        winsound.PlaySound("*", winsound.SND_ALIAS)
        print("Image saved")
        time.sleep(3)

    cv2.waitKey(1)
    time.sleep(1)
