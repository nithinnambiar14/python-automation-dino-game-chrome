import pyautogui
from PIL import Image,ImageGrab
import time
from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)
    return

def takescreenshot():
    image=ImageGrab.grab().convert('L')
    return image

def ifcollide(data):
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(240, 470):
        for j in range(563, 650):
            if data[i,j]<100:
                hit("up")    
                return



    return


if __name__ == "__main__":
    time.sleep(2)

    while True:
        image=takescreenshot()
        data=image.load()
        ifcollide(data)
'''
    print(asarray(image))

     #Draw the rectangle for cactus
    for i in range(270, 415):
        for j in range(563, 650):
            data[i, j] = 0
    
    # Draw the rectangle for birds
    for i in range(270, 415):
        for j in range(490, 563):
            data[i, j] = 171

    image.show()
    #break
'''
      
    
