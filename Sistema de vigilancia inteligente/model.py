
#Librerias
import cv2
import torch
from datetime import datetime
import funtions as f
from Alert import Alert,SaveImage

model= torch.hub.load('ultralytics/yolov5', 'yolov5x6')# modelo

#configuración del modelo
model.conf = 0.66#confidence threshold (0-1)
model.classes= [0]# detección de personas

cap=f.active_cam()

while(True):
    date = datetime.now()
    hour= int(date.strftime('%H'))
    if hour>=9 or hour<=17:
        frame=f.read_camera(cap)
        for i in frame:
            img= cv2.resize(i[0] ,(0,0),fx=0.3,fy=0.3)
            texto= i[1]
            result= model(img)
            #result.render()
            labels = result.xyxyn[0][:, -1].numpy()
            #cameras= f.all_cam(frame)
            if (labels.all()==0):
                Alert(texto)
                #print(labels)
                SaveImage(img)
       # cv2.imshow('camera', cameras)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #stop_cam(cap)
        #break