import numpy as np
import cv2
import os

def draw_box(image, box, label):
    img = image.copy()
    x0,y0,x1,y1 = box
    color = (0,0,255)
    thickness = 1
    img = cv2.rectangle(img, (x0,y0), (x1,y1), color, thickness)
    img = cv2.putText(img, label, (10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),1,cv2.LINE_AA)
    return img

def show_result(image):
    leng = len(image)
    if leng % 2 == 0:
        image_hor1 = np.concatenate(tuple(image[:leng//2]),axis = 1)
        image_hor2 = np.concatenate(tuple(image[leng//2:]),axis = 1)
        image_ver =  np.concatenate((image_hor1,image_hor2),axis = 0)
    else:
        # image_hor1 = np.concatenate(tuple(image[:]),axis = 1)
        # image_hor2 = np.concatenate(tuple(image[leng]),axis = 1)
        image_ver =  np.concatenate(tuple(image[:]),axis = 1)
    return image_ver