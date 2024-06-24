import cv2 as cv
import numpy as np
import os
import handtrackingmodule as htm

folder = "Header"
myList = os.listdir(folder)

overlayList =[]

for imgPath in myList:
    image = cv.imread(f"{folder}/{imgPath}")
    overlayList.append(image)


header = overlayList[0]

cam = cv.VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)

detector = htm.handDetector(detectConf=0.85)

while True :
    # 1. Import image
    success , img = cam.read()
    img = cv.flip(img,1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    # 3. Check which fingers are up
    # 4. If Selection Mode - Two finger are up
    # 5. If Drawing Mode - Index finger is up

    # Setting the Header image
    img[0:125,0:1280] = header
    cv.imshow("Image",img)
    cv.waitKey(1)
