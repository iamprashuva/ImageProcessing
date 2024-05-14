import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('tu logo.png',0)
plt.hist(img.ravel(),256,[0,256])

plt.show()
plt.savefig('hist1.png')

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))

cv2.imshow('Prash-Equalized Image',res)
cv2.imwrite('Prash-Equalized Image.png',res)

plt.hist(res.ravel(),256,[0,256])

plt.show()
plt.savefig('equal-hist1.png')