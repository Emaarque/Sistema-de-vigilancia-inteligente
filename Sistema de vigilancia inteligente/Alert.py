from datetime import datetime
import cv2
from pathlib import Path
import pywhatkit
 
def SaveImage(img):
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
    cv2.imwrite('detect/'+year_month+'.png',img)
    img_path= Path('detect/'+year_month+'.png')
    return img_path

def send_msj1(t, img_path):
    pywhatkit.sendwhats_image(phone_no='+5492392611662',
                        img_path= img_path,
                        caption= t,
                        tab_close=True)
def send_msj2(t, img_path):
    pywhatkit.sendwhats_image(phone_no='+5492392524855',
                        img_path= img_path,
                        caption= t,
                        tab_close=True)
def send_msj3(t, img_path):
    pywhatkit.sendwhats_image(phone_no='+5492392489549',
                        img_path= img_path,
                        caption= t,
                        tab_close=True)
def send_msj4(t, img_path):
    pywhatkit.sendwhats_image(phone_no='+5492392616215',
                        img_path= img_path,
                        caption= t,
                        tab_close=True)