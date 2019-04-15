from CircleDetection import CircleDetection
import cv2
import numpy as np 

img = cv2.imread('frame_check.jpg')
img = cv2.resize(img, (640, 480))

cg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(cg, 5)
th = cv2.adaptiveThreshold(median, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 2)

circles = cv2.HoughCircles(th, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=30, param2=20,
                               minRadius=20, maxRadius=30)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])      
        cv2.circle(median, center, 1, (0, 100, 100), 2)
        # circle outline
        radius = i[2]
        cv2.circle(median, center, radius, (255, 0, 0), 2)
        cv2.putText(median, str(center[1]), (center[0] + 10, center[1] + 10),
			        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)    
print(circles)
cv2.imshow("images", np.hstack([th, median]))

cv2.waitKey(0)