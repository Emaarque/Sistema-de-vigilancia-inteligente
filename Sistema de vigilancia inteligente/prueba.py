import pywhatkit


def alert(img):
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')

pywhatkit.sendwhats_image(phone_no='+5492392537311',
                        img_path='/home/ia1/cv/detect/2021-09-17,08-53-48.png',
                        caption='hay una persona',
                        tab_close=True)