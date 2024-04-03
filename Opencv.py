import cv2
import numpy as np
img = cv2.imread('imgs/geometry.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Anh muc xam',gray)
cv2.waitKey()
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
cv2.imshow('Hough xac xuat', edges)
cv2.waitKey()
lines = cv2.HoughLines(edges, 1, np.pi/180, 100)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow('Hough xac xuat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()