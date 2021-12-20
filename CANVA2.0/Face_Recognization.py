
from deepface import DeepFace
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/hemangjiwnani/Documents/CANVA2.0/Image.jpg')
plt.imshow(img)
prediction = DeepFace.analyze(img)
prediction['dominant_emotion']