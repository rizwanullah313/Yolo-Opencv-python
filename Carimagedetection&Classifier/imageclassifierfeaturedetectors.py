import cv2
import numpy as np
import os

path = 'Qiamges'
orb = cv2.ORB_create(nfeatures=1000)

images = []
classNames = []
myList = os.listdir(path)
print(myList)
print('Total Classes Detected', len(myList))
for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
    print(classNames)

def findDes(images):
    desList=[]
    for img in images:
        kp,des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList

def finID(img, desList, thres=15):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList=[]
    finalVal = -1
    try:
        for des in desList:
           matches = bf.knnMatch(des, des2, k=2)
           good = []
           for m, n in matches:
            if m.distance < 0.75*n.distance:
                good.append([m])
        matchList.append(len(good))
       # print(matchList)
    except:
        pass
    if len(matchList)!=0:
        if max(matchList) > thres:
            finalVal = matchList.index(max(matchList))
    return finalVal

desList = findDes(images)
print(len(desList))

cap = cv2.VideoCapture(0)

while True:
    success, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    id = finID(img2, desList)
    if id != -1:
        cv2.putText(imgOriginal, classNames[id],(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)

    cv2.imshow('img2', imgOriginal)
    cv2.waitKey(0)


# img1 = cv2.imread("Qiamges/honda civic 4.jpg", 0)
# img2 = cv2.imread("Tiamge/honda civic 6.jpg", 0)

# orb = cv2.ORB_create(nfeatures=1000)

# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)

# imgKp1 = cv2.drawKeypoints(img1, kp1, None)
# imgKp2 = cv2.drawKeypoints(img2, kp2, None)


# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
# cv2.imshow("ImgKp1", imgKp1)
# cv2.imshow("ImgKp2", imgKp2)

# cv2.imshow("Image1", img1)
# cv2.imshow("Image2", img2)
# cv2.imshow("Images", img3)

cv2.waitKey(0)