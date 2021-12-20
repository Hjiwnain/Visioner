##Important Libraries
import mediapipe  ##Handetection 
import cv2
import time
import os
import numpy as np
import Module as htm
#####################

################################
brushThickness = 20
eraserThickness = 50
imgInv = 0
xp =0
yp=0
flag=0
###############################


#folderPath = 'Header'
folderPath = "header"
myList = os.listdir(folderPath)
#print(myList)                                                                       ##Comment out

overlayList = []

def BrushThicknesschanger():
    brushnew = detector.ThicknessChanger(img,brushThickness,lmList)
    return brushnew

# myList = ['5.png','4.png','3.png','2.png','1.png']
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')  ## (f'header/5.png)
    overlayList.append(image)  
#print(overlayList)                                                                 ##Comment out
header = overlayList[0] 
draColor=(255,0,255)   ##Sense

cap = cv2.VideoCapture(0)  ##video 
cap.set(3,1280)  
cap.set(4,720)

#import HandTrackingModule
detector = htm.handDetector(detectionCon = 0.7)   ########

imagecanvas = np.zeros([720,1280,3],np.uint8)

while True:

    #1. Import image
    success, img = cap.read()
    #print(success,img)
    img = cv2.flip(img,1)

    #2. Find Hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)

    if len(lmList)!=0:
        
       # print(lmList)

        #Tip of index and midle finger
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]


    #3. Check which fingers are up
        fingers = detector.FingersUp()
       # print(fingers)

    #4. if selection mode - Two fingers up
        if fingers[1] and fingers[2]:  ##True AND TRUE = TRUE 
            xp,yp =  0,0
            #print("Selection mode")
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
              #  elif 1100 <x1<1200:
                    #Sx1 = 150
               #     brushnew = BrushThicknesschanger()
                #    brushThickness = brushnew
                    #header = overlayList[4]
            cv2.rectangle(img,(x1,y1-25),(x2,y2+25),draColor,cv2.FILLED)


        elif fingers[0]:
            print("i AM IN")
            if 1100<x1<1200:
                brushnew = BrushThicknesschanger()
                brushThickness = brushnew
                print("Brsuh thickness :- "+str(brushnew))
                cv2.rectangle(img,(x1,y1-25),(x2,y2+25),(255, 16, 240),cv2.FILLED)
                while(flag != 1):
                    if fingers[4]:
                        flag = flag + 1
        
        

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
    cv2.imshow("Image",img)
    cv2.imshow("canvas",imagecanvas)
    cv2.imshow("Inv",imgInv)
    cv2.waitKey(1)
