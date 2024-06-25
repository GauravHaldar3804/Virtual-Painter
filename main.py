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

brushThickness = 15
brushThicknessMin = 5
brushThicknessMax = 50
brushThicknessRange = brushThicknessMax - brushThicknessMax
brushBar = 420

eraserThickness = 60
eraserThicknessMin = 30
eraserThicknessMax = 150
eraserThicknessRange = eraserThicknessMax - eraserThicknessMax
eraserBar = 410

xp = 0
yp = 0
imgCanvas = np.zeros((720,1280,3),np.uint8)
header = overlayList[0]
header1 = overlayList[0]


drawColor = (255,0,255)
eraseColor = (0,0,0)
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
            # print("Selection Mode")
            header = header1
            xp = 0
            yp = 0
            
            if y1 < 125:

                if 250<x1<450:
                    drawColor = (255,0,255)
                    header = overlayList[0]

                elif 550<x1<750:
                    drawColor = (0,255,0)
                    header = overlayList[1]
                    header1 = header

                elif 800<x1<950:
                    drawColor = (255,0,0)
                    header = overlayList[2]
                    header1 = header

                elif 1050<x1<1200:
                    eraseColor = (0,0,0)
                    header = overlayList[3]
                    header1 = header
            if 25 < x1 < 85 and 145 < y1 < 500 :
                cv.rectangle(img,(43,int(y1)),(62,500),drawColor,cv.FILLED)
                brushThickness = int(np.interp(y1,[145,500],[brushThicknessMax,brushThicknessMin]))
                print(brushThickness,y1)
                brushBar = y1

            if 1200 < x1 < 1265 and 145 < y1 < 500 :
                cv.rectangle(img,(1215,int(y1)),(1240,500),eraseColor,cv.FILLED)
                eraserThickness = int(np.interp(y1,[145,500],[eraserThicknessMax,eraserThicknessMin]))
                print(eraserThickness,y1)
                eraserBar = y1

            

            cv.rectangle(img , (x1 , y1-25) , (x2 , y2+25) , drawColor , cv.FILLED)
        # 5. If Drawing Mode - Index finger is up
        elif fingers[1] and fingers[2] == False:
            # print("Drawing Mode")
            header = header1
            cv.circle(img,(x1,y1),brushThickness//2,drawColor,cv.FILLED)

            if xp == 0 and yp == 0:
                xp = x1
                yp = y1
                

            cv.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
            xp = x1
            yp = y1
        else :
            eraseColor = (0,0,0)
            header = overlayList[3]
            cv.line(imgCanvas,(xp,yp),(x1,y1),eraseColor,eraserThickness)
            cv.circle(img,(x1,y1),eraserThickness//2,eraseColor,cv.FILLED)
            if xp == 0 and yp == 0:
                xp = x1
                yp = y1
            xp = x1
            yp = y1

    cv.rectangle(img,(40,145),(65,500),(255,255,0),3)
    cv.putText(img,f"{str(int(brushThickness))}",(30,530),cv.FONT_HERSHEY_SIMPLEX,1,drawColor,2)
    cv.putText(img,f"Brush",(20,560),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv.putText(img,f"Thickness",(5,590),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv.rectangle(img,(43,int(brushBar)),(62,500),drawColor,cv.FILLED)

    cv.rectangle(img,(1215,145),(1240,500),(255,255,0),3)
    cv.putText(img,f"{str(int(eraserThickness))}",(1200,530),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
    cv.putText(img,f"Eraser",(1140,560),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv.putText(img,f"Thickness",(1120,590),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv.rectangle(img,(1215,int(eraserBar)),(1240,500),eraseColor,cv.FILLED)
    
    imgGray = cv.cvtColor(imgCanvas,cv.COLOR_BGR2GRAY)
    _ , imgInv = cv.threshold(imgGray , 10 , 255 , cv.THRESH_BINARY_INV)
    imgInv = cv.cvtColor(imgInv,cv.COLOR_GRAY2BGR)

    img = cv.bitwise_and(img,imgInv)
    img = cv.bitwise_or(img,imgCanvas)



    # Setting the Header image
    img[0:125,0:1280] = header
    cv.imshow("Image",img)
    cv.waitKey(1)
