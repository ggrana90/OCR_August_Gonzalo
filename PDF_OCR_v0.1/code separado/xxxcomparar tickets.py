import numpy as np
import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

per = 25

# Leer template
imgQ = cv2.imread('Tmp/0001-1.png')
# Resize
h,w,c = imgQ.shape
# imgQ = cv2.resize(imgQ,(w//2,h//2))

# detectar patron
orb = cv2.ORB_create(500)
kp1, des1 = orb.detectAndCompute(imgQ,None)
# impKp1 = cv2.drawKeypoints(imgQ,kp1,None)


path = 'Tmp'
myPicList = os.listdir(path)
print(myPicList)
for j,y in enumerate(myPicList):
    img = cv2.imread(path + "/"+y)
    # img = cv2.resize(img, (w // 2, h // 2))
    # cv2.imshow(y, img)
    kp2, des2 = orb.detectAndCompute(img,None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.match(des2,des1)
    matches.sort(key=lambda x:x.distance) #ordenar por calidad de match
    good = matches[:int(len(matches)*(per/100))]
    imgMatch = cv2.\
        drawMatches(img,kp2,imgQ,kp1,good[:20],None,flags=2) #cambiar value good para el numero de matches
    imgMatch = cv2.resize(imgMatch, (w // 1, h // 1))
    cv2.imshow(y, imgMatch)

#puntos de origen y destino de la comparacion de imagenes
    # srcPoints = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    # dstPoints = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    #
    # M, _ = cv2.findHomography(srcPoints,dstPoints,cv2.RANSAC,5.0)
    # imgScan = cv2.warpPerspective(img,M,(w,h))
    # imgScan = cv2.resize(imgScan, (w // 1, h // 1))
    # cv2.imshow(y, imgScan)




# cv2.imshow("Keypoints",impKp1)
# cv2.imshow("Output",imgQ)
cv2.waitKey(0)