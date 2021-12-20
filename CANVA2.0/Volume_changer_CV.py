from numpy.lib.type_check import mintypecode
#from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#from ctypes import cast, POINTER
#from comtypes import CLSCTX_ALL
import cv2
import time
import numpy as np
import Module as htm
import math


#########################
wCam , hCam = 640 , 480
#########################

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)


#pTime=0
#volume=0
volbar=400
#vol=0
volPer=0

detector = htm.handDetector(detectionCon=0.7)
##
minVol = 100
maxVol=200
###

while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList) != 0:
     #   print(lmList)

        x1,y1=lmList[4][1],lmList[4][2]
        x2,y2=lmList[12][1],lmList[12][2]
        cx,cy= (x1+x2) //2 , (y1+y2)//2


        cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)


        length=math.hypot(x2-x1,y2-y1)
        #print(length)
        ##Hand range 50-300
        # Volume range -65 -> 0

        thickness = np.interp(length,[50,220],[minVol,maxVol])
        volbar = np.interp(length,[50,220],[400,150])
        volPer = np.interp(length,[50,300],[0,100])

     #   print(int(length),thickness)
        #volume.SetMasterVolumeLevel(vol, None)

        if length<50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)


    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'Volume:{int(volPer)} %',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 3)


    #cTime =time.time()
    #fps=1/(cTime-pTime)
    #pTime=cTime

   # cv2.putText(img, f'FPS:{int(fps)}',(20,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0), 3)
   # cv2.putText(img, f'Hemang Jiwnani', (360, 70),cv2.FONT_HERSHEY_COMPLEX, 1, (232, 12, 0), 3)


    cv2.imshow('Img',img)
    cv2.waitKey(1)

class x():
    def ThicknessChanger():
        lmList = detector.findPosition(img,draw=False)
        if len(lmList) != 0:
        #  print(lmList)
            x1,y1=lmList[4][1],lmList[4][2]
            x2,y2=lmList[12][1],lmList[12][2]
            cx,cy= (x1+x2) //2 , (y1+y2)//2


            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
            cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)


            length=math.hypot(x2-x1,y2-y1)
            #print(length)
            ##Hand range 50-300
            # Volume range -65 -> 0

            thickness = np.interp(length,[50,220],[minVol,maxVol])
            volbar = np.interp(length,[50,220],[400,150])
            volPer = np.interp(length,[50,300],[0,100])

            #print(int(length),thickness)
            #volume.SetMasterVolumeLevel(vol, None)

            if length<50:
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
        cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'Volume:{int(volPer)} %',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 3)
