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

brushThichness = 15
eraserThickness = 100
xp = 0
yp = 0
imgCanvas = np.zeros((720,1280,3),np.uint8)
header = overlayList[0]
drawColor = (255,0,255)
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
    lmList,bbox = detector.findPosition(img,draw=False)

    if len(lmList) != 0:
        
        # Getting Landmarks For Index and Middlefinger
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()

        # 4. If Selection Mode - Two finger are up
        if fingers[1] and fingers[2]:
            print("Selection Mode")
            xp = 0
            yp = 0
            
            if y1 < 125:

                if 250<x1<450:
                    drawColor = (255,0,255)
                    header = overlayList[0]

                elif 550<x1<750:
                    drawColor = (0,255,0)
                    header = overlayList[1]

                elif 800<x1<950:
                    drawColor = (255,0,0)
                    header = overlayList[2]

                elif 1050<x1<1200:
                    drawColor = (0,0,0)
                    header = overlayList[3]

            cv.rectangle(img , (x1 , y1-25) , (x2 , y2+25) , drawColor , cv.FILLED)
        # 5. If Drawing Mode - Index finger is up
        elif fingers[1] and fingers[2] == False:
            print("Drawing Mode")
            cv.circle(img,(x1,y1),brushThichness//2,drawColor,cv.FILLED)

            if xp == 0 and yp == 0:
                xp = x1
                yp = y1

            if drawColor == (0,0,0):
                cv.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
                cv.circle(img,(x1,y1),eraserThickness//2,drawColor,cv.FILLED)
                

            cv.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThichness)
            xp = x1
            yp = y1

    imgGray = cv.cvtColor(imgCanvas,cv.COLOR_BGR2GRAY)
    _ , imgInv = cv.threshold(imgGray , 10 , 255 , cv.THRESH_BINARY_INV)
    imgInv = cv.cvtColor(imgInv,cv.COLOR_GRAY2BGR)

    img = cv.bitwise_and(img,imgInv)
    img = cv.bitwise_or(img,imgCanvas)



    # Setting the Header image
    img[0:125,0:1280] = header
    cv.imshow("Image",img)
    cv.waitKey(1)
