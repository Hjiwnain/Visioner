##Important Libraries
import mediapipe  ##Handetection
import cv2
import time
import os
import numpy as np
import Module as htm
from cvzone.HandTrackingModule import HandDetector
import math
#####################

################################
brushThickness = 20
eraserThickness = 50
imgInv = 0
xp =0
yp=0
minVol = 0
maxVol = 20
length = 0
###############################


#folderPath = 'Header'
folderPath = "header"
myList = os.listdir(folderPath)
#print(myList)                                                                       ##Comment out
#myList = ['1.png','2.png','3.png','4,png','5.png']

overlayList = []
#save = cv2.imread(f'/Users/hemangjiwnani/Documents/CANVA2.0/save.jpeg')

# myList = ['5.png','4.png','3.png','2.png','1.png']
#len(myList)
#>>> 5
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    ## ( f'header/5.png )
    ## (f'header/4.png)
    ## (f'header/3.png)
    ## (f'header/2.png)
    ## (f'header/1.png)
    overlayList.append(image)
#print(overlayList)                                                                 ##Comment out
header = overlayList[0]
#3 overlayList = ['5.png','4.png','3.png','2.png','1.png']
draColor=(255,0,255)   ##Sense

cap = cv2.VideoCapture(0)  ##video
cap.set(3,1280)
cap.set(4,720)

#import HandTrackingModule
detector = htm.handDetector(detectionCon = 0.7)   ########
detector2 = HandDetector(detectionCon=0.7,maxHands=2)
imagecanvas = np.zeros([720,1280,3],np.uint8)

while True:

    #1. Import image
    success, img = cap.read()
    #print(success)
    img = cv2.flip(img,1)

    #2. Find Hand landmarks
    hands,img = detector2.findHands(img)

    if len(hands)==1:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        fingers = detector2.fingersUp(hand1)
        #print(lmList)
        #Tip of index and midle finger
        x1,y1 = lmList[8][0],lmList[8][1]
        x2,y2 = lmList[12][0],lmList[12][1]

    #3. Check which fingers are up
        #fingers = detector.FingersUp()
        #print(fingers)

    #4. if selection mode - Two fingers up
        if fingers[1] and fingers[2]:  ##True AND TRUE = TRUE 
            xp,yp =  0,0
           # print("Selection mode")
            ##Checking for the click 
            if y1 < 125:
                if 550<x1<650:
                    header = overlayList[0]
                    draColor = (0,128,0)
                elif 670 <x1<770:
                    header= overlayList[1]
                    draColor = (0,0,255)
                elif 790 <x1<890:
                    header= overlayList[2]
                    draColor = (255,255,0)
                elif 890 <x1<990:
                    header= overlayList[3]
                    draColor = (128,0,128)
                elif 990 <x1<1090:
                    header= overlayList[3]
                    draColor = (0,0,0)
                #elif 1100 <x1<1200:
                    #Sx1 = 150
                 #   brushnew = BrushThicknesschanger()
                  #  brushThickness = brushnew
                    #header = overlayList[4]

            cv2.rectangle(img,(x1,y1-25),(x2,y2+25),draColor,cv2.FILLED)

    #5. if Drawing mode - Index fingers up
        if fingers[1] and fingers[2] == False:  ## True and False == False [False == False]
           # xp,yp =  0,0                                                                              #check for this line
            cv2.circle(img,(x1,y1),15,draColor,cv2.FILLED)
          #  print("Drawing Mode")
            if xp==0 and yp==0:
                xp,yp=x1,y1
            if draColor == (0,0,0):
                cv2.line(img,(xp,yp),(x1,y1),draColor,eraserThickness)
                cv2.line(imagecanvas,(xp,yp),(x1,y1),draColor,eraserThickness)
            else:
                cv2.line(img,(xp,yp),(x1,y1),draColor,brushThickness)
                cv2.line(imagecanvas,(xp,yp),(x1,y1),draColor,brushThickness)
            xp,yp = x1,y1

    elif len(hands)==2:
        #print("Hello")
        hand2 =hands[1]
        handtype = hand2["type"]
        lmList = hand2["lmList"]
        #print("handtype of 2:- "+handtype)
        fingers = detector2.fingersUp(hand2)
        #print(fingers)
            #print(lmList)
        if fingers[0] and fingers[1]:
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
            brushThickness = int(brushThickness)
            eraserThickness = brushThickness+30
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
           # cv2.rectangle(img,(1100,630),(1200,680),(255,255,0),cv2.FILLED)

    imgGray = cv2.cvtColor(imagecanvas,cv2.COLOR_BGR2GRAY)
    _ , imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    #print(img)
    #print(imgInv)
    img  = cv2.bitwise_and(img,imgInv)
    img= cv2.bitwise_or(img,imagecanvas)


    # 1. Setting the Navigation bar
    img[0:125,0:1280] = header
    #img = cv2.addWeighted(img,0.5,imagecanvas,0.5,0)
    #print(imgInv)
    #img[1145:1280,660:720] = header
    cv2.imshow("canvas",imagecanvas)
    cv2.imshow("Inv",imgInv)
    cv2.imshow("Image",img)
    cv2.imwrite('/Users/hemangjiwnani/Documents/CANVA2.0/img.jpg',img)
    cv2.waitKey(1)