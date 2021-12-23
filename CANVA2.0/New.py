from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np
import math


minVol =  0
maxVol =  20
volbar = 400

cap = cv2.VideoCapture(0)
brushThickness = 0
#cap.set(3,1280)
#cap.set(4,720)
detector = HandDetector(detectionCon=0.7,maxHands=2)

while True:
    success,img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img,flipType=False)

    if hands:
        hand1 = hands[0]
        handtype = hand1["type"]
        Lmlist = hand1["lmList"]
        handtype = hand1["type"]
        #print("handtype of 0"+handtype)
        print(handtype)

    """if len(hands)==2:
        hand2 =hands[0]
        handtype = hand2["type"]
        lmList = hand2["lmList"]
        #print("handtype of 2:- "+handtype)
        finger = detector.fingersUp(hand2)
        #print(finger)
        #print(lmList)
        if finger[0]==0 and finger[1]:
            x1,y1= lmList[4][0],lmList[4][1]
            x2,y2= lmList[8][0],lmList[8][1]
            cx,cy= (x1+x2) //2 , (y1+y2)//2
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
            cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)


            length=math.hypot(x2-x1,y2-y1)
            #print(length)
                    ##Hand range 30-300
                    # Volume range -65 -> 0

            brushThickness = np.interp(length,[30,300],[minVol,maxVol])
            #print(brushThickness)
            volbar = np.interp(length,[30,300],[400,150])
            #print(volbar)
            volPer = np.interp(length,[30,300],[0,100])
            #print("Vol percent :- "+ str(volPer))

                    #print(int(length),thickness)
                    #volume.SetMasterVolumeLevel(vol, None)
        if length:
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
                cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'Thickness:{int(volPer)} %',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 3)

                cv2.rectangle(img,(1100,630),(1200,680),(255,255,0),cv2.FILLED)
              #  cv2.putText(img,f'End',(100,100),cv2.FONT_HERSHEY_COMPLEX, 1, (232, 12, 0), 3)
        print(brushThickness)
        """
            #print("hello")
    #print
    cv2.imshow("Image",img)
    cv2.waitKey(30)
#https://www.youtube.com/watch?v=3xfOa4yeOb0