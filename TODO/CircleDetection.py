import cv2
import numpy as np
import time
import math

class CircleDetection():
    def __init__(self, img):
        self.img = img
        self.kernel = 5
        self.centers = []
        self.width, self.height = self.img.shape[1], self.img.shape[0]
        self.firstJoint = []
        self.secJoint = []
        self.thirdJoint = []


    def ProcessCircle(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, self.kernel)
        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
        
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                self.centers.append(center)
                # circle center
                cv2.circle(self.img, center, 1, (0, 100, 100), 2)
                # circle outline
                radius = i[2]
                cv2.circle(self.img, center, radius, (255, 0, 255), 1)
                cv2.putText(self.img, str(center[1]), (center[0] + 10, center[1] + 10),
			            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            
        return self.img
    
    def AngleDetection(self):
        x = []
        y = []
        # Determine which is firts, sec and third joint
        if len(self.centers) == 3:
            for center in self.centers:
                x.append(center[0])
                y.append(center[1])
            firstJointNum = np.argmax(y)
            self.firstJoint = [x[firstJointNum], y[firstJointNum]]
            
            x.remove(x[firstJointNum])
            y.remove(y[firstJointNum])
            secJointNum = np.argmax(y)
            self.secJoint = [x[secJointNum], y[secJointNum]]
            self.thirdJoint = [x[1-secJointNum], y[1-secJointNum]]
            print(self.firstJoint, self.secJoint, self.thirdJoint)
        else:
            pass
        

if __name__ == '__main__':
    img = cv2.imread('TODO-detect-circle.png')
    cd = CircleDetection(img)
    gray = cd.ProcessCircle()
    cd.AngleDetection()
    cv2.imshow('Gray Scale', gray)
    cv2.waitKey(0)