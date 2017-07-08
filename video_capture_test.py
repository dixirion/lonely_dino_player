

import sys, cv2 as cv
cap = cv.VideoCapture(0)
while True:
 ok, img = cap.read()
 if not ok:
  break

 cv.imshow("Captured image", img)
 gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

 gray = cv.GaussianBlur(gray, (7, 7), 1.5)

 edges = cv.Canny(gray, 1, 50)
 cv.imshow("edges", edges)
 if cv.waitKey(10000) > 0:
  break