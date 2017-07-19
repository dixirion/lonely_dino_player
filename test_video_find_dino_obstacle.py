import sys, cv2
import os
import numpy as np
import time


ffmpeg_dll_path = r'E:\python_examples\opencv-3.2.0-vc14\opencv\build\bin'
# ffmpeg_dll_path = r'C:\dev_projects\opencv-3.2.0-vc14\opencv\build\bin'
os.environ["PATH"] += os.pathsep +  ffmpeg_dll_path

cap = cv2.VideoCapture('test_data/t_rex_test_video.avi')

while(cap.isOpened()):
    start_time = time.time()

    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = frame

    img_rgb = gray
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('test_data/dino.png',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    delta_time = round((time.time() - start_time)*1000,2)
    t = 'T msec: ' + str(delta_time)
    cv2.putText(img_rgb, t, (10, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, 255,2)

    #cv2.imwrite('res.png',img_rgb)

    cv2.imshow('frame', img_rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




cap.release()
cv.destroyAllWindows()
