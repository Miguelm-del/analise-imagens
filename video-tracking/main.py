import cv2 as cv 

cap = cv.VideoCapture("skate.mp4")

tracker = cv.legacy.TrackerCSRT_create()
success, img = cap.read()
bbox = cv.selectROI("Tracking",img,False)
tracker.init(img,bbox)

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv.rectangle(img,(x,y),((x + w),(y+h)),(255,0,0),3,1)
    cv.putText(img,"Tracking",(75,80),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,255  ,0),2)


while True:
    timer = cv.getTickCount()
    success, img = cap.read()
    
    success, bbox = tracker.update(img)
    
    if success:
        drawBox(img, bbox)
    else:
        cv.putText(img,"Lost",(75,80),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)

     
    
    fps = cv.getTickFrequency()/(cv.getTickCount()-timer)
    cv.putText(img, str(int(fps)) +" fps",(75,50),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)
    cv.putText(img,"Press 'q' for exit ",(250,350),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
    cv.imshow("Tracking Object",img)
    
        
    if cv.waitKey(1) & 0xff ==ord('q'):
        break