import cv2,time
from datetime import datetime
import pandas

first_frame=None
video=cv2.VideoCapture(0)
status_list=[None,None]
time_list=[]
df=pandas.DataFrame(columns=["START","END"])
while True:
    check, frame = video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    status=0
    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    status_list.append(status)
    status_list=status_list[-2:]

    if status_list[-1] == 0 and status_list[-2] == 1:
        time_list.append(datetime.now())
    if status_list[-1] == 1 and status_list[-2] == 0:
        time_list.append(datetime.now())

    cv2.imshow("Video Capture",gray)
    cv2.imshow("Delta Capture",delta_frame)
    cv2.imshow("Threshold Delta",thresh_frame)
    cv2.imshow("Color Frame",frame)
    print(status_list)

    key=cv2.waitKey(1)
    if key==ord('q'):
        if status ==1:
            time_list.append(datetime.now())
        break


for i in range(0,len(time_list),2):
    df=df.append({"START":time_list[i],"END":time_list[i+1]},ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows
