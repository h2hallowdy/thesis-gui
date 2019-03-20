import os
import cv2

path = 'D:/Sample'
cap = cv2.VideoCapture(1)
img_counter = 0
max_counter = 100
while True:
    ret, img = cap.read()
    if not ret:
        break
    cv2.imshow('img', img)
    k = cv2.waitKey(1)
    
    if k & 0xFF == ord('q'):
        break
        print('bye bye')
    if k & 0xFF == ord('c'):
        while img_counter < max_counter:
            img_name = '{}.png'.format(img_counter)
            cv2.imwrite(os.path.join(path, img_name), img)
            img_counter += 1
        break
        print('Done')

cap.release()
cv2.destroyAllWindows()