import os
import cv2
import imutils

dir = "test_sc/"
list = os.listdir(dir)
print("File list: ", list)

pic0 = cv2.imread(dir+list[4])
pic0a = imutils.resize(pic0, height=512)

pic1 = cv2.imread(dir+list[1])
pic1a = imutils.resize(pic1, height=512)

diff = pic0a.copy()
cv2.absdiff(pic0a, pic1a, diff)

diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
for i in range(3):
    diff = cv2.dilate(diff, None, iterations=1+i)

(T, thresh) = cv2.threshold(diff, 3, 255, cv2.THRESH_BINARY)
cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

print(len(cnts))
for c in cnts:
    # nicely fiting a bounding box to the contour
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(pic1a, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow(list[0], pic1a)

cv2.waitKey(0)
cv2.destroyAllWindows()

