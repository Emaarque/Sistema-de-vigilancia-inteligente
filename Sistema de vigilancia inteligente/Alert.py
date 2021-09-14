from twilio.rest import Client
from datetime import datetime
import cv2

def Alert(texto):
    account_sid = 'AC1c5692cfc9751a2fa7a7140edcbba0c7' 
    auth_token = '738cb91e276503709d40a2d337ebb11b'  
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=texto,      
                              to='whatsapp:+5492392537311') 
def SaveImage(img):
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
    cv2.imwrite('detect/'+year_month+'.png',img)