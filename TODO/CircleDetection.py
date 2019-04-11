import cv2
import numpy as np
import time
import math


class CircleDetection():
    def __init__(self, img):
        self.img = img
        self.kernel = 3
        self.centers = []
        self.width, self.height = self.img.shape[1], self.img.shape[0]
        self.firstJoint = []
        self.secJoint = []
        self.thirdJoint = []


    def ProcessCircle(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, self.kernel)
        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=30, param2=5,
                               minRadius=10, maxRadius=30)
        print(circles)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                self.centers.append(center)
                # circle center
                # cv2.circle(self.img, center, 1, (0, 100, 100), 2)
                # # circle outline
                # radius = i[2]
                # cv2.circle(self.img, center, radius, (255, 0, 255), 1)
                # cv2.putText(self.img, str(center[1]), (center[0] + 10, center[1] + 10),
			    #         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)    
            return self.centers
    
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
    
    # capture = cv2.VideoCapture(0)
    # capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # capture.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    # while True:
    #     ret, frame = capture.read()
    #     frame = cv2.resize(frame, (640, 360))
    #     cv2.imshow('haha', frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         cv2.imwrite('frame.png', frame)
    #         break

    # capture.release()
    # cv2.destroyAllWindows()
    image = cv2.imread('frame_center.png')
    
    boundaries = [
        ([17, 15, 100], [50, 56, 255])
    ]
    for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)
        cd = CircleDetection(output)
        cens = cd.ProcessCircle()
        print(cens)
        # show the images
        # cv2.imshow("images", np.hstack([image, cropGray]))
        cv2.imshow('output', output)
        cv2.waitKey(0)