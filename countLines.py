import math

import cv2
import numpy as np



img = cv2.imread('./images/verticallines.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
i = 0
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

while i < len(lines):
    for rho, theta in lines[i]:
        print(lines[i])
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        point1 = [x1, y1]
        point2 = [x2, y2]
        print("p1 " + str(point1))
        print("p2 " + str(point2))


        rawPixles = (x1 - x2) ^ 2 + (y1 - y2) ^ 2
        print("Raw pixles" + str(rawPixles))
        pixels = math.sqrt(abs(rawPixles))
        print(str(pixels) + " between points")
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        i += 1
print("There are " + str(i) + " lines in the image")
cv2.imwrite('houghlines3.jpg', img)
