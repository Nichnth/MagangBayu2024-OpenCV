import cv2 as cv
import numpy as np

lower = np.array([80, 20, 20])
upper = np.array([100, 255, 255])

img = cv.imread('tugas1.png')

image= cv.cvtColor(img, cv.COLOR_BGR2HSV)
mask = cv.inRange(image, lower, upper)

contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

if len(contours) != 0:
        for contour in contours:
            if cv.contourArea(contour) > 600:
                x, y, w, h = cv.boundingRect(contour)
                cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 2)

cv.imshow("mask", mask)
cv.imshow("picture", img)

cv.waitKey(0)
cv.destroyAllWindows()
