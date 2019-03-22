import os
import cv2

path = 'D:/Sample'
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
img_counter = 0
max_counter = 100
while True:
    ret, img = cap.read()
    if not ret:
        break
    cv2.imshow('img', img)
    k = cv2.waitKey(1)
    
    if k & 0xFF == ord('q'):
        print('bye bye')
        break
        
    if k & 0xFF == ord('c'):
        while img_counter < max_counter:
            img_name = '{}.png'.format(img_counter)
            cv2.imwrite(os.path.join(path, img_name), img)
            img_counter += 1
        print('Done')
        break
        

cap.release()
cv2.destroyAllWindows()