import cv2
import imutils
import numpy as np
import pyautogui
import time
from datetime import datetime
from playsound import playsound

#   --------------- CONFIG ---------------
dir = "C:/Users/kijada/Pictures/PrtPsPy/"
sound = "D:\Documents\PythonProject\PrtScPy\sound\swiftly-610.wav"
start = (130, 80)       # screenshot start point
size = (1660, 950)      # screenshot size
height = 512            # resize height

#   --------------- VARIBLE ---------------
reg = start + size
current = cv2.cvtColor(np.array(np.zeros([size[1], size[0]], np.uint8)), cv2.COLOR_RGB2BGR)
last = cv2.cvtColor(np.array(pyautogui.screenshot(region=reg)), cv2.COLOR_RGB2BGR)

#   --------------- BLURRING ---------------
def blur(image, level):
    return(cv2.blur(image,(level, level)))


#   --------------- COMPARISON ---------------
def comparison(old, new):
    old = imutils.resize(old.copy(), height=height)
    new = imutils.resize(new.copy(), height=height)

    diff = new.copy()
    cv2.absdiff(old, new, diff)

    diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    for i in range(3):
        diff = cv2.dilate(diff, None, iterations=1 + i)

    (T, thresh) = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)
    box = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    box = imutils.grab_contours(box)

    cv2.imshow("Diff", diff)

    return(box)

#   --------------- MAKR CHANGES ---------------
def mark(image, tags):
    image = imutils.resize(image, height=height)
    for c in tags:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Marked changes", image)
    print("number of differences", len(tags))

#   --------------- SAVE IMAGE ---------------
ready = False
def save(changes):
    global ready
    global current
    global last
    if changes > 15:
        ready = True
        time.sleep(1)

    if changes > 5:
        ready = False
        image_name = "screenshot_" + datetime.now().strftime("%H-%M-%S_%d-%m-%Y") + ".png"
        cv2.imwrite(dir + image_name, current)
        print("Image saved")
        #playsound(sound)
        last = current
        time.sleep(1)

#   --------------- MAIN LOOP ---------------
while True:

    current = cv2.cvtColor(np.array(pyautogui.screenshot(region=reg)), cv2.COLOR_RGB2BGR)

    differences = comparison(current, last)
    mark(current, differences)
    save(len(differences))

    time.sleep(1)
    cv2.waitKey(1)

