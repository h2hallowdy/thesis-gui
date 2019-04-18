import cv2
import numpy as np 

calibrationSquareDimension = 1          # meters
arucoSquareDimenstion = 12              # meters
size = (9, 6)
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

capture = cv2.VideoCapture(0)
fps = capture.get(cv2.CAP_PROP_FPS)
wait_time = 1000 / fps
cv2.namedWindow("Webcam", cv2.WINDOW_AUTOSIZE)
count = 0
while True:
    ret, frame = capture.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Find the chess board corners
        found, corners = cv2.findChessboardCorners(gray, size, cv2.CALIB_CB_ADAPTIVE_THRESH | cv2.CALIB_CB_NORMALIZE_IMAGE)
        frame_copy = frame.copy()
        
        cv2.drawChessboardCorners(frame_copy, size, corners, found)
        if found:
            count += 1
            cv2.imshow("Webcam", frame_copy)

        else:
            cv2.imshow("Webcam", frame)

        key = cv2.waitKey(int(wait_time)) & 0xFF
        if key == ord('c'):
            if count > 15:
                ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
            break
    else:
        break
    

capture.release()
cv2.destroyAllWindows()
