import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture("Resources/cow.jpg")
whT = 320
confThreshold = 0.5

classFile = 'coco.names'
classNames = []
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

    # print(classNames)
    # print(len(classNames))

modelConfiguration = 'yolov3-320.cfg'
modelWeights = 'yolov3-320.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

def findObjects(outputs, img):
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidense = scores[classId]
            if confidense > confThreshold:
                w, h = int(det[2]*wT), int(det[3]*hT)
                x, y = int((det[0]*wT) - w/2), int((det[1]*hT) - h/2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidense))
                print(len(bbox))


while True:
    success, img = cap1.read()

    blob = cv2.dnn.blobFromImage(img, 1/255, (whT, whT), [0, 0, 0], 1, crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
#    print(layerNames)
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]
    print(outputNames)
    # print(net.getUnconnectedOutLayers())

    outputs = net.forward(outputNames)
    # print(len(outputs))
    # print(type(outputs[0]))
    # print(outputs[0].shape)
    # print(outputs[1].shape)
    # print(outputs[2].shape)

    # print(outputs[0][0])
    findObjects(outputs, img)

    cv2.imshow("image", img)
    cv2.waitKey(0)