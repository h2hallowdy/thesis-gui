import cv2
import numpy as np
from numpy.linalg import inv
import glob
import math

def InverseRodrigues(rotVecs):
    theta = np.linalg.norm(rotVecs)
    r = rotVecs / theta
    r_calculate = np.reshape(r, (3, 1))
    I = np.eye(3, dtype=float)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    rx, ry, rz = rotVecs.item(0), rotVecs.item(1), rotVecs.item(2)
    temp = np.array([[0, -rz, ry], [rz, 0, -rx], [-ry, rx, 0]])
    rodrigues_mat = cos_theta * I + ((1 - cos_theta)*r_calculate).dot(r_calculate.T) + sin_theta * temp
    return rodrigues_mat

def ImgPoints2RealPoints(camearMtx, rodriguesMtx, translateMtx, imgPts, scaleFactor):
    translate = np.reshape(translateMtx, (3, 1))
    rInverse = inv(rodriguesMtx)
    mInverse = inv(camearMtx)
    print(rInverse.shape)
    print(mInverse.shape)
    print(translate.shape)
    print(imgPts.shape)
    realWorldPoints = rInverse.dot(mInverse).dot(scaleFactor * imgPts) - rInverse.dot(translate)
    return realWorldPoints


# Load previously saved data
with np.load('B.npz') as X:
    mtx, dist, rvects, tvects, corners = [X[i] for i in ('mtx','dist','rvecs','tvecs', 'corners')]
print(rvects.ndim)
s = 59.09118
point = np.array([[183, 285, 1]]).T
rotVec = InverseRodrigues(rvects)

realWorldPoints = ImgPoints2RealPoints(mtx, rotVec, tvects, point, s)
print(realWorldPoints)

def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

axis = np.float32([[4.48599188, 12.71384658, 0], [1.5,0,0], [0,0,-3]]).reshape(-1,3)
for fname in glob.glob('frame_left*.jpg'):
    
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    

    # if ret == True:
        
    
    # Find the rotation and translation vectors.
    _, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners, mtx, dist)
   
    # project 3D points to image plane
    imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
    
        
    img = draw(img,corners,imgpts)
    cv2.imshow('img',img)
    k = cv2.waitKey(0) & 0xFF
    if k == ord('s'):
        cv2.imwrite('haha.png', img)

cv2.destroyAllWindows()