import cv2 as cv
import numpy as np

lower = np.array([0, 50, 50])
upper = np.array([40, 170, 170])

vid = cv.VideoCapture(0)

while True:
    succes, img = vid.read()
    image= cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(image, lower, upper)
    mask_m = cv.flip(mask, 1)

    cv.imshow("Camera", mask_m)
    if cv.waitKey(1) == 27: break

vid.release()
cv.destroyAllWindows()
