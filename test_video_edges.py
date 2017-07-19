import sys, cv2 as cv
import os

ffmpeg_dll_path = r'E:\python_examples\opencv-3.2.0-vc14\opencv\build\bin'
# ffmpeg_dll_path = r'C:\dev_projects\opencv-3.2.0-vc14\opencv\build\bin'
os.environ["PATH"] += os.pathsep +  ffmpeg_dll_path

cap = cv.VideoCapture('test_data/t_rex_test_video.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 0, 50)

    cv.imshow('frame',edges)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
