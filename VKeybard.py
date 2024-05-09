import subprocess

import cv2
from time import sleep
import cvzone
import pyperclip
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=int(0.8), maxHands=2)
keys = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '<-'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ",", ".", "/",'ok'],
    ['Space']
]
finaltext=''
def drawAll(img,buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), thickness=5)
    return img
class Button:
    def __init__(self,pos,text,size=[85,85]):
        self.pos = pos
        self.text = text
        self.size = size

buttonList= []

for i in range(len(keys)):
    for x, key in enumerate(keys[i]):
        buttonList.append(Button([100 * x + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img=detector.findHands(img)
    lmlist, bbox = detector.findPosition(img)
    img = drawAll(img, buttonList)
    if lmlist:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            if x < lmlist[8][0] < x + w and y < lmlist[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (176, 0, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), thickness=5)
                l, _, _ = detector.findDistance(8, 12, img)
                if l < 38:
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), thickness=5)
                    if(button.text=='<-'):
                        finaltext=finaltext[:-1]
                    elif button.text=='ok':
                        pyperclip.copy(finaltext)
                        cap.release()
                        cv2.destroyAllWindows()

                    else:
                        finaltext+=button.text

                    sleep(0.3)

    cv2.rectangle(img,(50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finaltext, (60,425), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), thickness=5)
    cv2.imshow('Image', img)
    cv2.waitKey(1)
