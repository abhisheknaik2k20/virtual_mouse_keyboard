import cv2
import numpy as np
import pyautogui

import HandTrackingModule as htm
import time
import autopy

# Webcam dimensions
wCam, hCam = 640, 480

# Frame parameters
frameR = 100
ptime=0

# Smoothening parameter for cursor movement
smoothening = 5

# Initialize previous and current cursor positions
plocx, plocy = 0, 0
clocx, clocy = 0, 0

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Get screen dimensions
wSrc, hSrc = autopy.screen.size()

# Initialize hand detector
detector = htm.handDetector(detectionCon=int(0.5), maxHands=1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img)

    if len(lmlist) != 0:
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]
        fingers = detector.fingersUp()
        print(fingers)

        # Draw rectangle for gesture region
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and fingers[0] == 0:
            # Interpolate hand position within gesture region
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wSrc))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hSrc))

            # Smoothen cursor movement
            clocx = plocx + (x3 - plocx) / smoothening
            clocy = plocy + (y3 - plocy) / smoothening

            # Check if the calculated coordinates are within the screen boundaries
            if 0 <= clocx <= wSrc and 0 <= clocy <= hSrc:
                autopy.mouse.move(wSrc - clocx, clocy)
                cv2.circle(img, (int(x1), int(y1)), 15, (255, 0, 255), cv2.FILLED)
                plocx, plocy = clocx, clocy

        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0 and fingers[0]==0:
            length, img, _ = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (int(x1), int(y1)), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

        if fingers[0] == 1 and fingers[1]==0 and fingers[3] == 0 and fingers[4] == 0 and fingers[2]==0:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wSrc))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hSrc))
            clocx = plocx + (x3 - plocx) / smoothening
            clocy = plocy + (y3 - plocy) / smoothening
            length, img, _ = detector.findDistance(4, 8, img)
            autopy.key.toggle(autopy.key.Code.DOWN_ARROW, True)
            if 0 <= clocx <= wSrc and 0 <= clocy <= hSrc:
                autopy.mouse.move(wSrc - clocx, clocy)
                cv2.circle(img, (int(x1), int(y1)), 15, (0, 255, 0), cv2.FILLED)
                cv2.circle(img, (int(x1), int(y1)), 15, (255, 0, 255), cv2.FILLED)
                plocx, plocy = clocx, clocy
        else:
            autopy.key.toggle(autopy.key.Code.DOWN_ARROW, False)

        if fingers[0] == 1 and fingers[1]==1 and fingers[3] == 0 and fingers[4] == 0 and fingers[2]==0:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wSrc))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hSrc))
            clocx = plocx + (x3 - plocx) / smoothening
            clocy = plocy + (y3 - plocy) / smoothening
            autopy.key.toggle(autopy.key.Code.UP_ARROW, True)
            if 0 <= clocx <= wSrc and 0 <= clocy <= hSrc:
                autopy.mouse.move(wSrc - clocx, clocy)
                cv2.circle(img, (int(x1), int(y1)), 15, (255, 0, 255), cv2.FILLED)
                plocx, plocy = clocx, clocy
        else:
            autopy.key.toggle(autopy.key.Code.UP_ARROW, False)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1 and fingers[0] == 0:
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
        if fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1 and fingers[0] == 1:
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)

    # Display image
    cv2.imshow("Image", img)

    # Check for exit command
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
