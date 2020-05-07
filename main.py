import numpy as np
import cv2
import csv
import os

imgb=cv2.imread("../Images/bird.jpg")
imgc=cv2.imread("../Images/cat.jpg")
imgf=cv2.imread("../Images/flowers.jpg")
imgh=cv2.imread("..\Images\horse.jpg")
path=["../Images/bird.jpg","../Images/cat.jpg","../Images/flowers.jpg","../Images/horse.jpg"]
img=[imgb,imgc,imgf,imgh]

    
def A():
    with open("../Generated/mycsv.csv","w",newline='')as f:
       writer=csv.writer(f)
       writer.writerow(["Image","Height","Width","Channel","Color at center"])
       for i in range(4):
           h,w,c=img[i].shape
           name=os.path.basename(path[i])
           name=os.path.splitext(name)
           color=img[i][200,320]
           writer.writerow([name[-2]+name[-1],h,w,c,color])

def B():
    imgc[:,:,0]=0
    imgc[:,:,1]=0
    red_image=imgc
    cv2.imwrite("../Generated/cat_red.jpg",red_image)

def C():
    b,g,r=cv2.split(imgf)
    alpha=np.ones(b.shape,dtype=b.dtype)*50
    imgf_bgra=cv2.merge((b,g,r,alpha))
    imgf_bgra=cv2.addWeighted(imgf_bgra,1,imgf_bgra,1,0)
    cv2.imwrite("../Generated/flowers_alpha.png",imgf_bgra)  
    
def D():
    b,g,r=cv2.split(imgh)
    new=cv2.merge((b*0.11,g*0.59,r*0.3))
    cv2.imwrite("../Generated/horse_gray.jpg",new)  

A()
B()
C()
D()    