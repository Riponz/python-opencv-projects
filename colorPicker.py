import cv2 as c
import numpy as np

#create blank image
img= np.zeros([300,500,3], np.uint8)

#creating window
c.namedWindow("Color Picker")

#creating trackbar

def cross(x):
    pass

s1="0:OFF\n1:ON"

c.createTrackbar(s1,"Color Picker",0,1,cross)

#trackbar for the values of r,g,b

c.createTrackbar("R","Color Picker",0,255,cross)
c.createTrackbar("G","Color Picker",0,255,cross)
c.createTrackbar("B","Color Picker",0,255,cross)

#displaying the updated image
while True:
    img = c.cvtColor(img, c.COLOR_BGR2RGB)
    c.imshow("Color Picker", img)
    k=c.waitKey(1) & 0xFF
    if k==27:
        break

    #get trackbar values
    s=c.getTrackbarPos(s1,"Color Picker")
    r=c.getTrackbarPos("R","Color Picker")
    g=c.getTrackbarPos("G","Color Picker")
    b=c.getTrackbarPos("B","Color Picker")

    if s==0:
        img[:]=0
    else:
        img[:]=[r,g,b]

c.destroyAllWindows()