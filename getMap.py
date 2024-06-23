import pickle
import cv2
import numpy as np
 
width, height = 1920, 1080  
 
cap = cv2.VideoCapture(0)  
cap.set(3, width)  
cap.set(4, height)  
points = np.zeros((4, 2), int)  

counter = 0 
 
 
def mousePoints(event, x, y, _, __):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        points[counter] = x, y  
        counter += 1  
        print(f"{points}")
 
while True:
    success, img = cap.read()
 
    if counter == 4:
        fileObj = open("map.p", "wb")
        pickle.dump(points, fileObj)
        fileObj.close()
        print("Points saved: map.p")
        cap.release()
        cv2.destroyAllWindows()
 
 
    for x in range(0, 4):
        cv2.circle(img, (points[x][0], points[x][1]), 3, (0, 255, 0), cv2.FILLED)
 
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    cv2.waitKey(1)  
 
