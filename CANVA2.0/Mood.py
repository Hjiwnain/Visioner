import cv2
from deepface import DeepFace
#from playsound import playsound
import os
import sys
#import subprocess



def Player():
    face_cascade = cv2.CascadeClassifier(
        r'C:\Users\Dell\Desktop\Canva-2.o-main\CANVA2.0\haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


    
    ret, frame = cap.read()
    result = DeepFace.analyze(img_path=frame, actions=[
                                'emotion'], enforce_detection=False)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        #for (x, y, w, h) in faces:
        #    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    User_Mode = result["dominant_emotion"]
    print(User_Mode)
    players(User_Mode)
    #subprocess.run('python Paint.py',shell=True)

    #'''cap.release()
        #cv2.destroyAllWindows()
        #
        #sys.exit()'''
        #txt = str(emotion)

    #cv2.putText(frame, txt, (50, 50),
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        #cv2.imshow('frame', frame)
        

    #if cv2.waitKey(1) & 0xff == ord('q'):
     #   pass

        

def players(User_Mode):

    if(User_Mode == 'happy'):
        os.startfile(r'C:\\Users\\Dell\\Downloads\\Happy.mpeg')
        print('Doing')
        sys.exit()
    elif(User_Mode == 'sad'):
        os.startfile(r'C:\\Users\\Dell\\Downloads\\Sad_1.mpeg')
        print('Doing')
        sys.exit()
    elif(User_Mode == 'suprise'):
        os.startfile(r'C:\\Users\\Dell\\Downloads\\Suprise.mpeg')
        print('Doing')
        sys.exit()
    elif(User_Mode == 'neutral'):
        os.startfile(r'C:\\Users\\Dell\\Downloads\\Sad_1.mpeg')
        sys.exit()
    elif(User_Mode == 'fear'):
        os.startfile(r'C:\\Users\\Dell\\Downloads\\Fear_1.mp3')
        sys.exit()
    elif(User_Mode == 'angry'):
        os.startfile(r'C:\\Users\\Dell\\Downloads\\Angry_1.mp3s')
        sys.exit()
    elif(User_Mode == 'disgust'):
        os.startfile(r'C:\\Users\\Dell\\Downloads\\New.mpeg')
        sys.exit()

Player()