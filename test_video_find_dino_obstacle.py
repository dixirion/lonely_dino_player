import sys, cv2
import os
import numpy as np
import time


# ffmpeg_dll_path = r'E:\python_examples\opencv-3.2.0-vc14\opencv\build\bin'
ffmpeg_dll_path = r'C:\dev_projects\opencv-3.2.0-vc14\opencv\build\bin'
os.environ["PATH"] += os.pathsep +  ffmpeg_dll_path

start_frame_offset = 0
frame_delay_obstcl = 10
frame_delay_game_over = 30

cap = cv2.VideoCapture('test_data/t_rex_test_video.avi')
frame_counter = 0


while(cap.isOpened()):
    start_time = time.time()
    prev_time = start_time

    time_log = []
    time_log.append('Frame #' + str(frame_counter))

    ret, frame = cap.read()
    frame_counter +=1

    if frame_counter <start_frame_offset:
        continue

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = frame

    img_rgb = gray
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    dino_img = cv2.imread('test_data/dino.png', 0)
    obstcl_img1 = cv2.imread('test_data/obstacle_1.png', 0)
    obstcl_img2 = cv2.imread('test_data/obstacle_2.png', 0)
    obstcl_img3 = cv2.imread('test_data/obstacle_3.png', 0)
    game_over_img = cv2.imread('test_data/game_over.png', 0)
    w1, h1 = dino_img.shape[::-1]
    w2, h2 = obstcl_img1.shape[::-1]
    w3, h3 = obstcl_img2.shape[::-1]
    w4, h4 = obstcl_img3.shape[::-1]
    w5, h5 = game_over_img.shape[::-1]

    find_dino = cv2.matchTemplate(img_gray, dino_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(find_dino >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w1, pt[1] + h1), (0, 0, 255), 2)


    delta_time_dino = round((time.time() - prev_time) * 1000, 2)
    time_log.append(str(delta_time_dino))
    prev_time = time.time()

    if frame_counter % frame_delay_obstcl == 0:
        find_obstcl = cv2.matchTemplate(img_gray, obstcl_img1, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(find_obstcl >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0, 255, 0), 2)

    delta_time_obstcl1 = round((time.time() - prev_time) * 1000, 2)
    time_log.append(delta_time_obstcl1)
    prev_time = time.time()

    if frame_counter % frame_delay_obstcl == 0:
        find_obstcl = cv2.matchTemplate(img_gray, obstcl_img2, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(find_obstcl >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w3, pt[1] + h3), (0, 255, 0), 2)

    delta_time_obstcl2 = round((time.time() - prev_time) * 1000, 2)
    time_log.append(delta_time_obstcl2)
    prev_time = time.time()

    if frame_counter % frame_delay_obstcl == 0:
        find_obstcl = cv2.matchTemplate(img_gray, obstcl_img3, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(find_obstcl >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w4, pt[1] + h4), (0, 255, 0), 2)

    delta_time_obstcl3 = round((time.time() - prev_time) * 1000, 2)
    time_log.append(delta_time_obstcl3)
    prev_time = time.time()

    if  frame_counter % frame_delay_game_over == 0:
        find_game_over = cv2.matchTemplate(img_gray, game_over_img, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(find_game_over >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w5, pt[1] + h5), (0, 255, 0), 2)

    delta_time_game_over = round((time.time() - prev_time) * 1000, 2)
    time_log.append(delta_time_game_over)
    prev_time = time.time()

    delta_time = round((time.time() - start_time)*1000,2)
    time_string = 'T msec: ' + str(delta_time) + ' | FPS:' + str(round(1000/delta_time,0))
    print time_string
    cv2.putText(img_rgb, time_string, (10, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, 255,2)

    frame_counter_string = 'Frame #' + str(frame_counter)
    cv2.putText(img_rgb, frame_counter_string , (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, 255,2)

    #cv2.imwrite('res.png',img_rgb)

    cv2.imshow('frame', img_rgb)

    delta_time_all = round((time.time() - prev_time) * 1000, 2)
    time_log.append(delta_time_all)
    prev_time = time.time()

    print time_log

    if cv2.waitKey(1) & 0xFF == ord('w'):
        time.sleep(2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




cap.release()
cv.destroyAllWindows()


