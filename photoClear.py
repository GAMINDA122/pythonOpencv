import cv2 as cv

img = cv.imread('text.jpg')
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

_, result = cv.threshold(img,70,255,cv.THRESH_BINARY)

adaptive = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,41,6)

cv.imshow('Image',img)
cv.imshow('Result',result)
cv.imshow('Adaptive Result',adaptive)

cv.waitKey(0)
cv.destroyAllWindows()