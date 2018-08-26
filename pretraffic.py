import cv2 as cv
import numpy as np
import os
import Image
# Playing video from file:
cap = cv2.VideoCapture('traffic.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1
    im=Image.open('name','r')
    pix_val=list(im.getdata())
    #if(pix_val<#808080)
    print ('Signal Change')

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

