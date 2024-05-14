import cv2
import cv2 as cv
import numpy as np
img=cv.imread('tu logo.png',0)
th=80
w,h=img.shape
print(w,h)
thr_img=np.array(img)

for x in range (w):
    for y in range (h):
        if thr_img[x,y]<=th:
            thr_img[x,y]=0
        else:
            thr_img[x,y]=255

cv.imshow('original',img)
cv.imshow('Thresholding',thr_img)
cv.waitKey(0)
cv.destroyAllWindows()