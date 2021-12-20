# Importing required libraries

import cv2
import mediapipe as mp
import time


# HandDetector class having 2  major functions
# 1. FindHands :-
# a. Will be searching for hands in video and will  be creating hand location
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands   ##
        self.hands = self.mpHands.Hands() ##
        self.mpDraw = mp.solutions.drawing_utils ##
        self.tipIds = [4, 8, 12, 16, 20]  ###
        self.volbar = 400
        self.volper = 0
        self.minVol = 100
        self.maxVol = 200

    def findHands(self, img, draw=True):
        imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        self.lmList = []
        #print("Hello ---")
        #print(self.results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h) ##
                #print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                # if id==4:
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return self.lmList

    def FingersUp(self):
        fingers = []

        # thumb
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4-Fingers
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def ThicknessChanger(self,img,brushThickness,lmList):
        import numpy as np
        import math
        #mList = detector.findPosition(img,draw=False)
        if len(lmList) != 0:
        #  print(lmList)
            x1,y1=lmList[4][1],lmList[4][2]
            x2,y2=lmList[20][1],lmList[20][2]
            cx,cy= (x1+x2) //2 , (y1+y2)//2


            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
            cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)


            length=math.hypot(x2-x1,y2-y1)
            #print(length)
            ##Hand range 50-300
            # Volume range -65 -> 0

            brushThickness = np.interp(length,[50,220],[self.minVol,self.maxVol])
            volbar = np.interp(length,[50,220],[400,150])
            volPer = np.interp(length,[50,300],[0,100])

            #print(int(length),thickness)
            #volume.SetMasterVolumeLevel(vol, None)

            if length<50:
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
        cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'Volume:{int(volPer)} %',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 3)

        cv2.rectangle(img,(1100,630),(1200,680),(255,255,0),cv2.FILLED)
        cv2.putText(img,f'End',(100,100),cv2.FONT_HERSHEY_COMPLEX, 1, (232, 12, 0), 3)

        if 630<x1<680:
            return brushThickness

""""
def main():

    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)


        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
    """
