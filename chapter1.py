import cv2
import numpy as np


# cap = cv2.VideoCapture("Resources/Carv.mp4")
# while True:
  #  success, img = cap.read()
  #  cv2.imshow("Video", img)
  #  if cv2.waitKey(1) & 0xFF == ord('q'):
  #      break



# upload image
# print("Package imported")
# img = cv2.imread("Resources/car1.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)



# img = cv2.imread("Resources/car.jpg")
# kernel = np.ones((5,5),np.uint8)

# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny = cv2.Canny(img,150,200)
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Dialation Image", imgDialation)
# cv2.imshow("Eroded Image",imgEroded)

# cv2.waitKey(0)


# img = cv2.imread("Resources/images (3).jpg")
# print(img.shape)
# imgResize = cv2.resize(img, (800, 600))
# print(imgResize.shape)
# imgCropped = img[0:200, 200:500]

# (194, 259, 3) height, width, channel
# cv2.imshow("Image", img)
# (600, 800, 3) width, height, channel
# cv2.imshow("Resize Image", imgResize)
# cv2.imshow("Cropped Image", imgCropped)
# cv2.waitKey(0)



# img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:]=255,0,0

# cv2.line(img,(0,0),(300,300),(0,255,0),3)
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img,(0,0,),(250,350),(250,4,2),4)
# cv2.rectangle(img,(0,0,),(250,350),(250,4,2),cv2.FILLED)
# cv2.circle(img,(300,400),50,(255,255,0),5)
# cv2.putText(img," Rizwan ",(300,100),cv2.FONT_HERSHEY_SIMPLEX,1,(250,2),1)
# cv2.imshow("Image",img)

# cv2.waitKey(0)