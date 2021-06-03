import numpy as np
import pandas as pd
import cv2

img = cv2.imread('ColorDet.jpg')

clicked = False
r = g = b = 0

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def getPixelCo_ord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, clicked
        clicked = True
        b,g,r = img[y,x]
        r = int(r)
        g = int(g)
        b = int(b)
       
cv2.namedWindow('IMAGE')
cv2.setMouseCallback('IMAGE',getPixelCo_ord)

def getColor_Name(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
    
while(1):

    cv2.imshow("IMAGE",img)
    if (clicked):
   
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        text = getColor_Name(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
