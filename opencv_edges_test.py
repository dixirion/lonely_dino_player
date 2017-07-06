import sys, cv2 as cv # Импортируем системный модуль
 # Импортируем модуль OpenCV (cv2) под именем cv
img = cv.imread(sys.argv[1], 1) # Загружаем изображение
cv.imshow("original", img) # Отрисовываем изображение
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 # Конвертируем цветное изображение в монохромное
gray = cv.GaussianBlur(gray, (7, 7), 1.5)
 # Добавляем размытие
edges = cv.Canny(gray, 0, 50) # Запускаем детектор ребер
cv.imshow("edges", edges) # Отображаем результат
cv.waitKey() # Ожидаем нажатия любой клавиши для завершения работы